# Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.
N = int(input('Введите N'))
numbers = list(range(0, N))
print(numbers)
for i in numbers:
    numbers[i] = 3**i
    if i%2!=0:
        numbers[i] *= -1

print(numbers)


numbers2 = [3**i for i in range (0,N)]
print(numbers2)