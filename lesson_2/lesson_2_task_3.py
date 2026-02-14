import math
a=float(input('Введите сторону: '))
def square(a):
    result = a * a
    return result

result = square(a)
result_2 = math.ceil(result)
print(result_2)