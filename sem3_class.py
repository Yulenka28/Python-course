"""
# задача 17
# вариант решения 1
list_1 = [1, 7, 2, 0, -1, 3, 4, 4]
Q = len(set(list_1))
print(Q)

# вариант решения 2 через for
list_with_duplicates = [1, 1, 2, 0, -1, 3, 4, 4]
list1 = [1, 2, 0, -1, 3, 4]

for i in list_with_duplicates:
    if i not in list1:
        list1.append(i)
        
print(len(list1))

# третий варинат через срезы
str1 = [1, 1, 2, 0, -1, 3, 4, 4]
counter = 0
for i in range(len(str1)):
    if str1[i] not in str1[:i]:
        counter += 1
print(counter)

"""
"""
# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,  K – положительное число.
# Input:   [1, 2, 3, 4, 5] k = 3
# Output:  [3, 4, 5, 1, 2]
# вариант 1

list_1 = [7, 9, 13, 15, 17, 18]
list_2 =[]
t = int(input("введите шаг: "))
k = t

for i in range (0, len(list_1)):
    if i<(len(list_1)-k):
       list_2.append(list_1[k+i])
    else:
       list_2.append(list_1[i-(len(list_1)-k)])
            
print((list_2))

# вариант 2

lst = [1, 2, 3, 4, 5, 6, 7]
k = 3
for i in range(k):
    el = lst.pop()
    lst.insert(0, el)
print(lst)

"""

#Напишите программу для печати всех уникальных значений в словаре. 
# Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
# {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}] 
#Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

"""
#достаем слова по ключу
my_dict = {
    'V': 'S001',
    'B': 'rgreg'
}
for key in my_dict:
    print(my_dict[key])

# достаем ключи
my_dict = {
    'V': 'S001',
    'B': 'rgreg'
}
for key in my_dict:
    print(my_dict[key])

# достаем значения
my_dict = {
    'V': 'S001',
    'B': 'rgreg'
}

for val in my_dict.values():
    print(val)

"""

# my_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, \
#          {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}] 

# all_val = []
# for now_dict in my_list:
#     for val in now_dict.values():
#         all_val.append(val)


# print(set(all_val))

list_1 = [1, 2, 3, 15, 11]
k = 13
number=0
for i in range(len(list_1)):
    if (k-list_1[i])<k-number and k-list_1[i]>0:
        number=i
print(list_1[number])