# Задайте список из n чисел последовательности (1 + 1/n) ** n и выведите на экран их сумму.
# Пример:
# - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
# Сумма 9.06
""""Вариант 1. Этот вариант выводит список, и сумму равную 10. По примеру это не правильно."""
# n = int(input())
# out_dict = {}
# for i in range(1, n + 1):
#     out_dict[i] = round((1 + 1 / n) ** n, 3) 
# print(out_dict)
# print(sum(out_dict))
"""Вариант 2"""
# from msilib import sequence
# n = int(input('Введите число: ')) 
# def get_squerence(n):
#     return [round((1 + 1 / x)**x, 5) for x in range (1, n + 1)]
# nums = get_squerence(n)
# print(nums)
# print(round(sum(nums), 5))
"""Вариант 3"""
n = int(input('Введите число: '))
res = [round((1+1/i)**i, 3) for i in range(1, n+1)]
print(f'Список: {res}\nСумма: {round(sum(res), 3)}')
