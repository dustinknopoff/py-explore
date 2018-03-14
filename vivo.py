#!/usr/bin/env python
import requests
import webbrowser
from bs4 import BeautifulSoup


def main():
    """
    Adds reminder to Things.app if there is a pair of shoes under $60 in size 10.
    """
    results = getcontent()
    flag = False
    for result in results:
        if int(result['Price'].replace('$', '')) <= 60:
            if getSize(result['Link']):
                webbrowser.open('things:///add?title=Vivo%20Shoes%20On%20Sale!&'
                            'notes=https%3A%2F%2Fwww.vivobarefoot.com%2Fus%2Fshop%2Fsale%23q%3Dgender.Mens&when=Today')
                flag = True
    if flag is False:
        print('Nothing below $60 in size 10 today')


def getcontent():
    """
    Scrapes VivoBarefoot website for clearance men's shoes
    :return: list of dictionaries containing product names, prices, and links
    """
    site = 'https://www.vivobarefoot.com/us/shop/sale#q=gender.Mens'
    r = requests.get(site).content
    soup = BeautifulSoup(r, 'html.parser')
    products = soup.find('ul', attrs={'class': 'products'})
    lists = products.find_all('li')
    results = []
    for li in lists:
        d = {}
        names = li.strong.get_text()
        if 'Men' in names:
            if 'Women' not in names:
                d['Product'] = names
                d['Link'] = 'https://www.vivobarefoot.com' + li.a.get('href')
                price = li.find('span', attrs={'class', 'sale'}).get_text()
                d['Price'] = price
                results.append(d)
    return results


def getSize(link):
    """
    Determines if the clearance shoes' size 10 (US) in stock.
    :param link: link to a particular shoe
    :return: true if in stock.
    """
    r = requests.get(link).content
    soup = BeautifulSoup(r, 'html.parser')
    sizes = soup.find('div', attrs={'class': 'sizes'})
    s10 = sizes.find('button', attrs={'data-size': '43'})
    s10 = str(s10)
    if 'nostock' in s10:
        return False


if __name__ == '__main__':
    main()
