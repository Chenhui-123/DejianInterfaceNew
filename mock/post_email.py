#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText

# 第三方 SMTP 服务
class PostEmail:
    def post_email(self):

        mail_host = "smtp.163.com"  # SMTP服务器
        mail_user = "15010588693@163.com"  # 用户名
        mail_pass = "TYHYHPHEVJPZKWRF"  # 密码(这里的密码不是登录邮箱密码，而是授权码)

        sender = '15010588693@163.com'  # 发件人邮箱
        receivers = ['chenhui@zhangyue.com']  # 接收人邮箱


        content = '接口测试完成，请查收测试报告'
        title = '接口测试邮件'  # 邮件主题
        message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
        message['From'] = "{}".format(sender)
        message['To'] = ",".join(receivers)
        message['Subject'] = title

        try:
            # smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
            smtpObj = smtplib.SMTP(mail_host, 25)
            smtpObj.login(mail_user, mail_pass)  # 登录验证
            smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
            print("mail has been send successfully.")
        except smtplib.SMTPException as e:
            print(e)

postEmail=PostEmail()
if __name__=='__main__':
    postEmail=PostEmail()
    postEmail.post_email()
