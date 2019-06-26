def fibonacci_v1(n):
    if n > 0:
        if n == 1:
            return [0]
        elif n > 1:
            res = [0] * n
            res[1] = 1
            for i in range(2, n):
                res[i] = res[i - 1] + res[i - 2]
            return res
    else:
        print('Число элементов должно быть целым и положительным!')


def fibonacci_v2(n):
    if n > 0:
        if n == 1:
            return [0]
        elif n > 1:
            res = [0, 1, ]
            for i in range(2, n):
                res.append(res[i - 1] + res[i - 2])
            return res

    else:
        print('Число элементов должно быть целым и положительным!')


def fibonacci_generator():  # генератор - итератор
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def fibonacci_iterator(n):
    if n > 0:
        if n == 1:
            return [0]
        elif n > 1:
            it = iter(list(range(2, n)))
            res = [0, 1, ]
            while True:
                try:
                    x = next(it)
                except StopIteration:
                    break
                res.append(res[x - 1] + res[x - 2])
            return res


if __name__ == "__main__":
    n = int(input('Введите число элементов последовательности: '))
    print(f'fibonacci_v1({n}): \n', fibonacci_v1(n))
    print(f'fibonacci_v2({n}): \n', fibonacci_v2(n))
    # import timeit
    # print(timeit.timeit("fibonacci_v1(n)", setup="from __main__ import fibonacci_v1, n", number=10))
    # print(timeit.timeit("fibonacci_v2(n)", setup="from __main__ import fibonacci_v2, n", number=10))
    print(f'fibonacci_iterator({n}): \n', fibonacci_iterator(n))
    f = fibonacci_generator()
    result = []
    for x in range(n):
        result.append(f.__next__())
    print('Ряд Фибоначчи (итератор v2): \n', result)

    # Результат
    # Введите число элементов последовательности: 10
    # fibonacci_v1(10):
    #  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    # fibonacci_v2(10):
    #  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    # fibonacci_iterator(10):
    #  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    # Ряд Фибоначчи (итератор v2):
    #  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
