import pytest
from main import fib_infinite_iterator


@pytest.mark.parametrize("n, result", [
    (1, [0]),
    (5, [0, 0, 1, 2, 3, 5, 8]),
    (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])])
def test_fib_infinite_iterator(n, result):
    assert fib_infinite_iterator(n) == result
