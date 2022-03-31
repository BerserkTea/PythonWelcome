# 28.Найти корни квадратного уравнения Ax² + Bx + C = 0
# Математикой
# Используя дополнительные библиотеки*
import math
 
print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
 
discr = b ** 2 - 4 * a * c
print("Дискриминант D = %.2f" % discr)
 
if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Корней нет")








# def CheckInt(X):
#     if (X % 1) == 0:
#         X = int(X)
#     else:
#         X = round(X, 2)
#     return X


# A, B, C = map(float, input("Введите через пробел коэффициенты для уравнения\nAx² + Bx + C = 0 \n").split())

# D = B**2 - 4*A*C  # Нахождение дискриминанта
# if D < 0:
#     YesOrNo = input("Вещественных и целочисленных корней нет! Вывести комплексные? Введите 'да' для вывода комплексных корней, 'нет' для завершения: ")
#     if YesOrNo == "да":
#         x1 = (-B + D**0.5)/(2*A)
#         x1 = complex(x1)
#         x2 = (-B - D**0.5)/(2*A)
#         x2 = complex(x2)
#         print(f"x1 = {x1}, x2 = {x2}")
#     # else:
#     #     exit()
# elif D == 0:
#     x = (-B)/(2*A)
#     x = CheckInt(x)
#     print(f'x1 = x2 = {x}')
# else:
#     x1 = (-B + D**0.5)/(2*A)
#     x1 = CheckInt(x1)
#     x2 = (-B - D**0.5)/(2*A)
#     x2 = CheckInt(x2)
#     print(f"x1 = {x1}, x2 = {x2}")
