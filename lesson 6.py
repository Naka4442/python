class Cat:

    hungry = True
    hp     = 10
    dmg    = 1

    def __init__(self, color, age, name):
        self.color  = color
        self.age    = age
        self.name   = name

    def eat(self):
        self.hungry = False
        self.dmg += 1
        print("%s очень плотно покушал. Его сила увеличилась на 1 и теперь равна %s" % (self.name, self.dmg))

    def meow(self):
        return "Meow!"

    def changeName(self, name):
        self.name = name

    def sleep(self):
        self.hp += 5
        print("%s хорошо поспал. Его здоровье увеличилось на 5 и теперь равно %s" % (self.name, self.hp))

    def bite(self, target):
        if(self.hp > 0):
            target.hp -= self.dmg
            print("%s укусил %s" % (self.name, target.name))
            print("Теперь у %s %s здоровья" % (target.name, target.hp))
            if(target.hp <= 0):
                print("%s получил по башке и остался без здоровья. Ему нужно отдохнуть" % target.name)
        else:
            print("%s получил по башке и не может атаковать" % self.name)

barsik = Cat("Рыжий", 5, "Барсик")
puhlya = Cat("Черный", 2, "Пухля")

for i in range(10):
    barsik.eat()

barsik.bite(puhlya)
puhlya.bite(barsik)

puhlya.sleep()

for i in range(20):
    puhlya.eat()

puhlya.bite(barsik)