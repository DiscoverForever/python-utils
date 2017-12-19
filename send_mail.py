#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import smtplib
from email.mime.text import MIMEText
from email.header import Header
options = {
    "sender": {
        "address": "sender@example.com",
        "password": "abcedfgfsdfsdf"
    },
    "receiver_address": ["receiver@example.com"]
}
msg = MIMEText("hello python", "plain", "utf-8")
msg["from"] = Header("tangyy", "utf-8")
msg["to"] = Header("tangyy", "utf-8")
msg["subject"] = Header("python邮件测试", "utf-8")

try:
    smtopObj = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
    smtopObj.login(options["sender"]["address"], options["sender"]["password"])
    smtopObj.sendmail(options["sender"]["address"],
                      options["receiver_address"], msg.as_string())

    print "邮件发送成功"
except smtplib.SMTPException:
    print "Error: 无法发送邮件"
except:
    print("Unexpected error:", sys.exc_info()[0])
