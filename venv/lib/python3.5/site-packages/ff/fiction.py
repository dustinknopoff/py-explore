import re, urllib2, bs4, unicodedata
from datetime import timedelta, date
import ff
# Constants
opener = urllib2.urlopen
root = 'https://www.fanfiction.net'

# REGEX MATCHES

# STORY REGEX
_STORYID_REGEX = r"var\s+storyid\s*=\s*(\d+);"
_CHAPTER_REGEX = r"var\s+chapter\s*=\s*(\d+);"
_CHAPTERS_REGEX = r"Chapters:\s*(\d+)\s*"
_WORDS_REGEX = r"Words:\s*([\d,]+)\s*"
_TITLE_REGEX = r"var\s+title\s*=\s*'(.+)';"
_DATEP_REGEX = r"Published:\s*<span.+?='(\d+)'>"
_DATEU_REGEX = r"Updated:\s*<span.+?='(\d+)'>"

# USER REGEX
_USERID_REGEX = r"var\s+userid\s*=\s*(\d+);"
_AUTHOR_REGEX = r"href='/u/\d+/(.+?)'"
_USERID_URL_EXTRACT = r".*/u/(\d+)"
_USERNAME_REGEX = r"<link rel=\"canonical\" href=\"//www.fanfiction.net/u/\d+/(.+)\">"
_USER_STORY_COUNT_REGEX = r"My Stories\s*<span class=badge>(\d+)<"
_USER_FAVOURITE_COUNT_REGEX = r"Favorite Stories\s*<span class=badge>(\d+)<"
_USER_FAVOURITE_AUTHOR_COUNT_REGEX = r"Favorite Authors\s*<span class=badge>(\d+)<"

# Useful for generating a review URL later on
_STORYTEXTID_REGEX = r"var\s+storytextid\s*=\s*storytextid=(\d+);"

# Used to parse the attributes which aren't directly contained in the
# JavaScript and hence need to be parsed manually
_NON_JAVASCRIPT_REGEX = r'Rated:(.+)'
_HTML_TAG_REGEX = r'<.*?>'

# Needed to properly decide if a token contains a genre or a character name
# while manually parsing data that isn't directly contained in the JavaScript
_GENRES = [
    'General', 'Romance', 'Humor', 'Drama', 'Poetry', 'Adventure', 'Mystery',
    'Horror', 'Parody', 'Angst', 'Supernatural', 'Suspense', 'Sci-Fi',
    'Fantasy', 'Spiritual', 'Tragedy', 'Western', 'Crime', 'Family', 'Hurt',
    'Comfort', 'Friendship'
]

# TEMPLATES
_STORY_URL_TEMPLATE = 'https://www.fanfiction.net/s/%d'
_CHAPTER_URL_TEMPLATE = 'https://www.fanfiction.net/s/%d/%d'
_USERID_URL_TEMPLATE = 'https://www.fanfiction.net/u/%d'

_DATE_COMPARISON = date(1970, 1, 1)


def _parse_string(regex, source):
    """Returns first group of matched regular expression as string."""
    return re.search(regex, source).group(1).decode('utf-8')


def _parse_integer(regex, source):
    """Returns first group of matched regular expression as integer."""
    match = re.search(regex, source).group(1)
    match = match.replace(',', '')
    return int(match)


def _parse_date(regex, source):
    xutime = _parse_integer(regex, source)
    delta = timedelta(seconds=xutime)
    return _DATE_COMPARISON + delta


def _unescape_javascript_string(string_):
    """Removes JavaScript-specific string escaping characters."""
    return string_.replace("\\'", "'").replace('\\"', '"').replace('\\\\', '\\')


