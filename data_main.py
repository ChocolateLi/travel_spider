from MysqlUtils import Mysql
from Utils import Utils

if __name__ == '__main__':

    # 初始化数据库
    file_name = "db_config.json"
    file_path = "."
    mysql = Mysql(file_name,file_path)

    # 测试随机采样
    sql = "select * from travel2 where length<=4096 and length>=512 and title!='NULL' and publish != '' order by RAND() limit 500"
    results = mysql.sample(sql)

    # 关闭mysql数据库
    mysql.close()

    # 将Mysql数据写入csv文件
    file_name = "mysql_random.csv"
    file_path = "."
    utils = Utils()
    utils.mysql_to_csv(results,file_name,file_path)
