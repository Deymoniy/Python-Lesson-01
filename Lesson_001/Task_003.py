#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и 
#выдаёт номер четверти плоскости, 
#в которой находится эта точка (или на какой оси она находится).

x = int(input('Enter your X '))
y = int(input('Enter your Y '))
if x > 0 and y >0:
    print("It's in the 1st quarter")
elif x < 0 and y > 0:
    print("It's in the 2nd quarter")
elif x < 0 and y < 0:
    print("It's in the 3rd quarter")
elif x > 0 and y < 0:
    print("It's in the 4th quarter")
else:
    print("Coordinates can't be equal 0")
