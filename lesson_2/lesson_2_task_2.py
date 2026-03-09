year=int(input('Введите год: '))
def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False
result = is_year_leap(year)
print(f'Год {year}: {result}')