import random

Number = 10**5
Randomtime = 10**8
data = [0] * Number

for i in range(Randomtime):
    data[random.randrange(Number)] += 1

# print data

fo = open("data-1.txt", "wb")
print "Name of the file: ", fo.name

for i in range(Number):
    dataOut = str(i) + ' ' + str(data[i]) + '\n'
    fo.write(dataOut)

fo.close()
