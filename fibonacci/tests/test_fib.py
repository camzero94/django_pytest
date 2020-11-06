from typing import Callable

import pytest

from fibonacci.naive import fibonacci_naive


@pytest.mark.parametrize(
    "fib_func",
    [
        fibonacci_naive,
    ],
)
@pytest.mark.parametrize("n,expected", [(5, 5)])
def test_naive( fib_func: Callable[[int], int], n: int, expected: int
) -> None:
    res = fib_func(n)
    assert res == expected
