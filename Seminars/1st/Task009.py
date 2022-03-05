#Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти

quarter = int(input('Введите номер четверти '))

if quarter == 1:
    print("X>0; Y>0")
elif quarter == 2:
    print("X<0; Y>0")
elif quarter == 3:
    print("X<0; Y<0")
elif quarter == 4:
    print("X>0; Y<0")
else:
    print("Insert correct number")

