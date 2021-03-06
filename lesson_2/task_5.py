"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
"""

ratings_lst = [7, 5, 3, 3, 2]
insert_flag = 0  # флаг, который показывает вставили рейтинг или нет

current_rating = int(input("Введите значение рейтинга: "))

# вариант для добавления в начало или в середину списка
for i in range(len(ratings_lst)):
    if current_rating > ratings_lst[i]:
        ratings_lst.insert(i, current_rating)
        insert_flag = 1
        break

# вариант для добавления в конец списка
if insert_flag == 0:
    ratings_lst.append(current_rating)

print(f'{ratings_lst}')
