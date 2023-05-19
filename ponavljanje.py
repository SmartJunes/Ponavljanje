import timeit


"""
class auto:
    def __init__(self,tip, marka):
        self.tip = tip
        self.marka = marka


auto1 = auto("SUV","")

print(auto1)

 """

N = 5
print (range(1,N))

def for_loop():
    result = 0
    for i in range(1,N):
       #print(str(result) +'' + str(i) )
        result += i
        print(result)
    return result



if __name__ == "__main__":
    print(timeit.timeit(for_loop, number=1))