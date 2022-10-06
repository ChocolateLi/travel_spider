import time

import requests
from bs4 import BeautifulSoup
import random
from lxml import etree
import re
from Utils import Utils

class Spider():
    def __init__(self,region,place,place_url,place_url_page) -> None:
        self.region = region
        self.place = place
        self.place_url = place_url
        self.place_url_page = place_url_page

        # 存储url的列表
        self.url_list = []

    # 定义一个获取每个网页游记url链接的方法，除开第一页
    def get_url(self,url):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.62',
            'referer': url,
        }
        res = requests.get(url=url, headers=headers)
        # 200响应时才爬取
        if(res.status_code == 200):   
            soup = BeautifulSoup(res.text, 'lxml')
            a_all = soup.find_all('a', class_="journal-item cf")
            base_url = "https://you.ctrip.com"

            for a in a_all:
                # 先进行拼接
                travel_url = base_url + a['href']
                # 然后存到list中
                self.url_list.append(travel_url)

            # with open('guangzhou_url.txt', 'a') as f:
            #     for a in a_all:
            #         travel_url = base_url + a['href']
            #         f.write(travel_url + '\n')

    # 爬取游记文本的url
    def crawl_travel_url(self):
        start_time = time.time()
        url_first = self.place_url
        # 第1页url爬取
        self.get_url(url_first)
        # 接下来从第2页开始爬取,爬取150页
        MAX_PAGE = 101
        for i in range(2,MAX_PAGE):
            # print('当前第-{}-页'.format(i))
            url = self.place_url_page.format(i)
            self.get_url(url)
            # print('当前第-{}-页爬取完成'.format(i))
            time.sleep(random.random()*3)

        
        end_time = time.time()
        print('爬取%s程序运行时间:%d'%(self.place,end_time-start_time))

        # 最后把存储url的列表返回
        return self.url_list

    # 解析游记url里的网页数据
    def get_url_detail(self,url):
        
        """
        url:游记文章地址
        """
        # 浏览器头部
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.62',
            'referer': url,
        }

        # 初始化数据，未获取则为-1
        travel_url,travel_title,pub_time,travel_text,text_len = ["NULL","NULL","NULL","NULL","NULL"]

        # 游记url
        travel_url = url

        # 获取响应内容
        res = requests.get(url=url,headers=headers)
        # 使用lxml解析网页内容
        html = etree.HTML(res.text) # 网页Element对象，可以使用xpath
        html_str = res.text # 网页字符对象，可以使用正则表达式

        # 获取文章标题
        try:
            travel_title = html.xpath("//div[@class='ctd_head_left']/h2/text()")[0].replace('\r','').replace('\n','').strip()
        except Exception as e:
            # traceback.print_exc()
            pass

        # 获取文章发布时间
        publish_time = ""
        try:
            publish_time = re.findall(r'\w+：\d{4}.\d{2}.\d{2}',html_str)[0].split('：')[1]
            # print(publish)
        except:
            try:
                publish_time = re.findall(r'发表.*?(\d{4}-\d{2}-\d{2})', html_str)[0]
            except Exception as e:
                # traceback.print_exc()
                pass

        pub_time = publish_time.replace('.','-')

        # 获取游记正文
        try:
            text = html.xpath("//div[@class='ctd_main_body']/descendant::p/text()") # 这是list列表
            travel_text = "".join(text)
            # 对文本数据做预处理
            travel_text = Utils.clear(travel_text)
        except Exception as e:
            # traceback.print_exc()
            pass

        # 获取文章长度
        try:
            text_len = str(len(travel_text))
        except Exception as e:
            # traceback.print_exc()
            pass

        # 获取喜欢数

        # 获取评论数

        # 获取浏览数

        # 构建数据
        data = {
            'region':self.region,
            'place':self.place,
            'url':travel_url,
            'title':travel_title,
            'publish':pub_time,
            'length':text_len,
            'text':travel_text
        }

        return data

    # 把数据保存到数据库中
    def saveData(self,mysql,data):
        region = data['region']
        place = data['place']
        url = data['url']
        title = data['title']
        publish = data['publish']
        length = data['length']
        text = data['text']

        # 满足512个字符才插入数据库，否则舍弃
        if(int(length)>512):
            sql = "insert into data (region,place,url,title,publish,length,text) values (%s,%s,%s,%s,%s,%s,%s)"
            val = (region,place,url,title,publish,length,text)
            mysql.insert_one(sql,val)

