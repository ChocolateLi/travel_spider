from MysqlUtils import Mysql
from Utils import Utils

if __name__ == '__main__':

    # 初始化数据库
    file_name = "db_config.json"
    file_path = "./"
    mysql = Mysql(file_name,file_path)

    # 测试随机采样
    # sql = "select * from data where length<=5000 and length>=1000 and title!='NULL' and publish != '' order by RAND() limit 1500"
    
    # 全部文件导出
    sql = "select * from data"
    results = mysql.sample(sql)


    # 关闭mysql数据库
    mysql.close()

    # 将Mysql数据写入csv文件
    # 先在本目录中创建这个文件的名字
    csv_name = "all_file.csv"
    csv_path = "./"
    utils = Utils()
    utils.mysql_to_csv(results,csv_name,csv_path)
    print("导出完成")
