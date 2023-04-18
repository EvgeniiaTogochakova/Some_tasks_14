# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# Пример:
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12
import random

n = int(input('Сколько элементов в первом наборе чисел? '))
m = int(input('Сколько элементов во втором наборе? '))
min_number = int(input('Введите минимальное число для рандомайзера: '))
max_number = int(input('Введите максимальное число для рандомайзера: '))
# list_n = [int(input('Введите целые числа первого списка: ')) for i in range(n)]
# list_m = [int(input('Введите целые числа второго: ')) for i in range(m)]
print(list_n := [random.randint(min_number,max_number) for i in range(n)])
print(list_m := [random.randint(min_number,max_number) for i in range(m)])
set_from_list_n = set(list_n)
set_from_list_m = set(list_m)
print('Повторяющиеся числа по возрастанию', intersection := sorted(set_from_list_n & set_from_list_m))

