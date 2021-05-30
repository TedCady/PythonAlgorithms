import random

def randInt(min = 0,max = 100):
        if max <= min:
                return ("Error: Minimum cannot be >= Maximum")
        num = (random.random() * (max -min)+min)
        return round(num)
print(randInt())
print(randInt(max = 50))
print(randInt(min = 50))
print(randInt(min = 50, max = 150))
print(randInt(max = 0))
print(randInt(min = 7, max = 3))

def randInt2(min = 0, max = 100):
        range = max - min
        if max <= min:
                return False
        return round(random.random() * range + min)
print(randInt2())
print(randInt2(max = 50))
print(randInt2(min = 50))
print(randInt2(max = 150, min = 50))
print(randInt2(max = 0))
print(randInt2(max = 3, min = 10))