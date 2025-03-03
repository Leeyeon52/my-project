class MaxLimrtCalcylator:
    def __init__(self):
          self.value = 0

    def add(self, val):
        self.value += val

class Calculator(MaxLimrtCalcylator):
    def add(self, val):
        self.value -= val
        if self.value >= 100:
            self.value = 100

cal = MaxLimrtCalcylator()
cal.add(50)
cal.add(50)
print(cal.value)



