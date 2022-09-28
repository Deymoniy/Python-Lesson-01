#Напишите программу, которая по заданному номеру четверти, 
#показывает диапазон возможных координат точек в этой четверти (x и y).

user_input = int(input("Enter a number of a quarter: "))

if user_input == 1:
    print("Possible values: X = 1 to infinty, Y = 1 to infinity")
elif user_input == 2:
    print("Possible values: X = -1 to -infinty, Y = 1 to infinity")
elif user_input == 3:
    print("Possible values: X = -1 to - infinty, Y = -1 to -infinity")
elif user_input == 4:
    print("Possible values: X = 1 to infinty, Y = -1 to infinity")
else:
    print("You've entered wrong number.")