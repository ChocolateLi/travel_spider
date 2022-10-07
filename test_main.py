
from ast import main

from TravelSpider import Spider

if __name__ == '__main__':
    test_url = "https://you.ctrip.com/travels/yangshuo702/1668662.html"
    data = Spider.get_url_detail(self=Spider,url=test_url)
    print(data['length'])
    
    