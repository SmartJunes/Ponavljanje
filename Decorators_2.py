import functools

def divideD(func):
    #x = param1 / param2
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

@divideD
def ispisi_godine(param):
    print(f"Osoba ima{param} godina")

ispisi_godine(15)
