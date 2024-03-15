print('Вы поедете на бал?')
word1 = input('Ответ: ')
if (not (word1 == 'да')) and (not (word1 == 'нет')) and (not (word1 == 'белое')) and (not (word1 == 'черное')):
    print('Верно')
else:
    print('Неверно')
