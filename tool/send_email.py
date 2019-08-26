import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from setting.project_config import *


def send_email(report_file):
    global smtp
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = Header(subject, 'utf-8')
    # 组装Email头

    enclosure = MIMEText(open(report_file, 'rb').read(), 'base64', 'utf-8')
    enclosure["Content-Type"] = 'application/octet-stream'
    enclosure["Content-Disposition"] = 'attachment; filename="report.html"'
    msg.attach(enclosure)
    # 构造附件

    try:
        smtp = smtplib.SMTP_SSL(smtp_server)
        smtp.login(smtp_user, smtp_password)
        smtp.sendmail(sender, receiver, msg.as_string())
        logging.info("邮件发送完成")
    except Exception as e:
        logging.error(str(e))
    finally:
        smtp.quit()

