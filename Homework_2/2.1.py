#1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

l = []
l.append(12)
l.append(6.77)
l.append('string')
l.append([12, 6.77, 'string'])
l.append({'integral': 15, 'float': 6.85, 'string': 'string'})
l.append((18, 7.88, 'string'))
l.append({2, 5, 6, 3, 3, 1, 7})
l.append(frozenset([2, 5, 6, 3, 3, 1, 7]))
l.append(complex(3, -2))
l.append(None)
l.append(True)
l.append(b'Byte text')
l.append(bytearray(b'Byte text'))

for i in l:
    print(i, type(i))