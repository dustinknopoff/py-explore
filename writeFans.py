import csv, json
from datetime import datetime
base = 'https://www.fanfiction.net'
myfile = open('./tutorial/favorites.json').read()
myfavs = json.loads(myfile)
with open('index.csv', 'a', encoding='utf8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Title", "Link", "Review", "Summary"])
    for line in myfavs:
        ttl = line.get('title')
        sum = line.get('summary')[0]
        reviews = base + line.get('reviews')
        link = base + line.get('link')
        writer.writerow([ttl, link, reviews, sum])
print('Done')

