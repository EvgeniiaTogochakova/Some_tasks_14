# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.
# Пример:
# 4 -> 1 2 3 4
# 9

import random

n = int(input('Сколько всего кустов черники? '))
blueberries_bushes = tuple((i for i in range(1, n + 1)))
print(blueberries_bushes)
dict_blueberries = {}
for element in blueberries_bushes:
    dict_blueberries[element] = random.randint(1, 30)
print(dict_blueberries)
number_bush = int(input('Перед каким кустом ставим модуль для собирания ягод? '))
blueberries = 0
for key in dict_blueberries:
    if key == number_bush:
        blueberries += dict_blueberries[key]
print(f'C этого куста соберем {blueberries} ягод')
blueberries_nearby = 0
for key in dict_blueberries:
    if number_bush == 1:
        blueberries_nearby = dict_blueberries[n] + dict_blueberries[2]

    elif number_bush == n:
        blueberries_nearby = dict_blueberries[n-1] + dict_blueberries[1]

    elif key == number_bush - 1:
        blueberries_nearby += dict_blueberries[key]

    elif key == number_bush + 1:
        blueberries_nearby += dict_blueberries[key]

print(f'А с соседних кустов мы соберем {blueberries_nearby}.\nТаким образом, всего получится {blueberries + blueberries_nearby} ягод черники')
