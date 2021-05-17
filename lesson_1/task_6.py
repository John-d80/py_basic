"""
6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
"""

initial_distance = input('Сколько спортсмен пробежал в первый день? Введите значение в км: ')
initial_distance = float(initial_distance)
desired_distance = input('Сколько спортсмен должен пробежать, чтобы победить? Введите значение в км: ')
desired_distance = float(desired_distance)

current_distance = initial_distance
result_day = 1

if desired_distance < initial_distance:
    print('Больше бегать не нужно')
else:
    while current_distance < desired_distance:
        current_distance *= 1.1
        result_day += 1

    print(f'Номер дня: {result_day}')
