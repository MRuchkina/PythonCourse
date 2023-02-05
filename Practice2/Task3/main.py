#Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму
def sequence(n):
    return[round((1 + 1 / i)**i, 2) for i in range (1, n + 1)]          


n = int(input("Введите количество чисел в списке: "))
sum = 0
d = {i : 3*i + 1 for i in range(1,n+1)}
print(f"Для n = {n}: {d}")

print(f'Список для {n} чисел =',sequence(n))

for i in range(1, n + 1):
    sum += (1 + 1 / i) ** i
print(f'Сумма последовательности из {n} чисел равна: {sum}')