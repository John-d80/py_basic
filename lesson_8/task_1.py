"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def to_date(cls, date_str):  # Извлекаем число, месяц, год. Преобразуем к int
        day_num, month_num, year_num = [int(x) for x in date_str.split('-')]
        return day_num, month_num, year_num

    @staticmethod
    def validation(date_str):  # Проверяем валидность по диапазону
        error_code = 0
        try:
            day_num, month_num, year_num = [int(x) for x in date_str.split('-')]
            if day_num not in range(1, 32):
                print('Неверно ввели день')
                error_code += 1
            if month_num not in range(1, 13):
                print('Неверно ввели месяц')
                error_code += 1
            if year_num < 1:
                print('Неверно ввели год')
                error_code += 1

            if error_code == 0:
                return 1

        except ValueError:
            print('Неверно ввели дату - не кодируется в int')


# validation_0
d_0 = '99-tt-1980'
if Date.validation(d_0):
    day_, month_, year_ = Date.to_date(d_0)
    print(f'День: {day_}, Месяц: {month_}, Год: {year_}')

# validation_1
d_1 = '99-02-1980'
if Date.validation(d_1):
    day_, month_, year_ = Date.to_date(d_1)
    print(f'День: {day_}, Месяц: {month_}, Год: {year_}')

# validation_2
d_2 = '01-88-1980'
if Date.validation(d_2):
    day_, month_, year_ = Date.to_date(d_2)
    print(f'День: {day_}, Месяц: {month_}, Год: {year_}')

# validation_3
d_3 = '01-01-1980'
if Date.validation(d_3):
    day_, month_, year_ = Date.to_date(d_3)
    print(f'День: {day_}, Месяц: {month_}, Год: {year_}')
