#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве
import math

x1, y1 = input ("Введите значения координат X и Y для первой точки: ").split()
x1, y1 = [int (x1), int(y1)]

x2, y2 = input ("Введите значения координат X и Y для второй точки: ").split()
x2, y2 = [int (x2), int(y2)]

del_x = x2 - x1
del_y = y2 - y1

dist =  math.isqrt((del_x*del_x) + (del_y*del_y))

print ('Расстояние между точками = ' + str(dist))

