print('                                  ▄▄▓▓▓▓▓▄,\n                                ▄▓▓▓▓▓▓▓▓▓▓▓,\n                              ╓▓▓▓▓▓▀,▄▄ ▀▓▓▓r\n                             ▓▓▓▓▓▓▓ █▓▓▌ ▓▓▓▌\n                           ╓▓▓▓▓▓▀▀▓▓▄▄,▄▓▓▓▓\nLEAPIN-IO                 ▄▓▓▓▓▓▓▓▌ ▓▓▓▓▓▓▓▀\n                        ╓▓▓▓▓▓▓▓▓▓ ▐▓▓▓▀▀"\n                           ▓▓▓▓▓▄,  ▀▓▓▄,\n                              "▀▓▓▓▓ⁿ\n                                 `▀ "\n')

print("Задача №1.Напишите программу, которая принимает на вход \
\nвещественное число и показывает сумму его цифр.\nВведите число: ")

float_str = input()
float_sum = 0
for i in float_str:
    try:        #На случай, если будет ошибка при преобразовании запятой или точки в число
        float_sum += int(i)
    except:
        pass
print(f"Сумма цифр = {float_sum} \n\n\n")


print("Задача №2. Напишите программу, которая принимает на вход число N\
\nи выдает набор произведений чисел от 1 до N.\nВведите число N: ")

n = int(input())
num_list = list()
result = list()
result.append(1)
for i in range(1,n+1):
    num_list.append(i)
for i in range(1,n):    
    result.append(result[i-1]*num_list[i]) 
print(f"Получается такой набор: {result}")


print("Задача №3.Задайте список из n чисел последовательности N\
\n$(1+1/n)^n$ и выведите на экран их сумму.\nВведите число n: ")

n2 = int(input())
new_dict = dict()
sum = 0
for i in range(1,n2+1):
    new_dict[i] = (1+1 /i)**i
    sum +=new_dict[i]
print(new_dict)
print(sum)

print("Задача №4.Задайте список из N элементов, заполненных числами из промежутка [-N, N].\
\nНайдите произведение элементов на указанных позициях.\
    \nПозиции хранятся в файле file.txt в одной строке одно число.\
    \nВведите число N: ")
import random as rand

list_of_positions = list()
rand_list = []
def infile_positions(a):
    for i in range(0,a):
        list_of_positions.append(rand.randint(0,a-1))
        
    with open("file.txt", "w") as f:
        for i in range(0,a):
            f.write(str(list_of_positions[i]) + "\n")
    return list_of_positions
def random_list(a):
    for i in range(0,a):
        rand_list.append(rand.randint(-a,a))
        if rand_list[i] == 0:
            rand_list[i] = 1
    return rand_list

def multiply(a):
    multiplication = 1
    with open("file.txt", "r") as f:
        lines = f.readlines()
        for i in lines:
            multiplication = multiplication * int(rand_list[int(i)])
    return multiplication
a = int(input())
print(f'Произведение чисел в последовательности {random_list(a)} \
    на позициях {infile_positions(a)} = {multiply(a)}')



print("Задача №5.Реализуйте алгоритм перемешивания списка.\
    \nВведите число элементов списка: ")

def create_list(number_of_elements):
    random_list2 = []
    for i in range(0,number_of_elements):
        random_list2.append(rand.randint(10,99))
    return random_list2


def list_shuffle(list2):
    list3 = list2.copy()
    x = [i for i in range(len(list2))]
    rand.shuffle(x)
    for i in range(len(list2)):
        list3[i] = list2[int(x[i])]
    return list3

list_before_shuffle = create_list(int(input()))
list_after_shuffle = list_shuffle(list_before_shuffle)
print(f"Вот такой список получился: {list_before_shuffle}")
print(f"А теперь перемешаем... И вот: {list_after_shuffle} ")
