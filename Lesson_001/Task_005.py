#Напишите программу, которая принимает 
#на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
import math
print("Hello, username. Let's see the distance between two points in 2D space. ")
xa = int(input("Enter a number for your first X: "))
ya = int(input("Enter a number for your first Y: "))
xb = int(input("Enter a number for your second X: "))
yb = int(input("Enter a number for your second Y: "))
result = float(math.sqrt((xb - xa)**2 + ((yb - ya)**2)))
print(f' {round(result, 2)}')