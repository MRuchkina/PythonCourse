#Реализуйте алгоритм перемешивания списка

import random

list = [7,56,277,87,87,58]

print ("Начальный список: " + str(list))

for i in range(len(list)-1, 0, -1):
    j = random.randint(0, i + 1) 
    list[i], list[j] = list[j], list[i] 

print ("Перемешанный список: " +  str(list))