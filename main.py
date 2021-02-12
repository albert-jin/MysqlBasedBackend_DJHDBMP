from pymysql import connect
from flask import jsonify,Flask,request
from flask_cors import CORS
from database import *  # 导入了6张表的class,基于表类进行后台功能的开发
import warnings

app =Flask(import_name=__name__)
CORS(app,supports_credentials =True)
database = connect(host='127.0.0.1', database='db_djhdbmpt', user='root', password='QA199839199839qa', port=3306)
cursor = database.cursor()
''' 基于activity_details表的所有数据库操作API:'''
activityDetailsInst =ActivityDetails(db=database,cursor=cursor)
########################################
@app.route(rule='/activity_details/insert',methods =['GET','POST'])
def activityDetailsInstInsert():
    '''
    通过ajax传参,一个前端的对象(python字典)包含要插入的列名:属性值
    :return:"failure" /  "success"

    '''
    try:
        if request.method =='GET':
            rowValues_dict =request.args.to_dict()
        else:
            rowValues_dict =request.form.to_dict()
        if not rowValues_dict:
            raise Exception('row_info not found when query API:/activity_details/insert!')
        if activityDetailsInst.insertDataWrap(ori_row_info=rowValues_dict):
            return  jsonify('success')
        return jsonify('failure')
    except Exception as e:
        warnings.warn(message=e.args)
        return jsonify('failure')


@app.route(rule='/activity_details/delete',methods =['GET','POST'])
def activityDetailsInstDelete():
    '''
    通过ajax传参,删除给定condition(必需)的rows
    :return: "failure" /  "success"

    '''
    try:
        if request.method =='GET':
             condition=request.args.get('condition') or ''
        else:
             condition=request.form.get('condition') or ''
        if not condition:
            raise Exception('don`t give delete condition when request API:/activity_details/delete!')
        if activityDetailsInst.deleteData(condition=condition):
            return  jsonify('success')
        return jsonify('failure')
    except Exception as e:
        warnings.warn(message=e.args)
        return jsonify('failure')

@app.route(rule='/activity_details/update',methods =['GET','POST'])
def activityDetailsInstUpdate():
    '''
    通过ajax传参,对满足(condition可选)条件的row进行(action必需)的更新动作
    :return: "failure" /  "success"

    '''
    try:
        if request.method =='GET':
            condition=request.args.get('condition') or ''
            action=request.args.get('action') or ''
        else:
            action = request.form.get('action') or ''
            condition=request.form.get('condition') or ''
        if not condition:
            raise Exception('don`t give delete condition when request API:/activity_details/delete!')
        if activityDetailsInst.updateData(action=action,condition=condition):
            return  jsonify('success')
        return jsonify('failure')
    except Exception as e:
        warnings.warn(message=e.args)
        return jsonify('failure')


@app.route(rule='/activity_details/select', methods=['GET', 'POST'])
def activityDetailsInstSelect():
    '''
    通过ajax传参,一个前端的对象(python的字典),返回指定查询条件(condition可选)的数据（不指定condition则返回整张表所有row）
    :return: "failure" /  返回的结果

    '''
    if request.method == 'GET':
        select_condition = request.args.get('condition') or ''
    else:
        select_condition = request.form.get('condition') or ''
    results = activityDetailsInst.selectData(condition=select_condition)
    return jsonify(results)
########################################

''' 基于member_user表的所有数据库操作API:'''
memberUserInst =MemberUser(db=database,cursor=cursor)
########################################
@app.route(rule='/member_user/insert',methods =['GET','POST'])
def memberUserInstInsert():
    '''
    通过ajax传参,一个前端的对象(python字典)包含要插入的列名:属性值
    :return:"failure" /  "success"

    '''
    try:
        if request.method =='GET':
            rowValues_dict =request.args.to_dict()
        else:
            rowValues_dict =request.form.to_dict()
        if not rowValues_dict:
            raise Exception('row_info not found when query API:/member_user/insert!')
        if memberUserInst.insertDataWrap(ori_row_info=rowValues_dict):
            return  jsonify('success')
        return jsonify('failure')
    except Exception as e:
        warnings.warn(message=e.args)
        return jsonify('failure')


@app.route(rule='/member_user/delete',methods =['GET','POST'])
def memberUserInstDelete():
    '''
    通过ajax传参,删除给定condition(必需)的rows
    :return: "failure" /  "success"

    '''
    try:
        if request.method =='GET':
             condition=request.args.get('condition') or ''
        else:
             condition=request.form.get('condition') or ''
        if not condition:
            raise Exception('don`t give delete condition when request API:/member_user/delete!')
        if memberUserInst.deleteData(condition=condition):
            return  jsonify('success')
        return jsonify('failure')
    except Exception as e:
        warnings.warn(message=e.args)
        return jsonify('failure')

