import pytest
from main import fibonacci_v1, fibonacci_v2, fibonacci_iterator, fibonacci_generator


@pytest.mark.parametrize("n, result", [
    (-10, None),
    (1, [0]),
    (5, [0, 1, 1, 2, 3]),
    (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])])
def test_fibonacci_v1(n, result):
    assert fibonacci_v1(n) == result


@pytest.mark.parametrize("n, result", [
    (-10, None),
    (1, [0]),
    (5, [0, 1, 1, 2, 3]),
    (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])])
def test_fibonacci_v2(n, result):
    assert fibonacci_v2(n) == result


@pytest.mark.parametrize("n, result", [
    (1, [0]),
    (5, [0, 1, 1, 2, 3]),
    (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])])
def test_fibonacci_generator(n, result):
    f = fibonacci_generator()
    res = []
    for x in range(n):
        res.append(f.__next__())
    assert res == result


@pytest.mark.parametrize("n, result", [
    (-10, None),
    (1, [0]),
    (5, [0, 1, 1, 2, 3]),
    (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])])
def test_fibonacci_iterator(n, result):
    assert fibonacci_iterator(n) == result
