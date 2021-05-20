"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
"""

input_str = input('Введите строку из нескольких слов: ')

# уберем возможные пробелы в начале и в конце
# объединим множественные пробелы в один
input_str = " ".join(input_str.strip().split())

for n, w in enumerate(input_str.split()):
    print(f'{n+1}: {w[:10]}')