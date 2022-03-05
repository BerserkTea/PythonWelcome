#Сообщить в какой четверти координатной 
# плоскости или на какой оси находится 
# точка с координатами Х и У 

coordinateX = int(input('Введите координату х '))
coordinateY = int(input('Введите координату y '))

if coordinateX > 0 and coordinateY>0:
    print("Точка находится в 1 четверти")
if coordinateX < 0 and coordinateY>0:
    print("Точка находится в 2 четверти")
if coordinateX < 0 and coordinateY<0:
    print("Точка находится в 3 четверти")
if coordinateX > 0 and coordinateY<0:
    print("Точка находится в 4 четверти")
if coordinateX == 0 and coordinateY!=0:
    print("Точка находится на оси y")
if coordinateX != 0 and coordinateY==0:
    print("Точка находится на оси x")
if coordinateX == 0 and coordinateY==0:
    print("Точка в начале координат")