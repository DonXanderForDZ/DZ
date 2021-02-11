"""
4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
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
        return f'{self.name} едет'

    def stop(self):
        return f'{self.name} остановилась'

    def turn(self, value):
        if value >= 360:
            value_gr = value % 360
        else:
            value_gr = value
        return f'{self.name} повернула на {value_gr} градусов по часовой стрелке'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'Скорость автомобиля {self.name} превышает 60 км\ч и составляет {self.speed} км\ч.'
        else:
            return f'Скорость автомобиля {self.name} составляет {self.speed} км\ч.'

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'Скорость автомобиля {self.name} превышает 40 км\ч и составляет {self.speed} км\ч.'
        else:
            return f'Скорость автомобиля {self.name} составляет {self.speed} км\ч.'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed < 40:
            return f'Для {self.name} {self.speed} км\ч - очень мало'
        else:
            return f'{self.name} едет {self.speed} км\ч5'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def shw_police(self):
        if self.is_police:
            return f'{self.name} полицейский автомобиль'
        else:
            return f'{self.name} не полицейский автомобиль'

belorus = WorkCar(20, 'синий', 'белорус', False)
kamaz = WorkCar(60, 'оранжевый', 'камаз', False)
bmw  = TownCar(100, 'черный', 'бумер', False)
mers = TownCar(50, 'белый', 'мерен', False)
shkoda = PoliceCar(150, 'бело-синий', 'мигалка', True)
lamba = SportCar(250, 'зеленый', 'ламба', False)
ferr = SportCar(33, 'крассный', 'ферри', False)

print(lamba.turn(int(input('Введите значение поворота автомобиля по часовой стрелке в градусах: '))))
print(bmw.show_speed())
print(shkoda.shw_police())
print(ferr.show_speed())
print(kamaz.show_speed())
print(mers.go())
print(mers.stop())



