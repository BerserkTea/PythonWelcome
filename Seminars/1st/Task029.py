# 29.Найти НОК двух чисел
def gcd(a,b):
    while(b>0):
        a,b=b,a%b
    return a
 
def lcm(x,y):
    return (x*y)//gcd(x,y)
 
a = int(input("Введите число a "))
b = int(input("Введите число b "))
print(lcm(a,b))