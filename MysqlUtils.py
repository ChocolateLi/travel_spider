import pymysql
import os
import json
import traceback

class Mysql():
    
    def __init__(self,file_name,file_path) -> None:
        # 初始化mysql数据库
        try:
            # 找到配置文件
            config = self.find_file(file_name,file_path)
            # 加载配置文件
            with open(config,'r') as file:
                load_dict = json.load(file)
            self.conn = pymysql.connect(**load_dict)
        except Exception as e:
            # 日志功能后面再加
            traceback.print_exc()
            print("cannot create mysql connect")

        self.cursor = self.conn.cursor()


    # 查找数据库的json文件
    def find_file(self,file_name,file_path):
        for root,dirs,files in os.walk(file_path):
            if file_name in files:
                return os.path.join(root,file_name)

    # 执行语句
    def exec(self,sql,val):
        # 插入、删除、更新、查找语句
        try:
            # 执行sql
            self.cursor.execute(sql,val)
            # 提交到数据库执行
            self.conn.commit()

        except Exception as e:
            # 打印异常信息
            traceback.print_exc()
            # 发生错误则回滚
            self.conn.rollback()

    # 执行语句
    def exec(self,sql):
        # 插入、删除、更新、查找语句
        try:
            # 执行sql
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.conn.commit()

        except Exception as e:
            # 打印异常信息
            traceback.print_exc()
            # 发生错误则回滚
            self.conn.rollback()
            
    # 插入一条数据
    def insert_one(self,sql,val):
        self.exec(sql,val)

    # 随机采样
    def sample(self,sql):
        self.exec(sql)
        # 获取所有记录列表
        results = self.cursor.fetchall()
        return results

    # 关闭数据库和游标
    def close(self):
        self.conn.close()
        self.cursor.close()

# if __name__ == '__main__':
    
    # 初始化数据库
    # file_name = "db_config.json"
    # file_path = "."
    # mysql = Mysql(file_name,file_path)

    # # 测试随机采样
    # sql = "select * from travel2 where length<=4096 and length>=512 and title!='NULL' and publish != '' order by RAND() limit 500"
    # results = mysql.sample(sql)

    # print(results)

