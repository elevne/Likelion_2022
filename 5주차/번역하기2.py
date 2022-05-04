from googletrans import Translator

translator = Translator()


sentence = input('문장 입력: ')
lang = input('언어 입력: ')
detected = translator.detect(sentence)

# print(detected.lang)
result = translator.translate(sentence,lang)

print('--- 출력결과 ---')
print(detected.lang,':',sentence)
print(result.dest,':',result.text)
print('----------------')