import pytest
from datetime import datetime, timedelta
from typing import Callable

class PerformanceError(Exception):
    def __init__(self, runtime:timedelta,limit:timedelta):
        self.runtime = runtime
        self.limit = limit
    def __str__(self):
        return f"Performance test failed. Function took {self.runtime.total_seconds()} seconds, which is longer than the limit of {self.limit.total_seconds()} seconds"


@pytest.fixture
def timer(runtimeLimit=timedelta(seconds=2)):
    start = datetime.now()
    yield
    end = datetime.now()
    final = end-start
    print(f"Time taken: {final.total_seconds()}")
    if final > runtimeLimit:
        raise PerformanceError(final, runtimeLimit)




def track_performance(method: Callable, runtimeLimit=timedelta(seconds=2)):
    def run_function_validate_runtime(*args, **kwargs):
        start = datetime.now()
        result = method(*args, **kwargs)
        end = datetime.now()
        final = end-start
        print(f"Time taken: {final.total_seconds()}")
        if final > runtimeLimit:
            raise PerformanceError(final, runtimeLimit)
        return result
    return run_function_validate_runtime


