# count = int(input("Сколько чисел вы хотите ввести?"))
# numbers = []
# for i in range(count):
#     numbers.append(int(input("Введите число >> ")))
# newNumbers = []
# for number in numbers:
#     if number > 5:
#         newNumbers.append(number)
# print(newNumbers)


letters = "пЛРФЫЩГЗФЩЦКрЗФЩЫТДФЛЫАиЗЩЫФЗвДЛВРАеЗЩФОЗЩАОАт"
clean = ""
for letter in letters:
    if not letter.isupper():
        clean += letter
print(clean)