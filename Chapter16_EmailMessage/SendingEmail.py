#SENDING EMAIL
import smtplib #Nạp module smtplib
smtpObj = smtplib.SMTP('smtp.gmail.com', 587) #Tạo đối tượng smtp
#Hoặc dùng smtplib.SMTP_SSL() -> Port 465. Bỏ qua bước khởi chạy TLS.
"""
Gmail:	smtp.gmail.com
Outlook:	smtp-mail.outlook.com
Yahoo: smtp.mail.yahoo.com
"""
smtpObj.starttls() #Khởi chạy TLS
username = input('Username')
password = input('Password')
smtpObj.login(username, password)
content = 'Subject: <Subject>\n "Content"'
smtpObj.sendmail(email_sender, email_receiver, content) #Trả 1 về dictionary địa chỉ mail bị lỗi.
smtpObj.quit()
