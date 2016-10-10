import random

Number = 10
data = [0] * Number

for i in range(Number):
    data[random.randrange(Number)] += 1

print data
