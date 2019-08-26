import logging
import os
import time


store_address = "http://www.mendian.com"
# 门店后台的地址
operate_address = "http://www.yunying.com"
# 运营后台的地址
time_stamp = int(time.time())
# 时间戳
universal_signature = "zxcvbnmasdfghjkl"
# 万能签名


db_host = '192.168.1.106'
db_port = 3306
db_user = 'root'
db_password = '123456'
db_database = ''
# MySQL数据库配置


current_path = os.path.dirname(os.path.dirname(__file__))
# 获取当前目录的父目录的绝对路径
# 也就是整个工程的根目录
case_path = os.path.join(current_path, "case")
# 测试用例的目录
excel_path = os.path.join(current_path, "resource")
# Excel文件的路径
today = time.strftime("%Y-%m-%d", time.localtime())
# 年月日
report_path = os.path.join(current_path, "report")
# 测试报告的路径
log_path = os.path.join(current_path, "log", "log{}.log".format(today))
# 日志的路径
api_report_file = os.path.join(report_path, "report{}.html".format(today))
# 测试报告

logging.basicConfig(
    level=logging.INFO,
    # 日志级别
    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
    # 日志格式
    datefmt='%Y-%m-%d %H:%M:%S',
    # 日期格式
    filename=log_path,
    # 日志输出文件
    filemode='a'
    # 追加模式
)
# log配置


smtp_server = 'smtp.qq.com'
smtp_user = '123456789@qq.com'
smtp_password = '123456'
sender = smtp_user
# 发件人
receiver = 'tester_team@yyy.com'
# 收件人
subject = 'YYY接口测试报告'
# 邮件主题

