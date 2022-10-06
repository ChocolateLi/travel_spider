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
        text.replace(u'\xa0', u'').replace('\n', '').replace('\r', '').replace(' ','').strip()
        return self.re_obj.sub("", text)

# if __name__ == '__main__':
    # utils = Utils();
    # str = """"""
    # print(len(str))
    # print("---------------------------")
    # str = utils.clear(str)
    # print(len(str))

    # str = "   哈哈哈   怎么了，   干嘛  "
    # print(str)
    # print(str.strip(" ").replace(" ",""))
