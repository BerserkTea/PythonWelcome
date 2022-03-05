# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
def checkPredikatbool (x,y,z):
    if not (x or y or z) == (not x) and (not y) and (not z):
        print('True')
        return True
    else:
        print('False')
        return False 

if (checkPredikatbool(True,True,True) and checkPredikatbool(False,False,False) and checkPredikatbool(True,False,False) and checkPredikatbool(True,True,False) and checkPredikatbool(True,False,True) and checkPredikatbool(False,True,True) and checkPredikatbool(False,True,False) and checkPredikatbool(False,False,True)):
    print ('Horosho')
else:
    print('Nehorosho')