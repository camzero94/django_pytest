
from fibonacci.fib import fibonacci, fib_cached
from fixtures import  timer,track_performance 
from typing import Callable
import pytest

# def my_parametrized(*args, **kwargs):
#     def wrap_function(func):
#         def exec_fun():
#             #extract args return map [{n:0, expected:0},{n:1, expected:1}...]
#             string_args, values = args
#             key_arr = string_args.split(",")
#             parsed_arr = [  {
#                             key_arr[0]:first_arg,
#                             key_arr[1]:second_arg
#                             }
#                             for first_arg, second_arg in values
#                          ]
#             for val in parsed_arr:
#                 result = func(**val)
#             return result
#         return exec_fun
#     return wrap_function

# @my_parametrized("n,expected",[(0,0),(1,1),(2,1),(20,6765)])

# # Parametrize 
# @pytest.mark.parametrize("n,expected",[(0,0),(1,1),(2,1),(20,6765)])
# def test_fibonacci_multiple_values(n:int, expected:int):
#     res = fibonacci(n)
#     assert res == expected







# Cache Version


@pytest.mark.performance
@pytest.mark.parametrize("func", [fibonacci, fib_cached])
@pytest.mark.parametrize("n,expected",[(20,6765)])
def test_fibonacci_multiple_values_cache(timer: Callable,func: Callable[[int], int], n: int, expected:int):
    res = func(n)
    assert res == expected


# @pytest.mark.performance
# @track_performance
# def test_fibonacci():
#     res = fibonacci(40)
#     assert res == 102334155 
