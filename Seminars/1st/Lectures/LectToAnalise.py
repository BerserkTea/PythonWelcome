spisok = list(map(int,'1 2 3 5 8 15 23 38'.split()))
print(type(spisok[0]))
def f(x):
    return x**2
list = [(i, f(i)) for i in spisok if i % 2 == 0]
print(type(list))
print(list)

# 

# data = '1 2 3 5 8 15 23 38'.split()

# res = map(int, data)
# res = filter(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x ** 2), res))
# print(res)