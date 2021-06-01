"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""

count_words_dict = {}

# открываем файл на чтение в кодировке UTF-8
with open('2_task.txt', 'r', encoding='utf-8') as input_file:
    for n, line in enumerate(input_file):
        # будем считать слова по количеству пробелов
        count_words_dict[n+1] = len(line.split())

print(f'Словарь {{номер строки: количество слов}}: \n{count_words_dict}')
