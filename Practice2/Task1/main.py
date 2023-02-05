#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр

def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


str = input("Введите вещественное число: ")

if is_number(str):
    sum = 0 
    for num in str:
        if is_number(num):
            sum = sum + int(num)
else:    
    print('Вы ввели не вещественное число!')

print (sum)