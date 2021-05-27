"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание,
что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.

Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""

from itertools import count
from itertools import cycle

# задание а)
number_from, number_to = (int(x) for x in \
                          input('Введите целое число для начала цикла, и для его завершения через пробел: ').split())
for el in count(number_from):
    if el > number_to:
        break
    else:
        print(el)


# задание б)
n_cycles = int(input('Введите количество повторений: '))
input_list = ['съешь', 'ещё', 'этих', 'французских', 'булок']
с = 0
for el in cycle(input_list):
    if с > n_cycles:
        break
    print(el)
    с += 1