# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке
# возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. one_day — кол-во элементов первого множества. user_distance — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

from random import randint

# first_list = []
# second_list = []
# user_size_first = int(input('Input size for first list: '))
# user_size_second = int(input('Input size for second list: '))

# for i in range(user_size_first):
#     number = randint(0, 10)
#     first_list.append(number)

# for i in range(user_size_second):
#     number = randint(0, 10)
#     second_list.append(number)

# first_set = set(first_list)
# second_set = set(second_list)
# new_list = sorted(list(first_set.intersection(second_set)))

# print(first_set, second_set)  # Для проверки
# print(new_list)


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены
# только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте
# выросло ai ягод. В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит
# из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно
# перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним. Напишите программу для нахождения
# максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.
# Пример:
# 4 -> 1 2 3 4
# 9
# Визуализируем: user_distance - модуль сбора
# 1 2 <-\
# 3 4 <-|
# ^     |
# |-----user_distance

total_bushes = int(input('Input the total number of bushes: '))
shrub_number = int(input('Input the sequence number of the shrub: '))  # 1 <= shrub_number <= total_bushes
total_berries = []
modul_pick = 0

for item in range(total_bushes):
    berries = randint(1, 10)
    total_berries.append(berries)

print(total_berries)  # Для проверки

if shrub_number == total_bushes:
    """Если брать логику архитектуры примера, то последний элемент соседствует с двумя предыдущими кустами"""
    modul_pick = total_berries[shrub_number - 3] + total_berries[shrub_number - 2] + total_berries[shrub_number - 1]
    print(modul_pick)
elif shrub_number == 1:
    """Аналогично взял логику архитектуры примера: первый куст соседствует с двумя последующими кустами"""
    modul_pick = total_berries[shrub_number - 1] + total_berries[shrub_number] + total_berries[shrub_number + 1]
    print(modul_pick)
elif 1 < shrub_number < total_bushes:
    """Если брать логику реальной жизни, то соседними будут куст перед выбранным и куст после выбранного"""
    modul_pick = total_berries[shrub_number - 2] + total_berries[shrub_number - 1] + total_berries[shrub_number]
    print(modul_pick)
else:
    """Невозможно вбить порядковое значение куста больше, чем есть всего кустов. 
    Также невозможно вбить порядковый номер меньше либо равный 0"""
    print('Incorrect the number of bushes')