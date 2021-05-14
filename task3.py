import math
def rect(a, b):
    return a*b

def triangle(a, b):
    return rect(a, b)/2

def square(r):
    return math.pi*r**2

def length(r):
    return 2*math.pi*r

def sector(r, degrees):
    return square(r)/360*degrees
# a = int(input("Введите сторону a\n>> "))
# b = int(input("Введите сторону b\n>> "))
# print("Площадь прямоугольника с данными сторонами = " + str(rect(a, b)))
# print("Площадь прямоугольного треугольника с данными сторонами = " + str(triangle(a, b)))
r = int(input("Введите радиус окружности\n>> "))
degrees = int(input("Введите количество градусов сектора\n>> "))
print(square(r))
print(length(r))
print(sector(r, degrees))