#     sql = "insert into travel_test (region,city,url,title,publish,length,text) values (%s,%s,%s,%s,%s,%s,%s)"
#     val = ('华南','广州','https://you.ctrip.com/travels/guangzhou152/3968407.html','亲子南沙游｜广州周末游度假胜地','2020-09-03','1906','最南端的南沙南接 东莞 市、 中山 市、 深圳 ，毗邻 香港澳门 ，是 中国 南方通往世界的门户城市，南沙依托海洋与水网资源，珠 江口 岛屿众多，水道密布，构成了独特的珠江水网水乡景观。南沙已变成 广州 重点规划的旅游发展地， 广州 周边的最好玩之处，毗邻伶仃洋，因独有的咸 淡水 环境孕育了鲜甜的水产，滔滔珠江水，至南部出海处聚沙成滩，南沙的资源之多，目不暇接，南沙港邮轮码头，联通国际邮轮的航线，，可以祈福，许愿，吃素，带着父母来特别合适，新晋的蒲州花园最近成为热门的拍摄网红点，还有南沙湿地公园，十九涌十四涌海鲜水果一条街，入住 广州 南沙越秀酒店，无论是短途旅行，还是周末两天一夜，都被安排得明明白白，想起南沙的好吃好玩，真有点迫不及待。今年不适合跨省跨国旅行，发掘 广州 周边最好玩变成我们暑假的重要任务。吃住一条龙，才是正确打开暑假的模式，让我们都抓住暑假的尾巴吧。对于资深的吃货来说，夏天就是一个绝佳的季节，因为有南沙的海鲜在召唤你。南沙盛产番薯，番石榴，木瓜，杨桃，火龙蕉，神湾菠萝，新垦莲藕等，因为生态环境非常好，品质极佳，南沙吃海鲜也已经成为口碑，不时不吃就是地道 广州 人的标签。宝藏南沙，可谓深藏不露。对南沙的印象一直非常好，原因在我很多年前就经常来南沙，记得那时年纪小。南沙印象：像爱丽丝梦游仙境般的蒲州花园：这里还可以野餐噢，凹造型，没压力！：体验游艇的豪华，这边你还可以选择租赁一艘游艇，尝试出海扬帆的滋味。广州 南沙越秀喜来登酒店就坐落在这资源丰富的南沙核心地带。这次旅行印象最深就是吃道南沙特产番石榴做的甜品菜蔬。还有那些鲜到眉毛都跳起来的生猛海鲜。精选当季新鲜食材，不用跑到十九涌，在酒店就能开启一轮觅食度假。行政酒廊宽敞明亮，舒适，在这里商务办公，下午茶都十分合适。餐饮部分我最欣赏，无论是从下午茶亦或是中餐晚餐，一应俱全。带着孩子来酒店住，最希望的就是孩子可以吃得开心与满足。酒店还根据南沙的特色来配备款式独特的下午茶。孩子吃得可满足啦?酒店配套的健身中心硬件设备很不错，还有世界著名的健身设备“泰诺健”，可俯瞰南沙美景的户外恒温无边泳池让人蠢蠢欲动，这个季节唯有游泳才能让人远离炎热。晴天下的倒影，十分美丽儿子特别喜欢亲子的房间，无论多大年龄，都还是个孩子呀。我问他你会像小小朋友那样喜欢这些配套吗？他说尽管他是青少年了，但是依旧会很喜欢玩具，很喜欢这些让他回到过去童年记忆的布置。还和我说，应该要保持童真一面，那样活得才快乐。酒店客房共计291间，包括30间豪华及尊贵套房，客房均配备为品牌定制使用的特色睡床，55英寸超大纯平电视，高速上网及独立的浴缸及淋浴间。小朋友的欢迎甜品送到房间，可把他开心坏了。想想也是这个道理，在房间里和他玩起来了躲猫猫的游戏，一会儿穿进帐篷，一会儿说他已经变成玩偶，一会说妈妈，你帮忙把夜空灯打开，开心得很呢。挺开心他能喜欢亲子套房。环境惬意之余，今年情况很特殊，不能带他跨省跨国旅行，这样带他周边 广州 旅行也是也算是给他读书毕业的礼物呢。房间270度玻璃外屏，可以俯瞰部分南沙的景致，儿子就特别喜欢在窗边看地铁。帐篷是他小时候的最爱，这些他说都能让他找到乐趣。小朋友最喜欢就是每次住酒店都要泡浴缸，这是他享受的私密空间。夜幕降临，窗外灯光闪闪，为这个属于我们俩的亲子时光点缀了一番。我很喜欢他一起去旅行，这样我们母子关系更好，而且可以和他谈谈心，聊聊人生的意向。房间配套全部都是小朋友最适用的洗漱用品。非常贴心，连卫生间都给小朋友配备了幼童坐厕。夜晚降临，打开他的专属夜灯，漫天的繁星配备入眠，祝你有个好梦，儿子?晨早起来，被盛宴标帜餐厅的全日制自助餐丰富多样惊艳，现在他已经完全独立可以选择自己喜爱，又想品尝的美食。把自己打理得整整有条。日韩餐厅一直是我的挚爱，而儿子呢，最喜欢中餐采，南沙越秀酒店的两家餐厅，都能各自满足我们吃货的小心思。日料的放题，隐藏式菜单，满足了我不能跨国的心，足不出国门也能体验舌尖上的 日本 风情。这次我们就吃了这两家不同风味的。这是日韩餐厅“雅”。中式餐饮似乎最适合大多数人的胃，南沙的资源丰富，让大厨有了发挥创意，天马行空的余地。新鲜的食材，优越的地理环境，让南沙美食令人印象深刻。每一道都精致而味道独特。选用当季新鲜的配搭，给这个炎热的夏天带来了清爽可口的开始。完全可以告诉朋友们，我来酒店开启了一场舌尖上的南沙之旅。很开心两天一夜，可以选择了来南沙旅游，就算没有自驾也不用担心，南沙交通方便，地理位置条件成熟，周边配套的旅游设施众多，非常适合家庭来度假呢。不知道你又是否get了南沙的玩法了吗！')

#     mysql.insert_one(sql,val)

    

