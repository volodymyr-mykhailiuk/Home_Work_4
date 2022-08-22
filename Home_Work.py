from itertools import count
import math
# 1) Написать программу, которая считает 4 числа c клавиатуры и выведет на экран самое большое из них

a, b, c, d = float(input("a = ")), float(
    input("b = ")), float(input("c = ")), float(input("d = "))

if a != b and b != c and c != d:
    if a > b and a > c and a > d:
        print("Greater number is a =", a)
    elif b > c and b > d:
        print("Greater number is b =", b)
    elif c > d:
        print("Greater number is c =", c)
    else:
        print("Greater number is d =", d)
else:
    print("Numbers are equal!")

# 2) Есть девятиэтажный дом, в котором 4 подъезда. Номер подъезда начинается с единицы. На одном этаже 4 квартиры. Напишите программу которая, получит номер квартиры с клавиатуры,
# и выведет на экран, на каком этаже, какого подъезда расположенна эта квартира. Если такой квартиры нет в этом доме, то нужно сообщить об этом пользователю.

print()

number_of_appartment = int(input("Input number of appartment: "))

count_of_appartments_in_entrance = 36
count_of_appartments_on_floor = 4

entrance = math.ceil(number_of_appartment / count_of_appartments_in_entrance)
floor = math.ceil(number_of_appartment /
                  count_of_appartments_on_floor) - int((number_of_appartment / count_of_appartments_in_entrance)) * 9

if 1 <= number_of_appartment <= 144:
    entrance = math.ceil(number_of_appartment /
                         count_of_appartments_in_entrance)
    floor = math.ceil(number_of_appartment /
                      count_of_appartments_on_floor) - int((number_of_appartment / count_of_appartments_in_entrance)) * 9
else:
    print("Appartment is not in this house!")

print("Entrance:", entrance, "Floor:", floor)

# 3) Определить количество дней в году, который вводит пользователь. В високосном году - 366 дней, тогда как в обычном их 365. Високосный год определяется по следующему правилу:
# Год високосный, если он делится на четыре без остатка, но если он делится на 100 без остатка, это не високосный год. Однако, если он делится без остатка на 400, это високосный год.
print()

year = int(input("Year = "))

if (year % 4 == 0 or year % 400 == 0) and year % 100 != 0:
    print("366 days in", year, "year")
else:
    print("365 days in", year, "year")

# 4) Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано: a, b, c – стороны предполагаемого треугольника. Напишите программу, которая укажет,
# существует ли такой треугольник или нет.
print()

a, b, c = float(input("a = ")), float(input("b = ")), float(input("c = "))

if (a + b) > c and (b + c) > a and (a + c) > b:
    print("Triangle exist.")
else:
    print("Triangle doesn't exist.")
