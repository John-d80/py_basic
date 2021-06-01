"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

# словарь соответствия {'Eng': 'Рус'}
replace_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('4_task.txt', 'r', encoding='utf-8') as input_file:  # открываем на чтение входной файл
    with open('4_out_task.txt', 'w', encoding='utf-8') as out_file:  # открываем на запись выходной файл
        for line in input_file:  # для каждой строки из входного файла
            # ищем слово среди ключей словаря
            word_to_replace = [w for w in line.split() if w in replace_dict.keys()][0]
            out_file.write(line.replace(word_to_replace, replace_dict[word_to_replace]))  # замена
