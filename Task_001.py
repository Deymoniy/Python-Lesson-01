#Задайте список из нескольких чисел. 
#Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

#data = list(int([1, 2, 3, 4, 5, 6]))
data = [x for x in range(1, 10)]
l = len(data)
odd = []
for i in range(l):  
    if i%2==1:
        odd.append(data[i])

print(f'The odd numbers are {odd}')
print(f'And your result is {sum(odd)}')


