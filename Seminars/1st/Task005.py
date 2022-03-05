#Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30№
x = int(input("Введите число "))
if x % 5 == 0 and x % 10 == 0:
    print (f"Number {x} cratno 5 and 10")
elif x % 15 == 0 and x % 30 != 0:
    print(f"Number {x} cratno 15, but necratno 30")
else:
    print("Number doesnt much any usloviy")