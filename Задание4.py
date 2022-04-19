number = int(input("Print number"))
m = number % 10 #остаток от деления, последняя цифра
a = m // 10 #оставшееся число
while a > 0:
    if a % 10 > m:
        m = a % 10
        a = a // 10
        m != 0
print(m)