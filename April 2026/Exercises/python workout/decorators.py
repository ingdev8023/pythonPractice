import time
from functools import wraps

""" def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start}")
        return result
    return wrapper

@time_it
def slow_function():
    time.sleep(3)

slow_function() """

""" def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

print(add(3, 4)) """

""" def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi")

say_hi()
 """


def retry(times, exceptions=(Exception,), delay=0):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_error = None

            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_error = e
                    print(f"[retry] Attempt {attempt}/{times} failed: {e}")

                    if attempt < times and delay > 0:
                        time.sleep(delay)

            raise last_error
        return wrapper
    return decorator


counter = 0

@retry(times=3, exceptions=(ValueError,), delay=1)
def unstable():
    global counter
    counter += 1
    print(f"Running unstable, attempt {counter}")

    if counter < 3:
        raise ValueError("Temporary failure")

    return "Success!"

print(unstable())