import abc #  定义抽象类

'''测试阶段init:
    1. 若存在则删除表
    2. 创建该表
    3. 导入想定数据
    
    部署实施阶段
    1. 若不存在则创建
    2. ......
'''
Flag_TestIsNeed =False  # 是否属于测试阶段flag


class BaseTable(object):
    def __init__(self,table_name):
        '''
        :param table_name: 指定子类实例的唯一表名
        '''
        self.table_name =table_name # 自己的表名,用在许多地方,必须在子类实例化下修改
    @abc.abstractmethod
    def table_initialize(self):  # 创建该表
        pass
    @abc.abstractmethod
    def insertData(self,rows_info):  # 增
        pass
    @abc.abstractmethod
    def deleteData(self,condition):  # 删
        pass
    @abc.abstractmethod
    def updateData(self):  # 改
        pass
    @abc.abstractmethod
    def selectData(self):  # 查
        pass

    def otherActions(self):
        pass