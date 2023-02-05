#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

# Чтение чисел из файла
file_data = open("file.txt", "r")
m, n = file_data.read().split("\n")

m, n = int(m)-1, int(n)-1
count = int(input("Введите количество чисел: "))
arr = []

for i in range(-count, count+1):
    arr.append(i)

res = arr[m] * arr[n]

# Вывод результатов
print(f"Первая позиция: {m+1}\nВторая позиция: {n+1}\n Результат: {count}\n{arr}\n{res}")

for i in range(len(arr)-1, 0, -1):
    j = random.randint(0, i + 1) 
    list[i], list[j] = list[j], list[i] 
print ("Перемешанный список: " +  str(list))