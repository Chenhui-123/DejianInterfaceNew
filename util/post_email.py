# -*- coding: utf-8 -*-
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# 第三方 SMTP 服务
class PostEmail:
    def post_email(self, subject, content, file_path, file_name):

        mail_host = "smtp.163.com"  # SMTP服务器
        mail_user = "15010588693@163.com"  # 用户名
        mail_pass = "TYHYHPHEVJPZKWRF"  # 密码(这里的密码不是登录邮箱密码，而是授权码)

        sender = '15010588693@163.com'  # 发件人邮箱
        receivers = ['chenhui@zhangyue.com','zhangle@zhangyue.com']  # 接收人邮箱

        msgRoot = MIMEMultipart()
        msgRoot['Subject'] = subject
        msgRoot['From'] = sender
        if len(receivers) > 1:
            msgRoot['To'] = ','.join(receivers)  # 群发邮件
            part = MIMEText(content, _charset="utf-8")
            msgRoot.attach(part)
        else:
            msgRoot['To'] = receivers[0]
            part = MIMEText(content, _charset="utf-8")
            msgRoot.attach(part)

        # 添加附件部分
        path = file_path+file_name
        part = MIMEApplication(open(path, 'rb').read())
        part.add_header('Content-Disposition', 'attachment', filename=file_name)
        msgRoot.attach(part)

        s = smtplib.SMTP(mail_host, 25)
        try:
            s.login(sender, mail_pass)
            s.sendmail(sender, receivers, msgRoot.as_string())
            print ("邮件发送成功")
        except smtplib.SMTPException as e:
            print("Error, 发送失败", e)
        finally:
            s.quit()


postEmail=PostEmail()
if __name__=='__main__':
    postEmail=PostEmail()
    postEmail.post_email("发送附件测试", "python 邮件")
