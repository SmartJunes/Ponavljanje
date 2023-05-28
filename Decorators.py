import functools

def start_end_decorator(fuct):
    @functools.wraps(fuct)
    def wrapper(*args, **kwargs):
        print("start")
        result = fuct(*args, *kwargs)
        print("end")
        return result
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5

print(help(add5))
print(add5.__name__)

result = add5(5)
print(result)