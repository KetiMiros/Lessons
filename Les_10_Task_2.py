# Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма(2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани.
# Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.

from abc import ABC, abstractmethod

class Clothes:
     def __init__(self, param):
            self.param = param

     result = 0

     @property
     @abstractmethod
     def consumption(self):
        pass

     def __add__(self, other):
        Clothes.result += self.consumption + other.consumption
        return Costume(0)

     def __str__(self):
        res = Clothes.result
        Clothes.result = 0
        return f"{res}"

class Coat(Clothes):
        @property
        def consumption(self):
            return round((self.param / 6.5) + 0.5)

class Costume(Clothes):
        @property
        def consumption(self):
            return round((2 * self.param + 0.3) / 100)


coat = Coat(50)
costume = Costume(170)
print(coat + costume)
