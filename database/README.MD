## > 本文件夹下存放党建活动报名平台对应database下所有相关tables的创建·存储·直接读取相关以及相关操作
### 存储的表包括:
+ 以下的表格都在mysql数据库下的一个数据库database中(默认数据库名称DB_DJHDBMPT)
    + activity_activity ->activity_details  活动详情-表(包含活动详细·审核状态)
        + 对应database/activity_details.py的class类ActivityDetails
    + activity_student 活动审核-表(学生参与活动列表·包含活动名称·参与身份)
        + 对应database/activity_students.py的class类ActivityStudents
    + documents_notice 通知公告-表
        + 对应database/documents_notice.py的class类DocumentsNotice
    + documents_suggestion 学生建议
        + 对应database/documents_suggestion.py的class类DocumentsSuggestion
    + document_reply 学院回复学生建议的情况
        + 对应database/document_reply.py的class类DocumentReply
    + member_user 用户信息
        + 对应database/member_user.py的class类MemberUser
        
* 所有以上表格class都继承基础表格抽象类BaseTable
    + 抽象类应具有:
        + attributes includes
            1. 字段信息(字段名称·字段类型)
            2. 主键约束
            3. 外键约束
        + functions includes
            1. 表格的建立
            2. 表格的增·删·改·查


# 后端API明细:
##    1. 访问地址:https://IPV4:PORT/activity_details/
##    2. https://IPV4:PORT/member_user/
##    3. https://IPV4:PORT/activity_student/
# 以上API address适用于以下子路由：
>>> 注释 : API address => ~ 
### 增
```
a. API address: ~/insert
访问该API的attributes:支持ajax(get与post)方法
input:
    请求表单是一行待插入记录的字典:{'列名1':'值','列名2':'值'...}
    成功的情况:
      1.所有的NOT NULL 属性列名均给出且给出的所有属性对应的属性值合法 =>return "success"
    失败的情况:
      1.不包含表单或表单为空=>没有传递插入数据，插入失败=>return "failure"
      2.表单中未包含所有NOT NULL 属性=>return "failure"
      3.表单中未包含的属性非法（不符合数据库标准）=>return "failure"
output: "failure" /  "success"
```

### 删
```
b. API address: ~/delete
访问该API的attributes:支持ajax(get与post)方法
input:
      成功的情况:
      1.请求表单中包含condition 属性&condition属性值合法=>删除activity_details表中满足condition的数据 =>return "success"
      失败的情况:
      1.请求表单中不包含condition 属性 或 不提供表单=>return "failure"
      2.请求表单的condition属性值非法=>return "failure"
      
output:"failure" /  "success"
```

### 改
```
c. API address: ~/update
访问该API的attributes:支持ajax(get与post)方法
input:
      成功的情况:
      1.请求表单中包含必要字段action,可选字段condition(默认更新所有rows),且属性值合法=>return "success"
      失败的情况:
      1.不满足上面成功条件则失败=>return "failure"
output:"failure" /  "success"
```

### 查
```
d. API address: ~/select
访问该API的attributes:支持ajax(get与post)方法
input:
      成功的情况:
      1.请求表单中包含合法的 condition 属性=>返回activity_details表中满足condition的数据
      2.请求表单中不包含condition 属性 或 不提供表单=>返回整张表数据
      失败的情况:
      1.请求表单中 condition 属性非法
output:"failure" /  返回的结果
```