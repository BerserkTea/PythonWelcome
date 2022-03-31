# 31.Составить список простых множителей натурального числа N
N = int(input('Введите N'))
x= N+1
some_list = []
for i in range(2, x):
    if N % i == 0:
        some_list.append(i)
        N = N/i
print(some_list)


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
