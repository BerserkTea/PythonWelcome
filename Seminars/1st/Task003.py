#Вывести на экран числа от -N до N
print('Введите N')
N = int(input())
count = -N
while count<=N:
    print('{0}'.format(count))
    count=count+1
    