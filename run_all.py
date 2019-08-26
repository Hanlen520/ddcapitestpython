from unittest import defaultTestLoader
from setting.project_config import *
from BeautifulReport import BeautifulReport
from tool.send_email import send_email


if __name__ == "__main__":
    test_suite = defaultTestLoader.discover(case_path, pattern='*test.py')
    result = BeautifulReport(test_suite)
    result.report(
        filename="report{}".format(today),
        # 测试报告文件名称, 如果不指定默认文件名为report.html
        description='YYY接口自动化测试报告',
        # 测试报告用例名称展示
        report_dir=report_path,
        # 测试报告文件写入路径
        theme='theme_default'
        # 测试报告主题样式
    )

    send_email(api_report_file)
    # 发送邮件

