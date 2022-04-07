# 31.Составить список простых множителей натурального числа N
from math import factorial


N = int(input('Введите N '))

def Factor(n):
    Ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            Ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        Ans.append(n)
    return Ans
print(Factor(N))


# def IsPrime(n):
#     d = 2
#     while n % d != 0:
#         d += 1
#     return d == n

# n = int(input("Введите натуральное число: "))
# def factorization(n):
#     factors = list()
#     divisor = 2
#     while(divisor <= n):
#         if (n % divisor) == 0:
#             factors.append(divisor)
#             n = n/divisor
#         else:
#             divisor += 1
#     return factors
# print(factorization(n))
