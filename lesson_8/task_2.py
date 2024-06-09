"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно
обработать эту ситуацию и не завершиться с ошибкой.
"""


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_data = input("Введите два числа через пробел: ")

try:
    a, b = [int(x) for x in inp_data.split()]
    if b == 0:
        raise OwnError("Деление на ноль!")
except ValueError:
    print("Вы ввели не числа")
except OwnError as err:
    print(err)
else:
    print(f"All Ok. Частное: {a/b:0.5f}")
