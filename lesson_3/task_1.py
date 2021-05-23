"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


# определяем функцию с позиционными аргументами
def division(a, b):
    return a / b


# вспомогательные перменные
not_success = True  # для цикла while
result = None  # сюда положим реультат

while not_success:
    try:
        input_str = input('Введите два числа a, b через пробел: ').split()
        a, b = (float(x) for x in input_str)  # переводим два числа в tuple
        result = division(a, b)
        not_success = 0  # если ошибок нет, выходим из цикла while
    except ValueError:
        print(f'Что-то не то ввели..., попробуйте еще раз')
    except ZeroDivisionError:
        print(f'Деление на ноль, попробуйте еще раз')

print(f'Частное a/b с точностью до 5 знака равно: {result:.5f}')
