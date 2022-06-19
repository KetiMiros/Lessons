#Создать класс TrafficLight (светофор)
#определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);


# -----------------------------------------------------1вариант-----------------------------------------------------
from time import sleep


class TrafficLight:
    __color = "Чёрный"

    def running(self):
        while True:
            print("TrafficLight is red now")
            sleep(7)
            print("TrafficLight is yellow now")
            sleep(2)
            print("TrafficLight is green now")
            sleep(7)
            print("TrafficLight is yellow now")
            sleep(2)


trafficLight = TrafficLight()
trafficLight.running()


# -------------------------------------------------------2вариант---------------------------------------------------------

import time
import itertools


class TrafficLight:
    __color = [["red", [7, 31]], ["yellow", [2, 33]], ["green", [7, 32]], ["yellow", [2, 33]]]


    def running(self):
        for light in itertools.cycle(self.__color):
            print(f"\r\033[{light[1][1]}m\033[1m{light[0]}\033[0m", end="")
            time.sleep(light[1][0])


trafficLight_1 = TrafficLight()
trafficLight_1.running()
