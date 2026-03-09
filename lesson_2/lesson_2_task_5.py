mon = int(input('Введите месяц года: '))
def month_to_season(mon):
    if mon in [12, 1, 2]:
        print('Зима')
    elif mon in [3, 4, 5]:
        print('Весна')
    elif mon in [6, 7, 8]:
        print('Лето')
    elif mon in [9, 10, 11]:
        print('Осень')
    else:
        print('Такого месяца не существует!')
month_to_season(mon)
