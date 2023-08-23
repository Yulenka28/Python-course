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

n = 423
summa = 0
while n > 0:
    x = n % 10
    summa = summa + x
    n = n // 10
print(summa)