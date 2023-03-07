# Задача №39. Решение в группах

# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: 
# 7

# 3 1 3 4 2 4 12

# 6

# 4 15 43 1 15 1

# Вывод:

# 3 3 2 12


# (каждое число вводится с новой строки)

from random import randint
N = int(input('Введите: '))
M = int(input('Введите: '))
array = []
for i in range(0, N):
    array.append(randint(0,10))

array2 = []
for i in range(0, M):
    array2.append(randint(0,10))


print(array)
print(array2)

for i in array:
    for j in array2:
        if i==j:
            break
    else:
        print(i, end = ' ')


#можно и так строки 40-45
for i in array:
    if i not in array2:
       print(i, end = ' ')







#ИЛИ 

def inputArray(size):
    array = []
    for i in range(size):
        array.append(int(input()))
    return array

N = int(input("Введите размер первого массива: "))
array_1 = inputArray(N)
M = int(input("Введите размер второго массива: "))
array_2 = inputArray(M)
print(array_1)
print(array_2)
print([i for i in array_1 if i not in array_2])
