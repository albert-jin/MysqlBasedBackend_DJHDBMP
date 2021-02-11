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
        