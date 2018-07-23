#!/usr/bin/env python3.5
from collections import Counter

import nltk
import requests
from bs4 import BeautifulSoup


# def isApp(word):
#     """
#     Checks to see if given word is a Mac or iOS app.
#     :param word: a valid English word.
#     :return: True if word is the name of an application.
#     """
#     r = requests.get(f"https://www.macupdate.com/find/mac/{word}").content
#     soup = BeautifulSoup(r, 'html.parser')
#     for app in soup.find_all("td", class_="td-app-name"):
#         possible = app.span.get_text()
#         if word.capitalize() is possible:
#             return True
#     return False


def tokenize(alltext):
    """
    Given string, find the most common words longer then 5 chars. long
    :param alltext: a string of words.
    :return: Array of 40 most common words with 5+ chars.
    """
    all_words = nltk.tokenize.word_tokenize(alltext)
    all_word_dist = nltk.FreqDist(w.lower() for w in all_words)

    stopwords = nltk.corpus.stopwords.words('english')
    counter = Counter(w.lower() for w in alltext.replace('.', '').replace(',', '').replace("'", "").split()
                      if w not in stopwords and len(w) > 5)
    # print(counter.most_common(40))
    all_word_except_stop_dist = nltk.FreqDist(
        w.lower() for w in all_word_dist if w not in stopwords and len(w) > 5)
    most_common = all_word_except_stop_dist.most_common(40)
    return counter.most_common(100)


# def runner():
#     posts = get_all()
#     alltext = ""
#     for s in posts:
#         alltext += s
#     freqwords = tokenize(alltext)
#     apps = []
#     # for word in freqwords:
#     #     print(f"Working on {word}")
#     #     if isApp(word):
#     #         apps.append(word)
#     print(freqwords)
#     #
#     # print(isApp(freqwords[0]))


def get_all():
    """
    Gets all posts from What is Your Favorite App Ever Question on MPU Forum
    :return: Array of post contents.
    """
    allposts = []
    base = "https://talk.macpowerusers.com/t/what-is-your-favorite-app-ever/478?page="
    count = 1
    while 1:
        print(count)
        r = requests.get(base + str(count)).content
        soup = BeautifulSoup(r, 'html.parser')
        if 'Oops! That page doesn’t exist or is private.' in soup.h1.get_text():
            break
        else:
            # print("Here")
            soup = BeautifulSoup(r, 'html.parser')
            for post in soup.find_all("div", class_="post"):
                # print(post)
                allposts.append(post.get_text())
        count += 1
    return allposts


if __name__ == '__main__':
    posts = get_all()
    alltext = ""
    for s in posts:
        alltext += s
    freqwords = tokenize(alltext)
    print(freqwords)
