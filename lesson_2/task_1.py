"""
1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""

all_type_list = ['abra', 999, 666.777, {1: 'ca', 2: 'da', 3: 'bra'}, ('and', 'something', 'else'), ['QQQ', 'NYSE']]

for el in all_type_list:
    print(f'The type of element {[el]} is: {type(el)}')