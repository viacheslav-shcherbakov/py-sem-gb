from logo import logo
print(logo)

# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
print("Введите номер дня недели: ")

day_of_week = int(input())
if day_of_week >=1 and day_of_week <= 5:
    print("Будний день.")
else:
    print("Выходной")

##############################################

# Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x=10
y=23
z=45

print(not (x or y or z) == (not x and not y and not z))


##################################################
# Напишите программу, которая принимает на вход координаты 
# точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти 
# плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:
x=34
y=-30

# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

if x>0 and y>0:
    print("1")
elif x>0 and y<0:
    print("2")
elif x<0 and y<0:
    print("3")
elif x<0 and y>0:
    print("4")   


# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

print("Введите номер четверти: ")
quater = int(input())
if quater == 1:
    print("x>0 y>0")
elif quater == 2:
    print("x<0 y>0")
elif quater == 3:
    print("x<0 y<0")
elif quater == 4:
    print("x<0 y>0")
##############################################
# Напишите программу, которая принимает на вход координаты 
# двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math

print("Введите x1: ")
x1 = int(input())
print("Введите x2: ")
x2 = int(input())
print("Введите y1: ")
y1 = int(input())
print("Введите y2: ")
y2 = int(input())
distance = round(math.sqrt((x2-x1)**2+(y2-y1)**2),2)
print(distance)