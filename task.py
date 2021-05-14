copybook = 0.2
stack    = 3.7
box      = 70
print("Стоимость одной тетради = " + str(copybook) + "$")
print("Стоимость одной пачки (20 тетрадей) = " + str(stack) + "$")
print("Выгода при покупке пачки = " + str(round(copybook*20 - stack, 1)) + "$")
print("Стоимость одной коробки (20 пачек) = " + str(box) + "$")
print("Выгода при покупке коробки = " + str(stack*20 - box) + "$")
needs = int(input("Сколько вы хотите купить тетрадей?\n>> "))
if(needs >= 400):
    boxes = int(needs/400)
    stacks = int((needs - boxes*400)/20)
    copybooks = int(needs - boxes*400 - stacks*20)
    print("Выгоднее всего купить: коробки - " + str(boxes) + ", пачки - " + str(stacks) + ", тетради - " + str(copybooks))
    print("Это будет стоить " + str(box*boxes + stacks*stack + copybooks*copybook) + "$")
    print("Вы сэкономите " + str(copybook*needs - (box*boxes + stacks*stack + copybooks*copybook)) + "$")
elif(needs >= 20 and needs < 400):
    stacks = int(needs/20)
    copybooks = int(needs%20)
    print("Выгоднее всего купить: пачки - " + str(stacks) + ", тетради - " + str(copybooks))
    print("Это будет стоить " + str(stacks*stack + copybooks*copybook) + "$")
    print("Вы сэкономите " + str(copybook*needs - (stacks*stack + copybooks*copybook)) + "$")
else:
    print("Тетради обойдутся вам в " + str(needs*copybook) + "$")