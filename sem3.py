from logo import logo
import random
from os import system as sys


#  Первая задача
sys('CLS') 
print(logo)
print("ЗАДАЧА № 1.\nЗадайте список из нескольких чисел. Напишите программу, \
\nкоторая найдёт сумму элементов списка, стоящих на нечётной позиции.\n\
    Введите число для рандомайзера: ")

def new_random_list(n):
    first_list = list(x for x in range(31*n, 73*n, n))
    print(f"Получился такой список: \n {first_list}")
    return first_list

def not_even_sum(z):
    result = 0
    for i in range(len(z)):
        if not i%2:
            result += z[i]
    return result 

print(f"Сумма элементов на нечетной позиции = {not_even_sum(new_random_list(int(input())))}.")
exit = input("\nНажмите ввод, чтобы продолжить...")

########################################
# Вторая задача
sys('CLS') 
print(logo)
print("ЗАДАЧА № 2.\nНапишите программу, которая найдёт произведение пар чисел списка.\
\nПарой считаем первый и последний элемент, второй и предпоследний и т.д.")

def pairs_on_the_edge(random_list):
    result_list = [a for a in range(len(random_list)//2)]
    for i in result_list:
        result_list[i] = int(random_list[i])*int(random_list[-i-1])
    return result_list

second_list = new_random_list(int(input("Введите число для рандомайзера: ")))

print(f"Вот такой получился в результате: {pairs_on_the_edge(second_list)}")
exit = input("\nНажмите ввод, чтобы продолжить...")

########################################
# Третья задача
sys('CLS') 
print(logo)
print("ЗАДАЧА № 3.\nЗадайте список из вещественных чисел. Напишите программу,\
\nкоторая найдёт разницу между максимальным и минимальным значением дробной части элементов.")
def float_num_list(float_input):
    float_list = []
    for y in range(7):
        float_list.append(random.uniform(-float_input, float_input))
    return float_list
def float_diff(float_li):
    maximum = 0
    minimum = float_li[0]
    for i in float_li:
        if i > maximum:
            maximum = i
    for i in float_li:
        if i < minimum:
            minimum = i
    diff = maximum - minimum
    return diff


    diff = max(float_li)-min(float_li)
    print(max(float_li))
    # return diff

new_float_list = float_num_list(float(input("Введите любое вещественное число (float): ")))
print(f"Получился вот такой рандомный список: {new_float_list}")
print(f"Вот такая разница: {float_diff(new_float_list)}")
exit = input("\nНажмите ввод, чтобы продолжить...")
########################################
# Третья задача
sys('CLS') 
print(logo)
print("ЗАДАЧА № 4.\nНапишите программу, которая будет \
    преобразовывать десятичное число в двоичное.")

def decimal_to_binary(dec):
    bin_str = bin(int(dec))
    binary = bin_str.removeprefix("0b")
    return binary

decimal = int(input("Введите целое число: "))
print(f"Вот такое двоичное числополучилось: {decimal_to_binary(decimal)}")
exit = input("\nНажмите ввод, чтобы продолжить...")

########################################
# Третья задача
sys('CLS') 
print(logo)
print("ЗАДАЧА № 5.\nЗадайте число.\
\nСоставьте список чисел Фибоначчи, в том числе для отрицательных индексов.")

def fibonacci(number):
    if number in (-1, 1, 2):
        return 1
    if number == 0:
        return 0
    if number < 0:
        return -(fibonacci(-number - 1) + fibonacci(-number - 2))
    return fibonacci(number - 1) + fibonacci(number - 2)
     
def f_list(num):
    new_f_list = []
    for i in range(-num, num+1):
        new_f_list.append(fibonacci(i))
    return new_f_list

print(f"Вот такой список: {f_list(int(input('Введите коеффициент: ')))}")

exit = input("THAT'S ALL FOLKS!\nНажмите ввод, чтобы закончить")