"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
 имя, фамилия, год рождения, город проживания, email, телефон.
 Функция должна принимать параметры как именованные аргументы.
 Реализовать вывод данных о пользователе одной строкой.
"""


# функция, собирающая данные о человеке; именованная переменная descriptions - список, содержит все поля
def person_descriptions(descriptions):

    person_dictionary = {}  # инициализируем словарь с данными

    print('Проверки корректности ввода отключена. Пожалуйста, будьте внимательны.')

    for el in descriptions:
        person_dictionary[el] = input(f'Введите {el}: ')

    return person_dictionary


# функция печатает данные человека
def print_person(person_dict):
    print('\nЧеловек такой-то:')
    for k in person_dict.keys():
        print(f'{k}: {person_dict[k]}')


# элементы структуры данных ло человеке
descriptions = ('Имя', 'Фамилия', 'год рождения', 'город проживания', 'email', 'телефон')

# заполняем данные
person_dict = person_descriptions(descriptions)

# печатаем данные
print_person(person_dict)
