'''
Make a scraping bot that will scrape news off Hacker News website and save those articles that have over 50 votes.
'''

import requests, time, os
from bs4 import BeautifulSoup

class HackerNewsScraping:
    
    title_list = []
    score_list = []
    link_list = []
    final_list = []

    def __init__(self, link, minimum_vote):
        self.unchanged_link = link
        self.link = link
        self.minimum_vote = minimum_vote
        
    def unused_code(self):
        # self.news_heading = self.soup.find_all(class_=["score", "title", "storylink"])      
        pass 

    def scrape(self):

        self.web_page = (requests.request('GET', str(self.link)))
        self.soup = BeautifulSoup(self.web_page.text, 'lxml')

        self.score = self.soup.find_all(class_="score")
        self.storylink = self.soup.find_all(class_="titlelink", href=True)
        self.athing = self.soup.find_all(class_="athing")


        for item in self.athing:
            if item.text not in self.title_list:
                self.title_list.append(item.text)
        
        for point in self.score:
            self.score_list.append(point.text)

        for link in self.storylink:
            if link["href"] not in self.link_list:
                self.link_list.append(link["href"])        

        # Using the os module to write and open storage file so that it works on machine with almost all operating system.
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__)) # This code returns the absolute path of the current directory.
        storage_file = os.path.join(THIS_FOLDER, 'news.txt') # This code joins the absolute path of the current directory with the name of the current file.
        # news_file = open(storage_file, "a")
        with open(storage_file, "a") as news_file:

            for t, s, l in zip(self.title_list, self.score_list, self.link_list):
                if int(s.split()[0]) > self.minimum_vote and l not in self.final_list: # This condition checks if the score if more than 50 and if the link is not saved previously.
                    print(f"{t} \n Points: {s} \n Link: {l} ")
                    self.final_list.append(l)
                    news_file.write(f"{t} \n Points: {s} \n Link: {l} \n")
                
        # news_file.close()

    def scrape_upto_the_given_page(self, page_num=0):
        # Give the page_num parameter an integer value and it will scrape pages of hacker news equal to the value of page_num.

        self.page_num = input("Enter the page number upto which you want to scrape from. ")
        while True:
            try:
                int(self.page_num)
                break
            except:
                if type(self.page_num) != int:
                    print("Your input must be an integer. ")
                    self.page_num = input("Enter the page number you want to scrape from. ")
                    continue

        for pages in range(int(self.page_num)):
            self.link = self.unchanged_link
            self.link = f"{self.link}?p={pages}"
            
            try:
                self.scrape()
                time.sleep(1.5)
            except:
                print("No news remaining.")
    
    def scrape_given_page(self):
        self.page_num = input("Enter the page number you want to scrape from. ")
        while True:
            try:
                int(self.page_num)
                break
            except:
                if type(self.page_num) != int:
                    print("Your input must be an integer. ")
                    self.page_num = input("Enter the page number you want to scrape from. ")
                    continue
            
        self.link = self.unchanged_link
        self.link = f"{self.link}?p={self.page_num}"

        try:
            self.scrape()
        except:
            print("No news remaining.")

        
Bot_1 = HackerNewsScraping("https://news.ycombinator.com/news", 50)

Bot_1.scrape_upto_the_given_page()