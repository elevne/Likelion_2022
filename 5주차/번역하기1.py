from googletrans import Translator

translator = Translator()


sentence = input('언어 감지할 문장 입력: ')
# detected = translator.detect(sentence)

# print(detected.lang)

result = translator.translate(sentence,'en')
print(result)