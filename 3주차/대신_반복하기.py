import random
import time

for _ in range(30):
    print(random.choice(['된장찌개', '피자', '제육볶음','치킨','떡볶이','라면']))
    print('이 문장도 반복되나..?')
    time.sleep(1)

while True:
    print(random.choice(['된장찌개', '피자', '제육볶음','치킨','떡볶이','라면']))
    break
    print('이 문장도 반복되나..?')
    time.sleep(1)