def _visible_filter(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    element = unicodedata.normalize('NFKD', element).encode('ascii', 'ignore')
    if re.match(r'<!--.*-->', str(element)):
        return False
    return True


class Story(object):
    def __init__(self, url=None, id=None):
        """ A story on fanfiction.net

        If both url, and id are provided, url is used.

        :type id: int
        :param url: The url of the story.
        :param id: The story id of the story.

        Attributes:
            id  (int):              The story id.
            chapter_count (int);    The number of chapters.
            word_count (int):       The number of words.
            author_id (int):        The user id of the author.
            title (str):            The title of the story.
            date_published (date):  The date the story was published.
            date_updated (date):    The date of the most recent update.
            author (str):           The name of the author.
            rated (str):            The story rating.
            language (str):         The story language.
            genre (str):            The genre(s) of the story.
            characters (str):       The character(s) of the story.
            reviews (int):          The number of reviews of the story.
            status (bool):          True if the story is complete, else False.
        """

        if url is None:
            if id is None:
                print "There must be a url or an id."
            else:
                url = _STORY_URL_TEMPLATE % int(id)

        source = opener(url).read()
        # Easily parsable and directly contained in the JavaScript, lets hope
        # that doesn't change or it turns into something like below
        self.id = _parse_integer(_STORYID_REGEX, source)
        try:
            # if there is only 1 chapter
            self.date_updated = _parse_date(_DATEU_REGEX, source)
            self.chapter_count = _parse_integer(_CHAPTERS_REGEX, source)
        except AttributeError:
            self.chapter_count = 1
            self.date_updated = None
        self.word_count = _parse_integer(_WORDS_REGEX, source)
        self.author_id = _parse_integer(_USERID_REGEX, source)
        self.title = _unescape_javascript_string(_parse_string(_TITLE_REGEX, source).replace('+', ' '))
        self.date_published = _parse_date(_DATEP_REGEX, source)
        self.author = _unescape_javascript_string(_parse_string(_AUTHOR_REGEX, source))

        # Tokens of information that aren't directly contained in the
        # JavaScript, need to manually parse and filter those
        tokens = [token.strip() for token in
                  re.sub(_HTML_TAG_REGEX, '', _parse_string(_NON_JAVASCRIPT_REGEX, source)).split('-')]

        # Both tokens are constant and always available
        self.rated = tokens[0].replace('Fiction', '').strip()
        self.language = tokens[1]

        # After those the remaining tokens are uninteresting and looking for
        # either character or genre tokens is useless
        token_terminators = ['Reviews: ', 'Updated: ', 'Published: ']

        # Check if tokens[2] contains the genre
        if tokens[2] in _GENRES or '/' in tokens[2] and all(token in _GENRES for token in tokens[2].split('/')):
            self.genre = tokens[2]
            # tokens[2] contained the genre, check if next token contains the
            # characters
            if not any(tokens[3].startswith(terminator) for terminator in token_terminators):
                self.characters = tokens[3]
            else:
                # No characters token
                self.characters = ''
        elif any(tokens[2].startswith(terminator) for terminator in token_terminators):
            # No genre and/or character was specified
            self.genre = ''
            self.characters = ''
            # tokens[2] must contain the characters since it wasn't a genre
            # (check first clause) but isn't either of "Reviews: ", "Updated: "
            # or "Published: " (check previous clause)
        else:
            self.characters = tokens[2]

        for token in tokens:
            if token.startswith('Reviews: '):
                # Replace comma in case the review count is greater than 9999
                self.reviews = int(token.split()[1].replace(',', ''))
                break
        else:
            # "Reviews: " wasn't found and for-loop not broken, hence no (0)
            # reviews
            self.reviews = 0

        # Status is directly contained in the tokens as a single-string
        if 'Complete' in tokens:
            self.status = True
        else:
            # FanFiction.Net calls it "In-Progress", I'll just go with that
            self.status = False

    def get_chapters(self):
        """
        A generator for all chapters in the story.
        :return: A generator to fetch chapter objects.
        """
        try:
            for number in range(1, self.chapter_count + 1):
                yield Chapter(story_id=self.id, chapter=number)
        except KeyboardInterrupt:
            print "!-- Stopped fetching chapters"

    def get_user(self):
        """
        :return: The user object of the author of the story.
        """
        return User(id=self.author_id)

    def print_info(self, attrs=['title', 'id', 'author', 'author_id', 'chapter_count', 'word_count', 'date_published',
                                'date_updated', 'rated', 'status', 'language', 'genre', 'characters', 'reviews']):
        """
        Print information held about the story.
        :param attrs: A list of attribute names to print information for.
        :return: void
        """
        for attr in attrs:
            print "%12s\t%s" % (attr, getattr(self, attr))

    def download(self, output='', message=True, ext=''):
        ff.download(self, output=output, message=message, ext=ext)

    # Method alias which allows the user to treat the get_chapters method like
    # a normal property if no manual opener is to be specified.
    chapters = property(get_chapters)


class Chapter(object):
    def __init__(self, url=None, story_id=None, chapter=None):
        """ A single chapter in a fanfiction story, on fanfiction.net

        :param url: The url of the chapter.
        :param story_id: The story id of the story of the chapter.
        :param chapter: The chapter number of the story.

        Attributes:
            story_id    (int):  Story ID
            number      (int):  Chapter number
            story_text_id (int):    ?
            title       (str):  Title of the chapter, or title of the story.
            raw_text    (str):  The raw HTML of the story.
            text_list   List(str):  List of unicode strings for each paragraph.
            text        (str):  Visible text of the story.
        """

        if url is None:
            if story_id is None:
                print 'A URL or story id must be entered.'
            elif chapter is None:
                print 'Both a stroy id and chapter number must be provided'
            elif story_id and chapter:
                url = _CHAPTER_URL_TEMPLATE % (story_id, chapter)

        source = opener(url).read()
        self.story_id = _parse_integer(_STORYID_REGEX, source)
        self.number = _parse_integer(_CHAPTER_REGEX, source)
        self.story_text_id = _parse_integer(_STORYTEXTID_REGEX, source)

        soup = bs4.BeautifulSoup(source, 'html5lib')
        select = soup.find('select', {'name': 'chapter'})
        if select:
            # There are multiple chapters available, use chapter's title
            self.title = select.find('option', selected=True).string.split(None, 1)[1]
        else:
            # No multiple chapters, one-shot or only a single chapter released
            # until now; for the lack of a proper chapter title use the story's
            self.title = _unescape_javascript_string(_parse_string(_TITLE_REGEX, source)).decode()
        soup = soup.find('div', id='storytext')
        # Try to remove AddToAny share buttons
        try:
            soup.find('div', {'class': lambda class_: class_ and 'a2a_kit' in class_}).extract()
        except AttributeError:
            pass
        # Normalize HTML tag attributes
        for hr in soup('hr'):
            del hr['size']
            del hr['noshade']

        self.raw_text = soup.decode()

        texts = soup.findAll(text=True)
        self.text_list = filter(_visible_filter, texts)
        self.text = '\n'.join(self.text_list)

class User(object):
    def __init__(self, url=None, id=None):

        if url is None:
            if id is None:
                print "Either url or id must be specified."
            else:
                self.userid = id
                url = _USERID_URL_TEMPLATE % id
        else:
            self.userid = _parse_integer(_USERID_URL_EXTRACT, url)

        source = opener(url).read()
        self._soup = bs4.BeautifulSoup(source, 'html5lib')
        self.url = url
        self.username = _parse_string(_USERNAME_REGEX, source)
        self.story_count = _parse_integer(_USER_STORY_COUNT_REGEX, source)
        self.favourite_count = _parse_integer(_USER_FAVOURITE_COUNT_REGEX, source)
        try:
            self.favourite_author_count = _parse_integer(_USER_FAVOURITE_AUTHOR_COUNT_REGEX, source)
        except AttributeError:
            self.favourite_author_count = None
    def get_stories(self):
        """
        Get the stories written by this author.
        :return: A generator for stories by this author.
        """
        xml_page_source = opener(root + '/atom/u/%d/' % self.userid).read()
        xml_soup = bs4.BeautifulSoup(xml_page_source)
        entries = xml_soup.findAll('link', attrs={'rel': 'alternate'})
        for entry in entries:
            story_url = entry.get('href')
            yield Story(story_url)

    def get_favourite_stories(self):
        """
        Get the favourite stories of this author.
        :return: A Story generator for the favourite stories for this author.
        """
        favourite_stories = self._soup.findAll('div', {'class': 'favstories'})
        for story in favourite_stories:
            link = story.find('a', {'class': 'stitle'}).get('href')
            link = root + link
            yield Story(link)

    def get_favourite_authors(self):
        """
        :return: User generator for the favourite authors of this user.
        """
        tables = self._soup.findAll('table')
        table = tables[-1]
        author_tags = table.findAll('a', href=re.compile(r".*/u/(\d+)/.*"))
        for author_tag in author_tags:
            author_url = author_tag.get('href')
            author_url = root + author_url
            yield User(author_url)
