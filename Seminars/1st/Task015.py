# 15.Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]
n = []
N = int(input('Введите '))
for i in range(0,N):
    if i == 0:
        X = 1
        n.append(X)
    else:
        X=n[i-1]*(i+1)
        n.append(X)
      
print(n)



# spisok = range(N+1)
# for i in spisok:
#     if i>1:
#         i = spisok[i]*(i+1)
#     else:
#         pass
# print(spisok)