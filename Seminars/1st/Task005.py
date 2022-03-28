#Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30№
# x = int(input("Введите число "))
# if x % 5 == 0 and x % 10 == 0:
#     print (f"Number {x} cratno 5 and 10")
# elif x % 15 == 0 and x % 30 != 0:
#     print(f"Number {x} cratno 15, but necratno 30")
# else:
#     print("Number doesnt much any usloviy")

def checkig_conditions(number):
    if (((number % 5 == 0 and number % 10 == 0) or number % 15 == 0) and number % 30 != 0):
        print('YES')
    else:
        print('NO')

num = int(input('enter a number to check: '))
checkig_conditions(num)