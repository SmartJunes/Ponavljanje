import functools

def divideD(func):
    #def wrapper():
    print("ttTTT1111")
    #func()
    print("ttTTT2222")
    return func

@divideD
def ispisi_godine():
    print("ttt33333")

ispisi_godine()
