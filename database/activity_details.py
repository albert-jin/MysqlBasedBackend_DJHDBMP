''' 所有表名等同于该py文件的文件名 '''
theModule_table_name = __file__.split('\\')[-1].split('/')[-1].split('.')[0]
from database.base_table import BaseTable, Flag_TestIsNeed
import warnings

from database.all_info.all_tables_info import all_tables_info
from database.all_info.DB_simulator_infos import DB_simulator_infos

class ActivityDetails(BaseTable):
    def __init__(self,db, cursor,meta_info=all_tables_info[theModule_table_name],simulator_info=DB_simulator_infos[theModule_table_name]):
        '''
        在cursor下实例化一个表对象
        :param meta_info => {cols_info(dict)：{col_name:other info},primary_key(list):XX,foreign_key(dict):XX}  foreign例如：{'某个字段名称':'other_tablename(某个字段名称)'}
        :param cursor: 针对的database
        '''
        self.table_name = theModule_table_name
        self.db =db
        self.cursor = cursor
        self.meta_info = meta_info  # 表的列属性信息以及主键、外键约束
        self.simulator_info = simulator_info  # 该表的想定数据,仅在测试时用
        self.allColsName =[]
        self.notNullColsName =[]
        super().__init__(self.table_name)
        self.table_initialize()  # 对表进行特殊的初始操作
        for k,v in self.meta_info['cols_info'].items():
            self.allColsName.append(k)
            if 'NOT' in v or 'not' in v:
                self.notNullColsName.append(k)

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
            # print(sql_)
            self.cursor.execute(sql_)
        except Exception as e:
            warnings.warn(message='Error when dropping existed_table ' + self.table_name + ' Callback:' + str(e))

    def __createIfNotExist(self):  # Test 2 & Run 1
        try:
            # 存在表则删除重新创建
            foreign_key =''
            if self.meta_info['foreign_key']:
                foreign_key = ',' + ','.join(['CONSTRAINT fk_{0} FOREIGN KEY ({1}) REFERENCES {2}'.format(
                    '_'.join([self.table_name,fk,self.meta_info['foreign_key'][fk]]).replace('(','_').replace(')',''),
                    fk,self.meta_info['foreign_key'][fk]) for fk in self.meta_info['foreign_key']])
            sql_ ='''CREATE TABLE IF NOT EXISTS {0}({1},PRIMARY KEY({2}){3}) Engine InnoDB;'''.format(
                self.table_name,','.join([' '.join(map(str,col_info)) for col_info in self.meta_info['cols_info'].items()]),
                ','.join(map(str,self.meta_info['primary_key'])),foreign_key)
            # print(sql_)
            self.cursor.execute(sql_)
        except Exception as e:
            warnings.warn(
                message='Error when creating unexisted_table ' + self.table_name + ' Callback:' + str(e))

    def __importSimlatorData(self,rows_info):  # Test3
        try:
            # 存在表则删除重新创建
            rows_info = "INSERT INTO {0} VALUES {1};".format(self.table_name, ','.join(['('+','.join(map(str,s_i))+')' for s_i in rows_info]))
            # print(rows_info)
            self.cursor.execute(rows_info)
            self.db.commit()
            print('成功往{0}里插入一行数据:{1}'.format(self.table_name,rows_info))
            return True
        except Exception as e:
            warnings.warn(
                message='Error when importing data into ' + self.table_name + ' Callback:' + str(e))
            self.db.rollback()

    def __insertData(self,row_info:list):
        try:
            assert len(row_info) == len(self.meta_info['cols_info'])
            if self.__importSimlatorData([row_info]):
                return True
        except Exception as e:
            warnings.warn(
                message='Cause Error when inserting one-row-data into ' + self.table_name + ' Callback:' + str(e))

    def insertDataWrap(self,ori_row_info: dict):
        '''step1:检查rows_info是否含有必须的字段,不符合则操作失败
           step2:将rows_info按照指定顺序格式投送到__insertData函数中
        '''
        try:
            row_info = []
            for colName in self.allColsName:
                if colName in ori_row_info:
                    row_info.append(ori_row_info[colName])
                elif colName in self.notNullColsName:
                    raise Exception('Invaild Value 在 insert 表({0}) =>don`t give me all NotNull value！缺失的NotNull属性为:{1}'.format(self.table_name,colName))
                else:
                    row_info.append('null')
            if self.__insertData(row_info=row_info):
                return True
        except Exception as e:
            warnings.warn(e.args)

    def deleteData(self,condition:str):
        '''
        删除满足条件的记录
        :param condition: 指定的删除条件
        :return:
        '''
        try:
            if not condition:
                raise Exception('didn`t set condition when delete rows from {0}'.format(self.table_name))
            sql_ = "DELETE FROM {0} WHERE ".format(self.table_name) + condition
            # print(sql_)
            # 执行SQL语句
            self.cursor.execute(sql_)
            # 提交修改
            self.db.commit()
            print('成功从{0}中删除特定数据,删除条件:{1}'.format(self.table_name,condition))
            return True
        except Exception as e:
            # 发生错误时回滚
            self.db.rollback()
            warnings.warn(
                message='Error when delete rows-info from {0} Error:{1}!'.format( self.table_name,e.args))
            return False

    def updateData(self,action:str,condition:str=''):
        '''
        用action来更新满足condition条件的记录
        :param condition: 指定的删除条件
        :return:
        '''
        try:
            if condition:
                condition ='WHERE '+condition
            sql_ = "UPDATE {0} SET {1} {2};".format(self.table_name,action,condition)
            print(sql_)
            # 执行SQL语句
            self.cursor.execute(sql_)
            # 提交修改
            self.db.commit()
            print('成功更新table {0}特定数据,更新条件:{1},更新操作:{2}'.format(self.table_name,condition,action))
            return True
        except Exception as e:
            # 发生错误时回滚
            self.db.rollback()
            warnings.warn(
                message='Error when update rows-info from {0} ,callback:{1}!'.format(self.table_name,e.args))
            return False

    def selectData(self,condition=''):
        '''
        获取满足条件的记录
        :param condition: 获取条件
        :return:
        '''
        try:
            if condition:
                condition ='WHERE '+condition
            sql_ = "SELECT * FROM {0} {1}".format(self.table_name,condition)
            #print(sql_)
            # 执行SQL语句
            self.cursor.execute(sql_)
            # 抓取数据表内容
            result =self.cursor.fetchall()
            print('成功从{0}中抓取{1}行特定数据'.format(self.table_name,len(result)))
            return result
        except Exception as e:
            warnings.warn(
                message='Cause Error when select rows-info from {0} Error:{1}!'.format(self.table_name,e.args))
            return 'failure'

