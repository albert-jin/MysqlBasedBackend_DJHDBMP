''' 所有表名等同于该py文件的文件名 '''
table_name = __file__.split('/')[-1].split('.')[0]
from database.base_table import BaseTable, Flag_TestIsNeed
import warnings


class ActivityDetails(BaseTable):
    def __init__(self,db, cursor, meta_info, simulator_info):
        '''
        在cursor下实例化一个表对象
        :param meta_info => {cols_info(dict)：{col_name:other info},primary_key(list):XX,foreign_key(dict):XX}  foreign例如：{'某个字段名称':'other_tablename(某个字段名称)'}
        :param cursor: 针对的database
        '''
        self.table_name = table_name
        self.db =db
        self.cursor = cursor
        self.meta_info = meta_info  # 表的列属性信息以及主键、外键约束
        self.simulator_info = simulator_info  # 该表的想定数据,仅在测试时用
        super().__init__(self.table_name)
        self.table_initialize()  # 对表进行特殊的初始操作

    def table_initialize(self):  # 测试阶段&部署阶段
        if Flag_TestIsNeed:
            self.__dropIfExist()
            self.__createIfNotExist()
            self.__importSimlatorData(self.simulator_info)
        else:
            self.__createIfNotExist()

    def __dropIfExist(self):  # Test 1
        try:
            # 存在表则删除重新创建
            sql_ ="DROP TABLE IF EXISTS " + self.table_name
            print(sql_)
            self.cursor.execute(sql_)
        except Exception as e:
            warnings.warn(message='Cause Error when dropping existed_table ' + self.table_name + ' Callback:' + str(e))

    def __createIfNotExist(self):  # Test 2 & Run 1
        try:
            # 存在表则删除重新创建
            foreign_key =''
            if self.meta_info['foreign_key']:
                foreign_key =','.join(['CONSTRAINT fk_{0} FOREIGN KEY ({1}) REFERENCES {2}'.format(
                    '_'.join([self.table_name,fk,self.meta_info['foreign_key'][fk]]),
                    fk,self.meta_info['foreign_key'][fk]) for fk in self.meta_info['foreign_key']])
            sql_ ='''CREATE TABLE IF NOT EXISTS {0}({1},PRIMARY KEY({2}){3}) Engine InnoDB;'''.format(
                self.table_name,','.join([' '.join(map(str,col_info)) for col_info in self.meta_info['cols_info'].items()]),
                ','.join(map(str,self.meta_info['primary_key'])),foreign_key)
            print(sql_)
            self.cursor.execute(sql_)
        except Exception as e:
            warnings.warn(
                message='Cause Error when creating unexisted_table ' + self.table_name + ' Callback:' + str(e))

    def __importSimlatorData(self,rows_info):  # Test3
        try:
            # 存在表则删除重新创建
            rows_info = "INSERT INTO {0} VALUES {1};".format(self.table_name, ','.join(['('+','.join(map(str,s_i))+')' for s_i in rows_info]))
            print(rows_info)
            self.cursor.execute(rows_info)
            self.db.commit()
        except Exception as e:
            warnings.warn(
                message='Cause Error when importing data into ' + self.table_name + ' Callback:' + str(e))
            self.db.rollback()

    def insertData(self,rows_info:list):
        try:
            assert len(rows_info) == len(self.meta_info['cols_info'])
            self.__importSimlatorData([rows_info])
            print('成功往{0}里插入一行数据:{1}'.format(self.table_name,rows_info))
        except Exception as e:
            warnings.warn(
                message='Cause Error when inserting one-row-data into ' + self.table_name + ' Callback:' + str(e))

    def deleteData(self,condition:str):
        '''
        删除满足条件的记录
        :param condition: 指定的条件
        :return:
        '''
        try:
            sql_ = "DELETE FROM {0} WHERE ".format(self.table_name) + condition
            print(sql_)
            # 执行SQL语句
            cursor.execute(sql_)
            # 提交修改
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()

    def updateData(self):
        pass

    def selectData(self):
        pass


if __name__ == '__main__':  # 在此对本模块functions进行test
    import random
    from pymysql import connect
    from database.all_info.all_tables_info import all_tables_info
    from database.all_info.DB_simulator_infos import DB_simulator_infos
    database = connect(host='127.0.0.1', database='db_djhdbmpt', user='root', password='QA199839199839qa', port=3306)
    cursor = database.cursor()
    test_table_obj =ActivityDetails(db=database,cursor=cursor,meta_info=all_tables_info['activity_details'],simulator_info=DB_simulator_infos['activity_details'])
    id_ =str(random.randint(100,10000000))
    test_table_obj.insertData(
        [id_, '\'test_activity_name_02\'', '\'团组织会\'', '\'2009-06-08 23:53:37\'', '\'2009-06-08 23:59:17\'','\'2009-06-08 23:53:17\'', '\'这是活动1的内容\'', 1, '\'这是活动的图片\'', '\'luo祥峰是个大学术毒瘤,以后的师弟选他要谨慎!!!!!!\'', '\'2009-06-08 23:53:17\'', 5.5,2.5, 1.5])
    test_table_obj.deleteData('id = '+id_)
    database.close()
