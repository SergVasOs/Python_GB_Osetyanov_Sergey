#5 Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек,
# или убыток — издержки больше выручки. Выведите соответствующее сообщение.
#6. Если фирма отработала с прибылью, вычислите рентабельность выручки.
#Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и
# определите прибыль фирмы в расчёте на одного сотрудника.


income = int(input("Введите значение выручки: "))
outcome = int(input("Введите значение издержек: "))
profit = income - outcome
if profit > 0:
    print("Фирма отработала с прибылью")
    profitability = profit / income
    print('Рентабильность составила {:.2f}'.format(profitability))
    employees = int(input('Введите количество сотрудников: '))
    profit_per_employee = profit / employees
    print('Прибыль фирмы в расчете на одного сотрудника составила {:.2f}'.format(profit_per_employee))
elif profit == 0:
    print("Фирма не получила прибыль, но и не в убытке")
else:
    print("Фирма отработала в убыток")