import time
class Human:
    grade = 0
    hunger = 50
    def __init__(self, name, secondName, age):
        self.name = name
        self.second = secondName
        self.age = age
    def say(self, word):
        return f'{self.name} говорит: {word}'
    def checkHunger(self):
        if(self.hunger <= 33):
            return f'{self.name} совсем голоден ({self.hunger}%)'
        elif(self.hunger <= 66):
            return f'{self.name} почти не голоден ({self.hunger}%)'
        else:
            return f'{self.name} сытый ({self.hunger}%)'
    def eat(self, food):
        self.hunger += food.energy
        return f'{self.name} съел {food.name}'

class Food:
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy

class Programmer(Human):
    def __init__(self, name, secondName, age, knowleges):
        super().__init__(name, secondName, age)
        self.knowleges = knowleges
        self.speed = knowleges*5
    def work(self, project):
        project.progress += self.speed
        return f'{self.name} работал над {project.name} и теперь проект приносит {project.progress} долларов'

class Businessman(Human):
    def __init__(self, name, secondName, age, money):
        super().__init__(name, secondName, age)
        self.money = money
    def pay(self, teacher, summ):
        if(summ > self.money):
            print(f'{self.name} не имеет столько денег')
            return False
        else:
            teacher.motivation += summ
            self.money -= summ
            return f'{self.name} заплатил {teacher.name} и теперь у него {self.money}$'

class Teacher(Human):
    motivation = 0
    def __init__(self, name, secondName, age, knowleges):
        super().__init__(name, secondName, age)
        self.knowleges = knowleges
    def teach(self, programmer, knowleges):
        if(self.motivation >= knowleges):
            programmer.knowleges += knowleges
            self.motivation -= knowleges
            return f'{self.name} обучил {programmer.name} и передал ему {knowleges} зн.'
        else:
            print(f'{self.name} не хочет учить. Ему нужны деньги')
            return False
    def learn(self, motivation):
        if(self.motivation >= motivation):
            self.knowleges += motivation
            self.motivation -= motivation
            return f'{self.name} получил знания по {motivation} технологий'
        else:
            print(f'{self.name} не хочет учиться. Ему нужны деньги')
            return False

class Project:
    progress = 0
    def __init__(self, name):
        self.name = name
    def profit(self, businessman):
        businessman.money += self.progress
        return f'{self.name} дал {businessman.name} {self.progress}$'

meat     = Food("мясо", 40)
cucumber = Food("огурец", 10)
snikers  = Food("сникерс", 20)

alex = Teacher("Саша", "Чернов", 20, 1000)
maks = Programmer("Максим", "Белов", 11, 100)
ilon = Businessman("Илон", "Маск", 49, 1000)

paypal = Project("PayPal")

while True:
    print(ilon.pay(alex, 100))
    print(alex.teach(maks, 50))
    print(alex.learn(50))
    print(maks.work(paypal))
    print(paypal.profit(ilon))
    time.sleep(1)