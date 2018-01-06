from bs4 import BeautifulSoup
import requests, re, csv
def main():
    base = 'https://www.fanfiction.net/'
    baseminus = 'https://www.fanfiction.net'
    my_page = 'https://www.fanfiction.net/u/7423303/'
    page = requests.get(my_page)
    soup = BeautifulSoup(page.content, 'html.parser')
    favs = soup.find_all('div', class_="z-list")
    summs = soup.find_all('div', class_="z-indent")
    print(favs[0])
    with open('newindex.csv', 'a', encoding='utf8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Title", "Author", "Link", "Summary", "Pairings", "Completed", "World", "Thumbnail"])
        for x in range(0, len(favs)):
            link = base + 's/' + str(favs[x]['data-storyid'])
            completed = int(favs[x]['data-statusid']) - 1
            title = favs[x]['data-title']
            img = baseminus + str(favs[x].find('img')['src'])
            sum = summs[x].contents[0]
            begin = str(sum).split('<')
            summary = begin[0]
            reg = re.findall(r'u/\d{7}/', str(favs[x]))
            world = favs[x]['data-category']
            for y in range(0, len(reg)):
                if y is None:
                    author = 'None'
                else:
                    author = base + str(reg[0])
            tst = re.findall(r'\[(.*?)\]',str(favs[x]))
            pairs = tst
            for i in range(0, len(tst)):
                pairs = []
                if i is  None:
                    pairs = 'None'
                else:
                    pairs = str(tst).replace(',', ' ')
                    pairs = pairs.replace('[', '')
                    pairs = pairs.replace(']', '')
                    pairs = pairs.replace('\'', '')
            writer.writerow([title, author, link, summary, pairs, completed, world, img])
        print(str(len(favs) + 1) + ' stories added to newindex.csv')

if __name__ == "__main__":
    main()