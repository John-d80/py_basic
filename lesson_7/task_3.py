"""
3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
умножение и обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества
ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
*****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
*****\n*****\n*****.
"""


class Cell:
    # quantity - параметр, соответствующий кол-ву ячеек в клетке
    def __init__(self, quantity):
        self.quantity = quantity

    # переопределяем сложение
    def __add__(self, other):
        return self.quantity + other.quantity

    # переопределяем вычитание
    def __sub__(self, other):
        difference = self.quantity - other.quantity
        return difference if difference > 0 else 'Разность двух клеток не определена'

    # переопределяем умножение
    def __mul__(self, other):
        return self.quantity * other.quantity

    # переопределяем деление
    def __truediv__(self, other):
        return self.quantity // other.quantity

    # метод для формирования ряда
    def make_order(self, number):
        return '\\n'.join(['*' * i for i in [number] * (self.quantity // number)] +
                          ['*' * i for i in [self.quantity % number]])


# создаем 2 объекта класса Cell с количеством ячеек 20 и 22
c1 = Cell(20)
c2 = Cell(18)

# результаты
print(f'При сложении получается клетка с кол-вом ячеек: {c1 + c2}')
print(f'При вычитании получается клетка с кол-вом ячеек: {c1 - c2}')
print(f'При умножении получается клетка с кол-вом ячеек: {c1 * c2}')
print(f'При делении получается клетка с кол-вом ячеек: {c1 / c2}')

print(f'Организация ячеек по рядам: {c1.make_order(3)}')
