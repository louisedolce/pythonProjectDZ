########################################## Л Е К Ц И И
# # пакет для графиков
import matplotlib.pyplot as plt
import numpy as np
#### Лекция №1
# def print_max(d,e):
#     if d > e:
#         print(f'max = {d}')
#     elif:
#         print(f'max = {e}')
#     else:
#         print(f'{d} = {e}')
#
# print_max(7,8) #вывод функции


# def some_func(p):
#     print(f"p внутри функции равно =  {p}")
#
# p = 50
# some_func(100)
# print(f'А если напечатаем p здесь, то будет p = {p}')
# #сначала программа выведем 100, в потом 50, так как здесь используются две разные p


# def some_func_2():
#     global p
#     p = 30
#     print(f'p внутри функции равно {p}')
#
# p = 50
# some_func_2()
# #p = 300 - теперь принт напечатал бы р = 300, потому что функция закончилась
# print(f'а если напечатаем p здесь, то p = {p}')
# p = 4000
# print(f'и вот, если напечатаем p здесь, то p = {p}')


# def func_outer():
#     x = 2
#     print('x равно', x)
#
#     def func_inner():
#         nonlocal x #промежуточное между local и global, исп. когда несколько вложенных функций
#         x = 5
#     func_inner()
#     print('Локальное x сменилось на', x)
# func_outer()


#значенияя аргументов по умолчанию и ключевые аргументы
# def some_letter(letter='a',times=2):
#     print(letter*times)
#
# some_letter()
# some_letter('b')
# some_letter('c', 3)
# some_letter(3) #функция выведет 6, так как подставлен один аругмент, по умолчанию первый, следовательно 2*3=6
# some_letter(times=4)
# some_letter(times=4, letter='d')
# some_letter('d', 4)


# def some_letters(letters, times = 2):
#     print(letters*times)
#
# #some_letters() - ничего не выведет, у lettrs нет значения
# some_letters('ss')
# some_letters('vvv', 5)


# def total(initial=5, *numbers, **keywords):
#     print(f'в переменной initial находится значение {initial}')
#     print(f'в numbers хранится кортеж {numbers}')
#     print(f'а keywords - это словарь: {keywords}')
#
# total(10, 1, 2, 3, vegetables=50, fruits=100)


# оператор return
# def summ_of_numbers(*numbers):
#     s = 0
#     for i in numbers:
#         s += i
#     print(s)
#     return s
#
# summ_of_numbers(2, 3, 4, 5)
# a, b, c, d, e = 6, 7, 8, 9, 10
# our_summ = summ_of_numbers(a, b, c, d, e)
# print(our_summ)


# строки документации
# def print_max_2(d, e):
#     '''Строка в первой логической строке функции является строкой документации для этой функции
#
#  Вторую строку принято оставлять пустой.
#  Начинаем писать с третье встроки - описание функции, всё такое ...  '''
#
#     if d > e:
#         return d
#     elif e > d:
#         return e
#     else:
#         return 'Числа равны'


# модуль numpy
# import numpy as np
#
# a = np.array([2, 3, 4], [5, 5, 6])
# print(a)

# ЛЕКЦИЯ 2
# работа с пакетом numpy
# g = np.arange(10, 30, 8) # массив от 10 до 30 с шагом 8
# h = np.listspace(0, 2, 9) # последнее число - кол-во элементов (сам рассчитывает шаг)

# def f1(i, j):
#     return i-j
# k = np.fromfunction(f1, (2, 3)) # две строки, три столбца
#
# # Операции с массивами
# b = np.array([[1, 2, 3], [4, 5, 6]])
# j = np.array([1, 2, 3])
# m = b + j #с массивами можем проводить любые желаемые операции
#
# n = b + 5
# p = b > 3 # выведет true/false
#
# r = sum(b)
# s = b.min()
#
# print(b[2,3]) # один конкретный элемент - 3 строка, 4 столбец (счет идет от 0)
# print(b[:, 2]) # третий столбец
# print(b[:2]) # первые две строки
# print(b[1:3, 2:4]) # вторая и третья строки, послденее число не включено в диапазон
#
# for row in b:
#     print(row) # построчно делит наш массив
#
# a = np.array([[1,2], [3,4]])
# b = np.array([[5,6], [7,8]])
# print(np.vstack((a,b))) # вертикальное сложение
# print(np.hstack((a,b))) # горизонтальное сложение, они нужны чтобы свзять два массива в один
#
# # тут должна быть хадана матрица из 4 строк...но мне лень писать
# print(np.hsplit(b, 2)) # разбить на 3 части
# print(np.hsplit(b, (1, 3))) # выведет 3 массива: первый столбец, второй и третий, четвертый столбец
#
# a = np.arange(12)
# b = a
# print(b is a) #тру или фолс
# b.shape = (3,4)
#

# plt.plot((0, 1, 2, 3, 4, 5, 6, 7), (0, 3, 1, 2, 1, 5, 4, 0)) # координаты точек х, через запятую у
# plt.show() #выведет график
# # если указать только одни координаты, то они автоматом будут считаться координатами у, а х будет идти от 0 до n
#
# plt.scatter([0, 1, 2, 3, 4], [0, 1, 2, 3, 4]) # такой график выводит точки без соед.линий
#
# # диаграммы (в виде столбиков, но другие виды тоже есть)
# plt.bar(g, h) # вводим дагнные через список
# plt.show()
#
# # я уже запуталась
# fig = plt.figure() #создаем фигуру (область, на которой будем работать)
# ax = fig.add_subplot(111)


# ЛЕКЦИЯ №3
fig = plt.figure()
ax = plt.axes(projection = '3d') #создаем тридэшную проекцию
# zline = np.linspace(0, 15, 1000)
# xline = np.sin(zline)
# yline = np.cos(zline)
# ax.plot3D(xline,yline, zline)
# x = np.linspace(-6, 6, 30)
# y = np.linspace(-6, 6, 30)
# X,Y = np.meshgrid(x,y) #создает координатную сетку, то есть не 30 делений, а конкретное значение в любой точке
# Z = f(X, Y)
#
# plt.show()

import astropy.io.fits as ap
hdulist = ap.open("nastyomysh.fit") # адрес фотографии на компьютере, из которой будем черпать данные о фотонах попавших на пиксель
hdulist.info()
exp = hdulist[0].header['exptime'] #обращаемся к первому слою фото (да, они бывают многослойные)
# header - выводит ключ объекта, позволяет рабоать с мета-данными
print(exp) #можно увидеть данные, которые мы и хотели получить
print(hdulist[0].header[:10])
scidata = hdulist[0].data
print(scidata[1][2]) # сначала строка потом столбец, но по зорошему наоборот
hdulist.close()