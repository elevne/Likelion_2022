import smtplib
from email.message import EmailMessage

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465

message = EmailMessage()
message.set_content("코드라이언 수업 짱짱")

smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
smtp.login('wonilchoi25@gmail.com','########')
smtp.send_message()
smtp.quit()