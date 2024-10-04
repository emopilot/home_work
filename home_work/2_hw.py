def task_1() -> None:
    # Создание переменных с разными типами данных
    my_int: int = 10
    my_float: float = 3.14
    my_str: str = "Hello, world!"
    my_list: list = [1, 2, 3, 4, 5]
    my_bool: bool = True

    # Вывод типов данных каждой переменной
    print(f"Тип my_int: {type(my_int)}")
    print(f"Тип my_float: {type(my_float)}")
    print(f"Тип my_str: {type(my_str)}")
    print(f"Тип my_list: {type(my_list)}")
    print(f"Тип my_bool: {type(my_bool)}")


# Вызов функции
task_1()

def task_2() -> None:
     a = [1, 2, 3, 5, 8, 13, 21]

     # Вывод первых трех элементов списка
     print("первые 3 значения списка", a[0:3])

 # Вызов функци
task_2()

def task_3(num: float) -> float:
    # Возвращаем квадрат числа
    return num ** 2

# Пример вызова функции
result = task_3(4)
print(result)  # Вывод: 16