@app.route(rule='/member_user/update',methods =['GET','POST'])
def memberUserInstUpdate():
    '''
    通过ajax传参,对满足(condition可选)条件的row进行(action必需)的更新动作
    :return: "failure" /  "success"

    '''
    try:
        if request.method =='GET':
            condition=request.args.get('condition') or ''
            action=request.args.get('action') or ''
        else:
            action = request.form.get('action') or ''
            condition=request.form.get('condition') or ''
        if not condition:
            raise Exception('don`t give delete condition when request API:/member_user/delete!')
        if memberUserInst.updateData(action=action,condition=condition):
            return  jsonify('success')
        return jsonify('failure')
    except Exception as e:
        warnings.warn(message=e.args)
        return jsonify('failure')


@app.route(rule='/member_user/select', methods=['GET', 'POST'])
def memberUserInstSelect():
    '''
    通过ajax传参,一个前端的对象(python的字典),返回指定查询条件(condition可选)的数据（不指定condition则返回整张表所有row）
    :return: "failure" /  返回的结果

    '''
    if request.method == 'GET':
        select_condition = request.args.get('condition') or ''
    else:
        select_condition = request.form.get('condition') or ''
    results = memberUserInst.selectData(condition=select_condition)
    return jsonify(results)

########################################

''' 基于activity_student表的所有数据库操作API:'''
activityStudentsInst =ActivityStudents(db=database,cursor=cursor)
########################################
@app.route(rule='/activity_student/insert',methods =['GET','POST'])
def activityStudentsInstInsert():
    '''
    通过ajax传参,一个前端的对象(python字典)包含要插入的列名:属性值
    :return:"failure" /  "success"

    '''
    try:
        if request.method =='GET':
            rowValues_dict =request.args.to_dict()
        else:
            rowValues_dict =request.form.to_dict()
        if not rowValues_dict:
            raise Exception('row_info not found when query API:/activity_student/insert!')
        if activityStudentsInst.insertDataWrap(ori_row_info=rowValues_dict):
            return  jsonify('success')
        return jsonify('failure')
    except Exception as e:
        warnings.warn(message=e.args)
        return jsonify('failure')


@app.route(rule='/activity_student/delete',methods =['GET','POST'])
def activityStudentsInstDelete():
    '''
    通过ajax传参,删除给定condition(必需)的rows
    :return: "failure" /  "success"

    '''
    try:
        if request.method =='GET':
             condition=request.args.get('condition') or ''
        else:
             condition=request.form.get('condition') or ''
        if not condition:
            raise Exception('don`t give delete condition when request API:/activity_student/delete!')
        if activityStudentsInst.deleteData(condition=condition):
            return  jsonify('success')
        return jsonify('failure')
    except Exception as e:
        warnings.warn(message=e.args)
        return jsonify('failure')

@app.route(rule='/activity_student/update',methods =['GET','POST'])
def activityStudentsInstUpdate():
    '''
    通过ajax传参,对满足(condition可选)条件的row进行(action必需)的更新动作
    :return: "failure" /  "success"

    '''
    try:
        if request.method =='GET':
            condition=request.args.get('condition') or ''
            action=request.args.get('action') or ''
        else:
            action = request.form.get('action') or ''
            condition=request.form.get('condition') or ''
        if not condition:
            raise Exception('don`t give delete condition when request API:/activity_student/delete!')
        if activityStudentsInst.updateData(action=action,condition=condition):
            return  jsonify('success')
        return jsonify('failure')
    except Exception as e:
        warnings.warn(message=e.args)
        return jsonify('failure')


@app.route(rule='/activity_student/select', methods=['GET', 'POST'])
def activityStudentsInstSelect():
    '''
    通过ajax传参,一个前端的对象(python的字典),返回指定查询条件(condition可选)的数据（不指定condition则返回整张表所有row）
    :return: "failure" /  返回的结果

    '''
    if request.method == 'GET':
        select_condition = request.args.get('condition') or ''
    else:
        select_condition = request.form.get('condition') or ''
    results = activityStudentsInst.selectData(condition=select_condition)
    return jsonify(results)

########################################

if __name__ == '__main__':
    app.run(host='localhost',debug=True)
    # database.close()