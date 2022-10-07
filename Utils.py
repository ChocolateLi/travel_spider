import os
import pandas
import re

class Utils():

    def __init__(self):
        self.re_obj = re.compile(r"[!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~（）：【】《》▲→▼■←↑→↓↖↗↘↙★●◆‘’“”\s]+")

    # 查找文件
    def find_file(self,file_name,file_path):
        for root,dirs,files in os.walk(file_path):
            if file_name in files:
                return os.path.join(root,file_name)

    # 将mysql数据转化为csv格式的数据
    def mysql_to_csv(self,results,file_name,file_path):
        csv_file = self.find_file(file_name,file_path)
        data = pandas.DataFrame(results)
        # 写入数据
        # 因为内容有中文，所以要用编码utf_8_sig，注意这里如果用utf-8是不能显示中文的
        pandas.DataFrame.to_csv(data,csv_file,encoding="utf_8_sig")

    # 定义一个数据预处理的方法
    # 因为游记文本内容有太多不需要的符号了，以及太多空格
    def clear(self,text):
        text.replace('\n', '').replace('\r', '').replace(' ','').strip()
        return self.re_obj.sub("", text)

# if __name__ == '__main__':
#     utils = Utils();
#     str = """                                                                桂林小巷子青旅
                                                            
#                                                                 七星景区
                                                            
#                                                                 七星花桥
                                                            
#                                                                 漓江边
                                                            
#                                                                 漓江
                                                            
#                                                                 象鼻山
                                                            
#                                                                 象鼻山景
#                                                                 漓江边道路

#                                                                 路边演唱

#                                                             再次来桂林却碰上国庆长假，小逛了下，到处的人，加上天热，逛得没劲啊
                                                            
#                                                                 桂林火车站"""
#     print(len(str))
#     print("---------------------------")
#     str = utils.clear(str)
#     print(len(str))

    # str = "   哈哈哈   怎么了，   干嘛  "
    # print(str)
    # print(str.strip(" ").replace(" ",""))
