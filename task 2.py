from faker import Faker
import random
fake = Faker("ru_RU")
students = {}
for i in range(10):
    name = fake.name()
    score = random.randint(0, 100)
    students[name] = score
names  = list(students.keys())
for i in range(len(names) - 1):
    f = 0
    for j in range(len(names) - 1 - f):
        if(students[names[j]] < students[names[j + 1]]):
            swap = students[names[j + 1]]
            students[names[j + 1]] = students[names[j]]
            students[names[j]] = swap
            f += 1
for student in students:
    print(student + " - " + str(students[student]))