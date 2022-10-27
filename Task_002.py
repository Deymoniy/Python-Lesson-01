#Напишите программу, которая найдёт произведение пар чисел списка. 
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.

#Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]
ints = [x for x in range(1, 11)]
first=[]
last= []
res = []
item = 0
for item in range(len(ints) // 2):
    first.append(ints[item])  
ints.reverse()
for item in range(len(ints) // 2):
    last.append(ints[item])
for item in range(len(first)):
    res.append(first[item] * last[item])   
print(res)