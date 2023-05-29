# result = 0
# count = 0
# while True:
#     number = int(input('Введите число\n'))
#     if number >= 0:
#         result += number
#         count += 1
#     if number < 0:
#         break
#     print('Сумма чисел = ', result)
# print('Результат =', result / count)

# result = 0
# while True:
#     number = int(input('Введите число\n'))
#     if number == 0:                      #and number % 2 == 1 or number < 0 and number % 2 == 1: 0 четный
#         break
#     if number % 2 == 0:
#         continue
#     result += number
# print('Сумма нечетных чисел = ', result)

# 6.4 операторы использовать
# 6.6 б + разность между ними
# 6.42 а

# 6.4
# result = 0
# while True:
#     number = int(input('Введите число\n'))
#     if number > 0:
#         break
#     result += 1
# print('Количество введенных отрицательных чисел =',result)

# 6.6 б
# while True:
S = 105
print(S % 10)

# 6.42 а
number = int(input('Введите число\n'))
number1 = 0
number2 = 0
NomerPoryd = 0
while number > 0:
    num = number % 10 # переход в конец введенного числа
    number1 = num
    NomerPoryd += 1
    print('Порядковый номер', num, '=', NomerPoryd)
    if number1 > number2:
        number2 = number1
    number = number // 10 # отделение последнего числа

