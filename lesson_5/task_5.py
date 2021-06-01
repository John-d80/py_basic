"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

numbers_to_insert = [123, -485, 555.55, 28.27, 674, 18, 17, 16]

# запись в файл (перед записью преобразуем числа в str
with open('5_task.txt', 'w') as out_file:
    out_file.write(' '.join([str(x) for x in numbers_to_insert]))

# чтение из файла (преобразуем str в float
with open('5_task.txt', 'r') as input_file:
    numbers = [float(x) for x in input_file.read().split()]

# печат суммы
print(f'Сумма чисел равна: {sum(numbers)}')
