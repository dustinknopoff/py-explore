from bs4 import BeautifulSoup
import requests, zipfile, os, html2text
from fanfiction import Scraper
scraper = Scraper()

page = 'https://www.fanfiction.net/s/6013584/'
story = scraper.scrape_story_metadata(6013584)
for chap in range(1, story['num_chapters']):
    favs = requests.get(page + str(chap))
    soup = BeautifulSoup(favs.content, 'html.parser')
    main = soup.find('div', attrs={'id': 'storytext'})
    cleaned = main.prettify()
    h = html2text.html2text(cleaned)
    fname = story['title']+'-'+ str(chap)
    with open('/Users/Dustin/Downloads/'+ fname + '.md', 'a', encoding='utf8') as f:
        f.write(h)
