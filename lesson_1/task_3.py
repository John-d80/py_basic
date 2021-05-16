"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
"""
num = input('Введите число n от 1 до 9: ')
num_1 = int(num)
num_2 = int(num+num)
num_3 = int(num+num+num)
print('Сумма (n + nn + nnn) равна: ', num_1+num_2+num_3)
