"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры
класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

    def get_income(self):
        return self._income


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return ' '.join([self.name, self.surname])

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


# экземпляр класса Position
person = Position('Вася', 'Пупкин', 'космонавт', {'wage': 500000, 'bonus': 1000000})
print(f'Имя работника: {person.get_full_name()}')  # метод класса Position
print(f'Должность: {person.position}')  # атрибут класса Worker
print(f'Оклад: {person.get_income()["wage"]}')  # доступ к защищенному атрибуту класса Worker
print(f'Бонус: {person.get_income()["bonus"]}')  # доступ к защищенному атрибуту класса Worker
print(f'Доход с учетом бонуса: {person.get_total_income()}')  # метод класса Position
