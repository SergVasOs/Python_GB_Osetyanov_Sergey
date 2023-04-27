# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.
#
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func1(x, y):
    return x ** y
def my_func(x, y):
    result = 1
    for i in range(abs(y)):
        result *= 1 / x
    return result

a = float(input('Введите действительное положительное число: '))
b = int(input('Введите целое отрицательное число: '))
print(my_func(a, b))
print(my_func1(a, b))