# from calendar import month
#
#
def print_max(num1: float, num2: float):

# Проверка какое число больше
    if num1 > num2:
        print(f"Наибольшее число: {num1}")
    elif num2 > num1:
        print(f"Наибольшее число: {num2}")
    else:
        print("Оба числа равны")

# Пример вызова функции
print_max(10, 14)

def check_difference(num1: float, num2: float):

# Проверка разницы чисел
    if abs(num1-num2) == 135:
        print("yes")
    else:
        print("no")

# Пример вызова функции
check_difference(150, 15)
check_difference(2116, 1971)

def get_season(month: int):

# Какой месяц к какому сезону относится
    if month in [12, 1, 2]:
        print("Winter")
    if month in [3, 4, 5]:
        print("Spring")
    if month in [6, 7, 8]:
        print("Summer")
    if month in [9, 10, 11]:
        print("Autumn")
    else:
        print("Неверный номер месяца")

# Пример вызова функций:
get_season(2)

def check_numbers(num1: float, num2: float, num3: float):

    if num1 > 10 and num2 > 10 and num3 > 10:
        print ("yes")
    else:
        print("no")

# Пример вызова функции:
check_numbers(33, 43, 9)


def count_positive(numbers: list):
    # Подсчитываем количество положительных чисел в списке
    count = 0
    for num in numbers:
        if num > 0:
            count += 1
    return count

# Пример вызова функции
numbers = [-5, 10, 3, -2, 8]
result = count_positive(numbers)
print(f"Количество положительных чисел: {result}")


def calculate_days(years: int, months: int):

    days_in_year = 12 * 29

    total_days = (years * days_in_year) + (months * 29)

    return total_days

# Пример вызова функции:
years = 2
months = 5
result = calculate_days(years, months)
print(f"Колличество дней: {result}")