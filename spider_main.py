from MysqlUtils import Mysql
from TravelSpider import Spider
import time
import random
from Utils import Utils
import json


if __name__ == '__main__':
 

    # 初始化数据库
    file_name = "db_config.json"
    file_path = "."
    mysql = Mysql(file_name,file_path)

    # 查找旅游城市的json文件
    utils = Utils()
    place_json_name = "place.json"
    place_json_path = "."
    places_file = utils.find_file(place_json_name,place_json_path)
    with open(places_file,'r') as file:
        places = json.load(file)

    # 获取旅游城市列表
    place_list = places['place_list']
    # 遍历每一个城市
    for place_info in place_list:
        region = place_info['region']
        place = place_info['place']
        place_url = place_info['place_url']
        place_url_page = place_info['place_url_page']

        # 定义爬虫对象
        spider = Spider(region,place,place_url,place_url_page)

        # 爬取url链接
        urls = spider.crawl_travel_url()
        print("%s有-%d-条url"%(place,len(urls)))

        start_time = time.time()

        for url in urls:
            # 休眠一下，避免识别成爬虫
            time.sleep(random.random() * 3)
            data = spider.get_url_detail(url)
            spider.saveData(mysql=mysql,data=data)

        end_time = time.time()

        print("爬取%s游记时长：%d" % (place,end_time-start_time))
        print("-----------分隔符-------------------")
    
    print("游记文本爬取成功")