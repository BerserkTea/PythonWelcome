# 17.Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число

N = int(input('Enter N '))
spisok = []
for i in range (-N,N+1,2):
    spisok.append(i)
print(spisok)
composition = 1
path = 'C:/Users/BerserkTea/Desktop/Python/PythonWelcome/Seminars/1st/fileTask017.txt'
data = open(path, 'r')
for line in data:
    temp = int(line)
    composition*=spisok[temp]
    # print(composition)
data.close
print (composition)