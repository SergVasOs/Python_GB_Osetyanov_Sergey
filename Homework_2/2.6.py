# 6.* Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами,
# то есть характеристиками товара: название, цена, количество, единица измерения.
# Структуру нужно сформировать программно, запросив все данные у пользователя.

goods = []
params = {'название': None, 'цена': None, 'количество': None, 'единица измерения': None}  # шаблон словаря
i = 1
while True:
    quite = input("Для ввода товара нажмите Enter, чтобы закончить ввод введите q: ")
    if quite.lower() == 'q' or quite.lower() == 'й':
        break
    new_params = params.copy()
    for key in new_params.keys():
        new_params[key] = input(f'Введите характеристику товара - {key}: ')
    new_params['цена'] = float(new_params['цена'])
    new_params['количество'] = int(new_params['количество'])
    goods.append((i, new_params))
    i += 1
print('Список товаров')
print(goods)
analytics = {'название': [],
             'цена': [],
             'количество': [],
             'единица измерения': []}
for good in goods:
    for key in good[1].keys():
        analytics[key].append(good[1].get(key))
print('Аналитика')
print(analytics)
