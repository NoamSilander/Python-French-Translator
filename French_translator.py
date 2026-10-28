from deep_translator import GoogleTranslator


translator = GoogleTranslator(source='en', target='fr')

user_input = input('What word do you want in French?: ').lower()

while True:
    try:
        print('-' * 5)
        print(translator.translate(user_input))
        print('-' * 5)
        user_input = input('What word do you want in French?: ').lower()
        
    except Exception as error:
        print('error:', error)
        user_input = input('That is not a part of the dictionary! Try again: ').lower()