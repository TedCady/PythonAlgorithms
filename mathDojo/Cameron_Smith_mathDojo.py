class mathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result += num
        for i in nums:
            self.result += (i)
        return self
    def subtract(self, num, *nums):
        self.result -= num
        for i in nums:
            self.result -= (i)
        return self
md = mathDojo()
x = md.add(2,1).add(2,2,5).subtract(3,1,2).result
print(x)