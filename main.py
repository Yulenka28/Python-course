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

d = {} #создали словарь
d = dict()  #создали словарь

d['q'] = 'qwerty'  #есть ключ q к которому если обратиться- получим слово qwerty
print(d)
d['w'] = 'werty'
print(d['q'])