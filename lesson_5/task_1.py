"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

import os

# удалим предыдущий файл, если существует
if os.path.exists('from_user.txt'):
    os.remove('from_user.txt')

# вспомогательные переменные
requests = ['о любви: ', 'о дружбе: ', 'о прекрасном: ', 'ещё: ']
not_enough = 1
request_num = 0

print('Давайте заполним файл. Оконание ввода - пустая строка.')
while not_enough:
    text_line = input('Введите что_нибудь ' + requests[request_num])
    request_num = request_num + 1 if request_num < 3 else 3
    if len(text_line) == 0:  # остановка по условию пустой строки
        not_enough = 0

    with open('from_user.txt', 'a') as f:  # допишем строку в конец файла
        f.write('\n'+text_line)
