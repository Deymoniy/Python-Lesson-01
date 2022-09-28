#Напишите программу для. проверки истинности утверждения 
#¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in [True,False]:
    for y in [True,False]:
        for z in [True,False]:
            result = (not (x or y or z))
            result2 = not x and not y and not z
            print(f'First time your left side equals {result} and second {result2}')
            print(f' So they are {result == result2}')