if __name__ == '__main__':  # 在此对本模块functions进行test
    import random
    from pymysql import connect
    database = connect(host='127.0.0.1', database='db_djhdbmpt', user='root', password='QA199839199839qa', port=3306)
    cursor = database.cursor()
    test_table_obj =ActivityDetails(db=database,cursor=cursor)
    # id_ =str(random.randint(100,10000000))
    # test_table_obj.__insertData(
    # [id_, '\'test_activity_name_02\'', '\'团组织会\'', '\'2009-06-08 23:53:37\'', '\'2009-06-08 23:59:17\'','\'2009-06-08 23:53:17\'', '\'这是活动1的内容\'', 1, '\'这是活动的图片\'', '\'luo祥峰是个大学术毒瘤,以后的师弟选他要谨慎!!!!!!\'', '\'2009-06-08 23:53:17\'', 5.5,2.5, 1.5]
    # )
    id_ = str(random.randint(100, 10000000))
    test_table_obj.insertDataWrap(
        {'id': id_,
         'title':  '\'test_activity_name_02\'',
         'publisher_type': '\'团组织会\'',
         'start_time': '\'2009-06-08 23:53:37\'',
         'end_time': '\'2009-06-08 23:59:17\'',
         'deadline':  '\'2009-06-08 23:53:17\'',
         'content':'\'这是活动1的内容\'',
         'status': 1,
         'pictures': '\'这是活动的图片\'',
         'auditing_name': '\'luo祥峰是个大学术毒瘤,以后的师弟选他要谨慎!!!!!!\'',
         'auditing_date': '\'2009-06-08 23:53:17\'',
         'point_participant':'5.5',
         'point_organizer': '5.5',
         'pointer_others': '5.5'}
    )
    test_table_obj.deleteData('id = '+id_)
    print('SUV',test_table_obj.selectData())
    print('TESLA',test_table_obj.selectData('id =3'))
    test_table_obj.updateData(action='publisher_type =\'修改后的组织\'',condition='id =2')
    database.close()