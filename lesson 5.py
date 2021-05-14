def translit(text):
    slovar = {
        "а" : "a",
        "б" : "b",
        "в" : "v",
        "г" : "g",
        "е" : "e",
        "и" : "i",
        "п" : "p",
        "р" : "r",
        "о" : "o",
        "м" : "m",
        "н" : "n",
        "к" : "k",
        "л" : "l",
        "д" : "d", 
        "с" : "s",
        "т" : "t",
        "ю" : "u",
        "я" : "ya",
        "э" : "e",
        "ч" : "ch",
        "ш" : "sh",
        "ь" : "'",
        "й" : "y",
        "з" : "z",
        "у" : "u",
        "х" : "h",
        "ц" : "tc"
    }
    newText = ""
    for letter in text:
        if letter in slovar.keys():
            newText += slovar[letter]
        else:
            newText += letter
    return newText

def summ(a, b):
    return a + b

def pi():
    return 3.14

scores = [10, 9, 8, 7, 6, 5, 43, 26, 91, 167, 21, 0, -5]

def getMax(numbers):
    maximum = numbers[0]
    for i in range(len(numbers)):
        if(numbers[i] < maximum):
            maximum = numbers[i]
    return maximum

# print(getMax(scores))

import random
import timeit

numbers = []
for i in range(1000):
    numbers.append(random.randint(0, 10000000000000000))

# start = datetime.datetime.now()
end = 0
def bubbleSort(s):
    for i in range(len(s) - 1):
        f = 0
        for j in range(len(s) - 1 - f):
            if(s[j] > s[j + 1]):
                swap = s[j]
                s[j] = s[j + 1]
                s[j + 1] = swap
                f += 1
    # end = datetime.datetime.now()
    return s

def combsort(alist):
    alen = len(alist)
    gap = (alen * 10 // 13) if alen > 1 else 0
    while gap:
        if 8 < gap < 11:    ## variant "comb-11"
            gap = 11
        swapped = False
        for i in range(alen - gap):
            if alist[i + gap] < alist[i]:
                alist[i], alist[i + gap] = alist[i + gap], alist[i]
                swapped = True
        gap = (gap * 10 // 13) or swapped
    return alist

print(bubbleSort(numbers))
print(timeit.timeit("bubbleSort(numbers)", setup="from __main__ import bubbleSort, numbers", number=1))
print(combsort(numbers))
print(timeit.timeit("combsort(numbers)", setup="from __main__ import combsort, numbers", number=1))