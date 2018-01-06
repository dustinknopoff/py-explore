from fanfiction import Scraper
scraper = Scraper()
# id = re.search('r\d', myfavs[0].get('link'))
id = 12729845
story = scraper.scrape_story_metadata(12729845)
for chap in range(0, story['num_chapters']):
    cont = scraper.scrape_chapter(id, chap)
    fname = story['title']+'-'+str(chap)
    with open(fname +'.txt', 'ab') as f:
        f.write(cont)