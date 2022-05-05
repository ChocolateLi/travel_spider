import os

class Utils():

    # 查找数据库的json文件
    def find_file(self,file_name,file_path):
        for root,dirs,files in os.walk(file_path):
            if file_name in files:
                return os.path.join(root,file_name)