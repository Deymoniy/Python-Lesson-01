#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#Пример:
#- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
print("Hello, user. Enter number to see factorial for each of its elements")
num = input('Enter your number ')
lst_num = list(map(int, str(num)))
for item in lst_num:
    fact = 1
    for number in range(1,item+1):
        fact = fact * number
    print ("Factorial of", item, "is", fact)

