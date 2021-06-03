"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar,
WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')

    def show_speed(self):
        print(f'Машина {self.name} едет со скоростью {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Машина {self.name} едет со скоростью {self.speed} км/ч')
        if self.speed > 60:
            print(f'!Превышение скорости!')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Машина {self.name} едет со скоростью {self.speed} км/ч')
        if self.speed > 40:
            print(f'!Превышение скорости!')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


t_car = TownCar(66, 'green', 'Peugeot')
s_car = SportCar(95, 'red', 'Tesla')
w_car = WorkCar(45, 'yellow', 'VW')
p_car = PoliceCar(85, 'white', 'Nissan')

print(f'Марка городской машины: {t_car.name}' )  # 1. атрибут name
print(f'Цвет городской машины: {t_car.color}' )  # 2. атрибут color
print(t_car.go())  # 3. метод go
print(w_car.show_speed())  # 4. метод show_speed
print(s_car.show_speed())  # 5. метод show_speed
print(t_car.show_speed())  # 6. метод show_speed
print(s_car.stop())  # 7. метод stop
print(s_car.turn('влево'))  # 8. метод turn
print(f'Машина {s_car.name} полицейская? - {s_car.is_police}')  # 9. атрибут is_police
print(f'Машина {p_car.name} полицейская? - {p_car.is_police}')  # 10. атрибут is_police
