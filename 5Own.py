# https://paragonie.com/blog/2016/05/how-generate-secure-random-numbers-in-various-programming-languages#python-csprng
import os
import sys
import random

# Random bytes
bytes = os.urandom(32)
csprng = random.SystemRandom()

# Random (probably large) integer
# random_int = csprng.randint(0, sys.maxint)


Number = 10**5
Randomtime = 10**8
data = [0] * Number

for i in range(Randomtime):
    data[csprng.randint(0, Number - 1)] += 1

# print data

fo = open("data-5.txt", "wb")
print "Name of the file: ", fo.name

for i in range(Number):
    dataOut = str(i) + ' ' + str(data[i]) + '\n'
    fo.write(dataOut)

fo.close()
