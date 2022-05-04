import smtplib

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465

smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
smtp.login('wonilchoi25@gmail.com','########')
smtp.send_message()

smtp.quit()