# При заданном целом числе n посчитайте n + nn + nnn
n = (input('введите n: '))
#print(f'{n} + {n}{n} + {n}{n}{n} = {n + n**2 + n**3}')
nn = n + n 
nnn = n + n + n
sum = int(n) + int(nn) + int(nnn)
print(sum)