#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def sum_decorator(start):
    """
    Декоратор для функции, который принимает начальное значение суммы.
    """
    def decorator(func):
        def wrapper(string_of_numbers):
            numbers = [int(num) for num in string_of_numbers.split()]
            result_sum = func(numbers)
            return result_sum + start

        return wrapper

    return decorator


@sum_decorator(start=5)
def calculate_sum(numbers):
    """
    Функция для подсчета суммы списка чисел.
    """
    return sum(numbers)


if __name__ == "__main__":
    input_string = input("Введите строку целых чисел через пробел: ")

    result = calculate_sum(input_string)

    print(f"Сумма чисел с учетом начального значения: {result}")
