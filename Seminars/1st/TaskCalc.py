# Написать программу, которая выполняет над двумя вещественными числами одну из четырех арифметических операций (сложение, вычитание, умножение или деление). 
# Программа должна завершаться только по желанию пользователя.

print("Ноль в качестве знака операции"
      "\nзавершит работу программы")
while True:
    operation = input("Знак (+,-,*,/): ")
    if operation == '0':
        break