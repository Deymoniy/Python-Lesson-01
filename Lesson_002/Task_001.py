#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:
#- 6782 -> 23
#- 0,56 -> 11

print("Hello, user. Enter number to see summ of its figures")
user_number = float(input('Enter your number '))
summ = 0
user_str = str(user_number)
user_str = user_str.replace('.', '')
num = int(user_str)
while (num > 0):
    summ += num % 10
    num = num // 10

print(f' The summ is {summ}')