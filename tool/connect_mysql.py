from pymysql import connect

from setting.project_config import *


class ConnectMySQL(object):
    # 封装连接MySQL的方法

    @staticmethod
    def query_mysql(sql_sentence):
        # 查询数据库的方法

        db = connect(
            host=db_host,
            user=db_user,
            password=db_password,
            db=db_database,
            port=db_port,
            charset="utf8")
        # 打开数据库连接

        cur = db.cursor()
        # 使用cursor()方法获取操作游标
        cur.execute(sql_sentence)
        # 执行sql语句
        results = cur.fetchall()
        # 获取查询的结果

        cur.close()
        # 关闭游标
        db.close()
        # 断开数据库连接

        return results
        # 返回一个元组


