class Animal:
    def __init__(self, name, age, color):
        self.name  = name
        self.age   = age
        self.color = color
        self.getInfo()
    def getInfo(self):
        print("Имя : " + self.name)
        print("Возраст : " + str(self.age))
        print("Цвет : " + self.color)

class Cat(Animal):
    def meow(self):
        print(self.name + " мяукнул(а)")

class Dog(Animal):
    def bark(self):
        print(self.name + " гавкнул(а)")

import time
murzik = Cat("Мурзик", 4, "Белый")
time.sleep(1)
sharik = Dog("Шарик", 2, "Черный")
time.sleep(1)
murzik.meow()
time.sleep(1)
sharik.bark()

from module import toDollars
print(toDollars(222))

print(time.strftime("%d-%m-%y %H:%M:%S"))

hello = "Привет, мир"
for s in hello:
    print(s)
    time.sleep(0.5)