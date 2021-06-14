"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class Complex:
    def __init__(self, r, im):
        self.r = r
        self.im = im

    def __add__(self, other):
        return Complex(self.r + other.r, self.im + other.im)

    def __mul__(self, other):
        return Complex(self.r * other.r - self.im * other.im,
                       self.r * other.im + self.im * other.r)

    def __str__(self):
        return f'{self.r} + {self.im}j'


c_num_1 = Complex(1, 2)
c_num_2 = Complex(-3, -1)

print(f'Сумма равна: {c_num_1 + c_num_2}')
print(f'Произведение равно: {c_num_1 * c_num_2}')