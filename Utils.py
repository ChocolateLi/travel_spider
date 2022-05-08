import os
import pandas

class Utils():

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

