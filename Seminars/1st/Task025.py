#25.  Написать программу преобразования десятичного числа в двоичное
n = int(input('введите число '))
b = ''
alert=bin(n)
print(alert)
while n > 0:
    b = str(n % 2) + b
    n = n // 2 
print(b)