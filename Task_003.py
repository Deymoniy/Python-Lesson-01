#Задайте список из вещественных чисел. 
#Напишите программу, которая найдёт разницу между максимальным и минимальным значением 
#дробной части элементов.
#Пример:
#[1.1, 1.2, 3.1, 5, 10.01] => 0.19

data = [1.1, 1.2, 3.1, 5.4, 10.01]
new_data = list(map(lambda x:x%1, data))
rounded_data = [round(elem,3) for elem in new_data]
print(rounded_data)
min_num = min(rounded_data)
print(f'min = {min_num}')
max_num = max(rounded_data)
print(f'min = {max_num}')
res = max_num - min_num
print(res)