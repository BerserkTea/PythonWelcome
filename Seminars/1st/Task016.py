# 16.Задать список из n чисел последовательности (1+1n)n и вывести на экран их сумму
spisok = []
N = int(input('Введите '))
for i in range(N):
    digit=(1+1*i)*i
    spisok.append(digit)
print(spisok)
print(sum(spisok))