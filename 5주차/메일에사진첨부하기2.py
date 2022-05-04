import smtplib
from email.message import EmailMessage #MIME타입으로 변환하기
import imghdr #이미지 유형을 알려주는 모듈

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465

message = EmailMessage()
message.set_content("코드라이언 수업 짱짱")

#header부분에 들어가는 내용
message['subject'] = '이것은 제목입니다.'
message['from'] = 'wonilchoi25@gmail.com'
message['To'] = 'cwi5525@naver.com'

with open('insta.png','rb') as image: #open을 사용하여 image를 읽는다~~
    image_file = image.read()

image_type = imghdr.what('insta',image_file)
#print(image_type)
message.add_attachment(image_file, maintype='image', subtype=image_type)

smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
smtp.login('wonilchoi25@gmail.com','########')
smtp.send_message(message)
smtp.quit()