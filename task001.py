# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример: 
# - 6782 -> 23
# - 0,56 -> 11
input_n = input('Введите число: ')
sum = 0
for i in input_n:
    if i.isdigit():
        sum += int(i)

print('Сумма цифр в числе равна - ', sum)

