"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


# функция считает сумму двух максимальных аргументов из трех
def sum_max_2(a, b, c):
    return sum([a, b, c]) - min([a, b, c])


# запросим 3 числа
numbers = input('Введите 3 числа через пробел: ').split()

# преобразуем в tuple из 3х чисел в качестве аргументов
args_3 = tuple(float(x) for x in numbers)

# печать результата
print(f'Сумма наибольших двух аргументов равна: {sum_max_2(*args_3)}')

