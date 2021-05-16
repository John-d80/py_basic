"""
1. Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в переменные,
выведите на экран.
"""

# type - list
lst = [1, 11, 22, 333]
print('My first list: ', lst)

# type - dict
d = {1: 'd', 2: 'i', 3: 'c', 4: 't'}
print('My first dict: ', d)

# type - string
s = 'Повезло нам с преподавателем!'
print('My first string: %s' % s)

# interactive_1
nums = input('Введите 3 числа через пробел: ')
print('Вот они, угадал?: %s' % nums)

# interactive_2
nums_for_sqrt = input('Теперь возведем число в квадрат. Введите целое число: ')
nums_for_sqrt = int(nums_for_sqrt)
print('Итак, квадрат %s: %s' % (nums_for_sqrt, nums_for_sqrt**2))
