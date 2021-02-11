from pymysql import connect
from database.all_info.all_tables_info import all_tables_info
from database.all_info.DB_simulator_infos import DB_simulator_infos

from database import *  # 导入了6张表的class,基于表类进行后台功能的开发
if __name__ == '__main__':
    database =connect(host='127.0.0.1',database='db_djhdbmpt',user='root',password='QA199839199839qa',port=3306)
    cursor =database.cursor()
    database.close()