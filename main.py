'''
Make a scraping bot that will scrape news off Hacker News website and save those articles that have over 50 votes.
'''

import requests
from bs4 import BeautifulSoup

web_page = (requests.request('GET', 'https://news.ycombinator.com/news'))
soup = BeautifulSoup(web_page.text, 'lxml')

# news_heading = soup.find_all("tr", class_=["athing", "title", "storylink"])
# news_link = soup.find_all("a", class_=["storylink"])
news_heading = soup.find_all(class_=["score", "title", "storylink"])

def scrape():
    title = soup.find_all(class_="title")
    score = soup.find_all(class_="score")
    storylink = soup.find_all(class_="storylink", href=True)
    athing = soup.find_all(class_="athing")

    title_list = []
    score_list = []
    link_list = []

    title_list.clear()
    score_list.clear()
    link_list.clear()

    for item in athing:
        if item.text not in title_list:
            title_list.append(item.text)
    
    for point in score:
        score_list.append(point.text)

    for link in storylink:
        link_list.append(link["href"])        

    for t, s, l in zip(title_list, score_list, link_list):
        print(f"{t} \n Points: {s}   {l} ")

import time
while True:
    scrape()
    time.sleep(6)


"Just testing"