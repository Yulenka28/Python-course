"""
Даны два массива чисел. Требуется вывести те элементы
первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит
число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество
элементов во втором массиве. Затем элементы второго массива

"""

# def sortArr (arr1, arr2):
#     arr3 = []
#     for i in arr1:
#        if i not in arr2:
#          arr3.append(i)
#     return arr3

# def elInput (n):
    
#     array_1 = []
#     for i in range(n):
#         array_1.append(int(input("Enter numbers of the array: ")))
#     return array_1

# n = int (input ("Enter quontity of elements for array: "))
# m = int (input ("Enter quontity of elements for array: "))

# array_3 = sortArr(elInput(n), elInput(m))
# print (array_3)

"""
Дан массив, состоящий из целых чисел. Напишите
программу, которая в данном массиве определит
количество элементов, у которых два соседних и, при
этом, оба соседних элемента меньше данного. Сначала
вводится число N — количество элементов в массиве
Далее записаны N чисел — элементы массива. Массив
состоит из целых чисел.
5
1 2 3 4 5 -> 0

5
1 5 1 5 1 -> 2

"""
# def countLessNum (arr1):
#    count=0
#    for i in range (1, n-1):
#     if arr1[i] > arr1[i-1] and arr1[i] > arr1[i+1]:
#         count +=1
#         return count

# def elInput (n):
#     arr1 = []
#     for i in range (n):
#         arr1.append(int(input(f"Enter number {i+1}: ")))
#     return arr1

# n = int(input ("Enter range of array: "))
# arr1 = elInput(n)
# countLessNum (arr1)
# print(countLessNum(arr1))


"""
Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.
Ввод:
1 2 1 2 2 2 3 4
Вывод:
7
"""

# def countPairs(arr1):
#     counter = 0
#     for i in range(len(a)):
#         for j in range(i + 1, len(a)):
#             if a[i] == a[j]:
#                 counter += 1
#     return counter

# a = [int(s) for s in input().split()]
# print(countPairs(a))

"""

"""