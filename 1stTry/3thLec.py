# from importlib.resources import path


path = 'C:/Users/BerserkTea/Desktop/Python/PythonWelcome/1stTry/3thLec.txt'
f = open(path, 'r')
data = f.read() + ' '
f.close

numbers = []

while data != '':
    space_pos = data.index(' ')
    numbers.append(int(data[:space_pos]))
    data = data[space_pos+1:]
print(numbers)
res = map(int, numbers)
res = filter ( lambda x: not x%2, res)
res = list(map(lambda x: (x, x**2), res))
print(res)