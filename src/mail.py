"""
Created on Tue Jan 10 17:23:18 2023

@author: sumedh joshi
"""

import smtplib
from email.message import EmailMessage

SENDER_EMAIL = "svm892073@gmail.com"
APP_PASSWORD = "xjpbqxdhiywmtuqp"


print("Mail Start")
msg = EmailMessage()
msg['Subject'] = "Suspicious Activity Detection"
msg['From'] = SENDER_EMAIL
msg['To'] = "aarush7276@gmail.com"
msg.set_content('Suspicious Activity Detected')

   


# with open('D:/bitmap/100%-Face Attendance with Excel Sheet/100%-Face Attendance with Excel Sheet/pandas_to_excel.xls', 'rb') as f:
#         file_data = f.read()
# msg.add_attachment(file_data, maintype="application", subtype="vnd.ms-excel", filename='D:/bitmap/100%-Face Attendance with Excel Sheet/100%-Face Attendance with Excel Sheet/pandas_to_excel.xls')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(SENDER_EMAIL, APP_PASSWORD)
        smtp.send_message(msg)
        print("Mail send successfully")
