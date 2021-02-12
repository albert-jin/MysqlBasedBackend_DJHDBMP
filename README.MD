## 存在的问题以及注意点:
1 当移植到与前端代码同一环境下,不需要考虑访问途径,否则需要使用内网穿透ngrok,或者花钱租个阿里云服务器,或者学校能帮忙解决问题

2 前端需要熟练掌握访问后端的方法

3 数据表之间有依赖,不要试图破坏外键约束或者主键约束原则进行数据操作

## 后端启动步骤
1 确保安装完所有python依赖:flask,pymysql,flask_cors,etc

2 需要配置机器的mysql,账户名为"B",密码为"C",端口为"D"(默认3306)

3 打开MySql workbench,执行"CREATE DATABASE if not exists A default character set utf8;"语句 创建一个名为"A"的database

4 在第3步基础上python main.py --database A  --port D --name B --password C 即可开启后台服务