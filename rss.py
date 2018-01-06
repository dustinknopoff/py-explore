import feedparser
feed = feedparser.parse('https://daringfireball.net/feeds/articles')
print(feed.feed)
print('-'*40 + '\n')
for a in feed.entries:
    file = open(a.title + '-' + feed.feed.title + '.html', 'w', encoding="utf-8")
    str = "<h1>"+a.title+"</h1><br /> <h2>By Daring Fireball </h2>"
    str = str + a.content[0].value
    file.write(str)