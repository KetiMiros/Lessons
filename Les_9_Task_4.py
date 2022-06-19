# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты:
# speed, color, name, is_police(булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

from random import choice

class Car:
    """ Main car """
    direction = ["↑ north", " northeast ↗", "east →", "southeast ↘",
                 "south ↓", "southwest ↙", "west ←", "northwest ↖"]

    def __init__(self, n, c, s, p=False):
        self.name = n
        self.color = c
        self.speed = s
        self.is_police = p
        print(f'New car: {n} has a color: {c}.\nIs the car a police car? {p}')

    def go(self):
        print(f'{self.name}: Car went.')

    def stop(self):
        print(f'{self.name}: Car stopped!')


    def turn(self):
        print(f'{self.name}: Car turned {choice(self.direction)}.')


    def snow_speed(self):
        return f'{self.name}: Car speed: {self.name}'


class TownCar(Car):
    """City car"""

    def snow_speed(self):
        return f'{self.name}: Car speed: {self.speed}. Speeding!' if self.speed > 60 else super().snow_speed()

class WorkCar(Car):
    """Cargo truck"""

    def snow_speed(self):
        return f'{self.name}: Car speed: {self.name}. Speeding!' if self.speed > 40 else super().snow_speed()

class SportCar(Car):
    """Sport Car"""


class PoliceCar(Car):
    """Patrol Car"""


    def __init__(self, n, c, s, p=True):
        super().__init__(n, c, s, p)


police_car = PoliceCar('"Полиция"', 'белый', 80)
work_car = WorkCar('"Грузовичок"', 'зелёный', 40)
sport_car = SportCar('"Спорт"', 'красный', 120)
town_car = TownCar('"Малолитражка"', 'розовый', 65)

list_of_cars = [police_car, work_car, town_car, sport_car]

for i in list_of_cars:
    i.go()
    print(i.snow_speed())
    i.turn()
    i.stop()
    print()