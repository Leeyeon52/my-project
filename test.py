amount = 10_000_000.0

print(amount)
print(amount + 2000)






class Myclass():
    def __init__(self):
        self.__variable = 10
        self.abc = 20
    def func(self):
        print('>>>',self.__variable)

obj =  Myclass()
obj.func()
print(obj.abc)
#print(obj.__variable)
print(obj._Myclass__variable)
