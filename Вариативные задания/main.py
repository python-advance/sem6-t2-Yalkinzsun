# Разработать функцию, возвращающую список чисел ряда
# Фибоначчи с использованием бесконечных итераторов (модуль itertools).

from itertools import count, islice


def fib_infinite_iterator(n):
    if n > 0:
        if n == 1:
            return [0]
        elif n > 1:
            res = [0, 1, ]
            for i in islice(count(2), n-2):
                res.append(res[i - 1] + res[i - 2])
            return res
    else:
        print('Число элементов должно быть целым и положительным!')


if __name__ == "__main__":
    n = int(input('Введите число элементов последовательности: '))
    print(f'fib_infinite_iterator({n}): \n', fib_infinite_iterator(n))

    # Результат
    # Введите число элементов последовательности: 10
    # fib_infinite_iterator(10):
    #  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
