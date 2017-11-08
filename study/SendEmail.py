import smtplib
from email.header import Header
from email.mime.text import MIMEText


def sendEmail(username, password, receivers, subject, content):
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = Header(username)
    message['To'] = Header(receivers, 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect('smtp.sina.com', 25)
        smtpObj.login(username, password)
        smtpObj.sendmail(username, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException as error:
        print("Error: 无法发送邮件", format(error))


if __name__ == '__main__':
    username = input('请输入用户名:')
    password = input('请输入密码:')
    receiver = input('请输入收件人:')
    subject = input('请输入主题')
    content = input('请输入内容:')
    sendEmail(username,password,receiver,subject,content);
