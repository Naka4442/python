# numbers = []
# for i in range(10):
#     numbers.append(int(input("Введите число\n>> ")))
# summ = 0
# for number in numbers:
#     summ += number
# print("Среднее арифметическое чисел = " + str(summ/len(numbers)))
one   = [1, 2, 3, 4, 4, 5]
two   = (1, 2, 3, 4, 4, 5)
three = {1, 2, 3, 4, 4, 5}
four  = frozenset((1, 2, 3, 4, 4, 5))
# slovar = dict((("cat", "кот"), ("dog", "собака"), ("fox", "лиса")))
slovar = {
    "а" : "a",
    "б" : "b",
    "в" : "v",
    "г" : "g",
    "д" : "d",
    "е" : "e",
    "и" : "i",
    "н" : "n",
    "о" : "o",
    "п" : "p",
    "м" : "m",
    "р" : "r"
}

print(slovar)
string = input("Введите слово")
newString = ""
for s in string:
    if s in slovar.keys():
        newString += slovar[s]
    else:
        newString += s
print(newString)