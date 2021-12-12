# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
# переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

print("Задание 1")

import time
import datetime


class TrafficLight:
    __color = ""

    def __init__(self, color):
        self.__color = color

    def running(self):
        print(datetime.datetime.now(), self.__color)
        if self.__color == "red":
            time.sleep(7)
            self.__color = "yellow"
        elif self.__color == "yellow":
            time.sleep(2)
            self.__color = "green"
        elif self.__color == "green":
            time.sleep(5)
            self.__color = "red"
        else:
            print(datetime.datetime.now(), "Ошибка")


TL = TrafficLight("red")


TL.running()
TL.running()
TL.running()
TL.running()
TL.running()

# 2. Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина). Значения данных атрибутов должны
# передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.

print("Задание 2")

class Road:
    _length = 0
    _width = 0
    __massa = 25
    __tolsh = 5

    def __init__(self, l, w):
        self._length = l
        self._width = w

    def calc(self):
        return self._width * self._length * self.__massa * self.__tolsh / 1000


R = Road(5000, 20)
print(R.calc(), "тонн")


# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен
# быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

print("Задание 3")

class Worker:
    name = ""
    surname = ""
    position = ""
    _income = {"wage": 0, "bonus": 0}


class Position(Worker):
    def __init__(self, n, s, p, w, b):
        self.name = n
        self.surname = s
        self.position = p
        self._income["wage"] = w
        self._income["bonus"] = b

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


P = Position("Ivan", "Petrov", "Manager", 50, 20)
print(P.get_full_name())
print(P.get_total_income())


# 4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

print("Задание 4")

class Car:
    speed = 0
    color = 0
    name = ""
    is_police = False

    def __init__(self, s, c, n):
        self.speed = s
        self.color = c
        self.name = n

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}')

    def show_speed(self):
        print(f'Текушая скорость {self.name} составляет {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed <= 60:
            print(f'Текушая скорость {self.name} составляет {self.speed}')
        else:
            print("Превышение скорости")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed <= 40:
            print(f'Текушая скорость {self.name} составляет {self.speed}')
        else:
            print("Превышение скорости")


class PoliceCar(Car):
    def __init__(self, s, c, n):
        super().__init__(s, c, n)
        self.is_police = True


TC = TownCar(62, "red", "Town Car")
SC = SportCar(100, "red", "Sport Car")
WC = WorkCar(45, "grey", "Work Car")
PC = PoliceCar(70, "blue", "Police Car")

TC.go()
TC.turn("направо")
TC.stop()

TC.show_speed()
SC.show_speed()
WC.show_speed()
PC.show_speed()

# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

print("Задание 5")

class Stationery:
    title = ""

    def draw(self):
        print("Запуск отрисовки")

class Pen (Stationery):
    def draw(self):
        print("Запуск отрисовки для ручки")

class Pencil (Stationery):
    def draw(self):
        print("Запуск отрисовки для карандаша")

class Handle (Stationery):
    def draw(self):
        print("Запуск отрисовки для маркера")

P = Pen()
Pncl = Pencil()
H = Handle()

P.draw()
Pncl.draw()
H.draw()
