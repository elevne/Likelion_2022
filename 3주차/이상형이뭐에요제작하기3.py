total_dic = {}

while True:
    question = input('질문을 입력해주세요: ')
    if question == 'q':
        break
    else:
        total_dic[question] = ""

for i in total_dic:
    print(i)
    answer = input('답변을 입력해주세요: ')
    total_dic[i] = answer
    
print(total_dic)