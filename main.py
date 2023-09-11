# print("Введите первое число: ")
# a = int(input())
# print("Введите второе число: ")
# b = int(input())

# print(a, ' + ', b, '=', a + b)

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else:
#     print('Привет, ', username)

# n = 423
# summa = 0
# while n > 0:
#     x = n % 10
#     summa = summa + x
#     n = n // 10
# print(summa)
"""
list_1 = []
list_1 = list()
print(list_1)
list_1 = [1, 5, 3, 4]
print(*list_1) #выведет лист без квадратных скобок
list_1 = [1, 5, 3, 4]
for i in list_1:  #напечатает каждый эл-т списка
    print(i)
print(len(list_1)) #длина списка покажется
print(list_1[2]) #покажет эл-т из списка по индексу 2 (счет с 0!)
print(list_1[-1]) #эл-т из списка но с конца

list_1 = [1, 5]
print(list_1)
list_1.append(8) #Добавит эл-т в конец списка
print(list_1)

list_1 = []  #создали пустой список и заполнили его 
print(list_1)
for i in range(5):
    list_1.append(i)
    print(list_1)

list_1 = [12, 7, -1, 21]
a = list_1.pop(1) #функция поп еще и возвращает эл-т, ему можно задать отдельную переменную!
print(a) 

list_1 = [12, 7, -1, 21]
print(list_1.insert(2, 11)) #вставляет эл-т, первая цифра- это номер позиции, вторая- какой эл-т
print(list_1)

t = (1, 2, 3, 5,) #это создали кортедж
for i in t:  #вывели по элементно
    print(i)

for i in range(len(t)):
    print(t[i])
    """

# def select(f, col):
#     return [f(x) for x in col]
# def where(f, col):
#     return [x for x in col if f(x)]
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data)
# res = where(lambda x: x % 2 == 0, res)
# print(res) # [2, 8, 38]
# res = list(select(lambda x: (x, x ** 2), res))

list_1 = [x for x in range (1,20)]
list_1 = list(map(lambda x: x + 10, list_1 ))
print(list_1)