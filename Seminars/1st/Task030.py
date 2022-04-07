# 30 Вычислить число Pi c заданной точностью d = 0.001

import math
def New_pi(d):
    if 0.1 >= d >= 10 ** -10:
        for_round = len(str(d))-2
        pi = math.pi
        new_pi = round(pi, for_round)
    else:
        new_pi = 'd не в заданном диапазоне'
    return new_pi

d = 0.001# int(input('введите коэффициент точности (от 10**-1 до 10**-10: '))
print(New_pi(d))
