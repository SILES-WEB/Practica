# Сохраним список участников в переменной
li = [
    {'ФИО': 'Алексей Иванович Боярышников', 'баллы': 100},
    {'ФИО': 'Иван Александрович Малых ', 'баллы': 20},
    {'ФИО': 'Петр Борисович Третьяков ', 'баллы': 40},
    
]
# Выводим список на экран
print('Участники соревнований:')
for elem in li:
    print(elem['ФИО'], ' - ', elem['баллы'])
# Выводим тройку победителей на экран
winner_list = sorted(li, key=lambda x: x['баллы'], reverse=True)[:3]
print('\nТройка победителей:')
for elem in winner_list:
    print(elem['ФИО'], ' - ', elem['баллы'])