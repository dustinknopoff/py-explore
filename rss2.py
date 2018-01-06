import feedparser
feed = feedparser.parse('https://9to5mac.com/feed/')
print(feed.feed.title)
# print('-'*40 + '\n')
for a in feed.entries:
    file = open(a.title + '-' + feed.feed.title + '.html', 'w', encoding="utf-8")
    string = "<h1>"+ a.title + "</h1><br /> <h2>" + a.author + "</h2>"
    string = string + a.summary
    file.write(string)