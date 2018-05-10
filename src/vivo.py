#!/usr/bin/env python

import webbrowser

import requests
from bs4 import BeautifulSoup


def main():
    """
    Adds reminder to Things.app if there is a pair of shoes under $60 in size 10.
    """
    clear = 'https://www.vivobarefoot.com/us/shop/sale#q=size.43~gender.Mens'
    reg = 'https://www.vivobarefoot.com/us/mens#q=size.43'
    results = [getcontent(clear), getcontent(reg)]
    flag = False
    for result in results:
        for elem in result:
            if int(elem['Price'].replace('$', '')) <= 60:
                webbrowser.open('things:///add?title=Vivo%20Shoes%20On%20Sale!&'
                                'notes=https://www.vivobarefoot.com/us/shop/sale#q=size.43~gender.Mens&when=Today')
                flag = True
    if flag is False:
        print('Nothing below $60 in size 10 today')


def getcontent(site):
    """
    Scrapes VivoBarefoot website for clearance men's shoes
    :return: list of dictionaries containing product names, prices, and links
    """
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
                try:
                    price = li.find('span', attrs={'class', 'sale'}).get_text()
                except AttributeError:
                    price = li.find('span', attrs={'class', 'price'}).get_text()
                d['Price'] = price
                results.append(d)
    return results


if __name__ == '__main__':
    main()
