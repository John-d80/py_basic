"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и
передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя и спользовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""


class Warehouse:
    """
    Структура, описывающая единицу оргтехники на складе:
    {
        "eq_type": "",
        {
            "eq_name": "",
            {
                "eq_model": "",
                {
                    "quantity": 0
                }
            }
        }
    }
    """

    equipment_unit = {}

    @classmethod  # метод - положить на склад
    def warehouse_to(cls, unit_type, unit_name, unit_model, quantity):
        cls.equipment_unit[unit_type][unit_name][unit_model] += quantity

    @classmethod  # метод - забрать со склада
    def warehouse_from(cls, unit_type, unit_name, unit_model, quantity):
        quantity_cur = cls.equipment_unit[unit_type][unit_name][unit_model]['quantity']
        if quantity_cur < quantity:
            raise ValueError
        else:
            cls.equipment_unit[unit_type][unit_name][unit_model] -= quantity

    @staticmethod  # метод - посмотреть всё на складе
    def print_all_equipment():
        for k, v in Warehouse.equipment_unit.items():
            print(k, v)


class Equipment:
    def __init__(self, eq_type, eq_name, eq_model, quantity=0):
        self.eq_name = eq_name
        self.eq_type = eq_type
        self.eq_model = eq_model
        # добавим логику обработки количества оборудования
        try:
            if type(quantity) != int:
                self.quantity = 0
                print('Неверное количество')
            else:
                self.quantity = quantity
        finally:
            self.update_equipment_unit()

    def update_equipment_unit(self):  # метод - обновить еденицу техники (есть - суммируем кол-во, нет - вносим)
        equipment_unit = Warehouse.equipment_unit.get(self.eq_type, {})
        if self.eq_name in equipment_unit.keys():
            equipment_unit_name = equipment_unit[self.eq_name]
            if self.eq_model in equipment_unit_name.keys():
                equipment_unit_model = equipment_unit_name[self.eq_model]
                equipment_unit_model['quantity'] += self.quantity
            else:
                equipment_unit_name[self.eq_model] = {'quantity': self.quantity}

        else:
            equipment_unit[self.eq_model] = {self.eq_model: {'quantity': self.quantity}}

        Warehouse.equipment_unit[self.eq_type] = equipment_unit


class Scanner(Equipment):
    def __init__(self, eq_name, eq_model, quantity, year):
        super().__init__('Scanner', eq_name, eq_model, quantity)
        self.year = year


class Tablet(Equipment):
    def __init__(self, eq_name, eq_model, quantity, resolution):
        super().__init__('Tablet', eq_name, eq_model, quantity)
        self.resolution = resolution


scanner_1 = Scanner('HP', 'ml-1', 100, 2018)
scanner_2 = Scanner('HP', 'ml-1', 500, 2019)
scanner_3 = Scanner('HP', 'ml-2', 200, 2020)

tablet_1 = Tablet('Lenovo', 'x51', 888, '1024x768')
tablet_2 = Tablet('ASUS', 'x553', 111, '1024x768')

# посмотреть что есть на складе
Warehouse.print_all_equipment()
# добавить планшет
Warehouse.warehouse_to(unit_type='Tablet', unit_name='Lenovo', unit_model='x51', quantity=112)
# еще раз посмотреть
Warehouse.print_all_equipment()

# запутался со складом... -)
# ----- To.Do разобраться!
