"""
# задача 9. Вычислить факториал
n = int(input())
factorial = 1
i =2
while i <= n:
    factorial *=i
    i +=1
print(factorial)
"""
"""
# задача 11
n = int(input())
fib2 = 1
fib1 = 0
fib = 0
counter = 1
while fib < n:
    fib = fib1 + fib2
    fib1, fib2 = fib2, fib
    counter += 1
print(counter if fib == n else -1)
"""
# n = int(input())
# count = 1
# maxx = 0
# for i in range(n):
#     if n > 0:
#         count += 1
#     else:
#         if count > maxx: 
#             maxx = count
#         count = 0

# print(maxx)

list_1 = [1, 12, 6, 7, 8, 15]
k = 13
b=[abs(list_1[i]-k) for i in range(len(list_1))]
print(list_1[b.index(min(b))])