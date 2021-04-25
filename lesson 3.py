#Перебор списка
cities = ["Иваново", "Ярославль", "Кострома", "Нижний Новгород"]
citiesStr = ""
for city in cities:
    citiesStr += city
    if(cities.index(city) != len(cities) - 1):
        citiesStr += ", "
print(citiesStr)
#Свойтсва и методы списков
#Добавление элемента в список
newCity = "Москва"
cities.append(newCity)
print(cities)
#Добавление элемента на определенное место в списке 
cities.insert(1, "Астрахань")
print(cities)
#Задача викторина
q = []
a = []
count = int(input("Введите количество вопрос\n>> "))
score = 0
for i in range(count):
    q.append(input("Введите вопрос\n>> "))
    a.append(input("Введите ответ\n>> "))
for i in range(count):
    if(input(q[i]) == a[i]):
        score += 1
print("Вы ответили на ", score/count * 100, "% вопросов")