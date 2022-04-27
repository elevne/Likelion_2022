# import random

# lunch = ['된장찌개','피자','제육볶음','짜장면']

# while True:
#     item = input('음식을 추가해주세요: ')
#     if item == 'q':
#         break
#     else:
#         lunch.append(item)

# print(lunch)
# set_lunch = set(lunch)

set_dinner = set(["된장찌개", "피자", "제육볶음", "짜장면"])
food = "짜장면"
set_dinner = set_dinner - set([food])
print(set_dinner)