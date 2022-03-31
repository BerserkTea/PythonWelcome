# 29.Найти НОК двух чисел
# least common multiple наименьшее общее кратное
# greatest common divisor наибольший общий делитель
def gcd(a,b):
    if (b==0):
        return a
    else:
        return gcd(b,a%b)

    # while a!=0 and b!=0:
    #     if a>b:
    #         a = a%b
    #     else:
    #         b = b%a
    #     return (a+b)
 
def lcm(x,y):
    return (x*y)//gcd(x,y)
 
a = int(input("Введите число a "))
b = int(input("Введите число b "))
print(lcm(a,b))
print(gcd(a,b))

# 320