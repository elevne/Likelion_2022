from googletrans import Translator

translator = Translator()

# sentence = '안녕하세요. 최원일입니다.'
sentence = input('언어 감지할 문장 입력: ')
detected = translator.detect(sentence)

print(detected.lang)