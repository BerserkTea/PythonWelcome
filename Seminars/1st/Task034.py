# Даны два файла в каждом из которых находится запись многочлена.
#  Сформировать файл содержащий сумму многочленов.
import os


path1 = "PythonWelcome/Seminars/1st/Task034_1.txt"
f1 = open(path1, 'r')
data1 = f1.read() + ' '
f1.close

with open('PythonWelcome/Seminars/1st/Task034_2.txt', 'r') as file2:
    data2 = file2.read()
    # data2 = file2.readlines()
    # print(type(data2))
    # print(type(data2[0]))

data3 = open("PythonWelcome/Seminars/1st/Task034_3.txt", 'w')
data3.writelines(f"{data1} + ")
data3.writelines(f"{data2}")
data3.close
# print( os.getcwd())