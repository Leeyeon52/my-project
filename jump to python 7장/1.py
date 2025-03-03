def mul3(n):
    return n * 3


def mul5(n):
    return n * 5


# closure.py
class Mul:
    def __init__(self, m):
        self.m = m

    def mul(self, n):
        return self.m * n

if __name__ == "__main__":
    mul3 = Mul(3)
    mul5 = Mul(5)

    print(mul3.mul(10))  # 30 출력
    print(mul5.mul(10))  # 50 출력



# decorator.py
import time

def elapsed(original_func):   # 기존 함수를 인수로 받는다.
    def wrapper():
        start = time.time()
        result = original_func()    # 기존 함수를 수행한다.
        end = time.time()
        print("함수 수행시간: %f 초" % (end - start))  # 기존 함수의 수행시간을 출력한다.
        return result  # 기존 함수의 수행 결과를 리턴한다.
    return wrapper

def myfunc():
    print("함수가 실행됩니다.")

decorated_myfunc = elapsed(myfunc)
decorated_myfunc()


a = [1, 2, 3]
ia = iter(a)
type(ia)

for i in ia:
    print(i)

for i in ia:
    print(i)





# iterator.py
class MyItertor:
    def __init__(self, data):
        self.data = data
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.position >= len(self.data):
            raise StopIteration
        result = self.data[self.position]
        self.position += 1
        return result

if __name__ == "__main__":
    i = MyItertor([1,2,3])
    for item in i:
        print(item)



# generator.py
def mygen():
    for i in range(1, 1000):
        result = i * i
        yield result

gen = mygen()

print(next(gen))
print(next(gen))
print(next(gen))


# c:/doit/typing_sample.py
def add(a: int, b: int) -> int: 
    return a+b

result = add(3, 3.4)
print(result)  # 6.4 출력
