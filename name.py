import random

user=int(input("Введите двухзначное целое число: "))
comp=random.randint(10,100)

while 10<=user<100:
    if user>comp:
        print("Вы -",user,"Комп -",comp,"ИТОГ:Победа")
    else:
        print("Вы -",user,"Комп -",comp,"ИТОГ:Проигрыш")
    break
else:
    print("Введите целое число!")
    user = int(input("Введите двухзначное целое число: "))