class Calc:
    numbers = []
    symbols = ("+", "-", "*", "/")
    def __init__(self, string):
        actions = {"+" : self.addition, "-" : self.subtraction, "*" : self.multiplication, "/" : self.division} 
        number = ""
        for i in range(len(string)):
            sub = string[i]
            if(sub in self.symbols):
                self.numbers.append(int(number))
                number = ""
                if(sub == "+"):
                    self.action = "+"
                elif(sub == "-"):
                    self.action = "-"
                elif(sub == "*"):
                    self.action = "*"
                elif(sub == "/"):
                    self.action = "/"
            elif(sub == " "):
                continue
            elif(type(int(sub)) == int):
                number += sub
                if(i == len(string) - 1):
                    self.numbers.append(int(number))
                    number = ""
        print(actions[self.action]())
        # print(self.action)
        # print(actions[self.action]())
    def addition(self):
        summ = 0
        for number in self.numbers:
            summ += number
        return summ
    def subtraction(self):
        substr = self.numbers[0]
        i = 1
        while i < len(self.numbers):
            substr -= self.numbers[i]
            i += 1
        return substr
    def multiplication(self):
        result = 1
        for number in self.numbers:
            result *= number
        return result
    def division(self):
        result = self.numbers[0]
        i = 1
        while i < len(self.numbers):
            result /= self.numbers[i]
            i += 1
        return result
text = input("Введите пример\n>> ")
calc = Calc(text)