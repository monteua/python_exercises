#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

import random
#create empty lists
a = list()
b = list()
c = list()

#generating random lists
for i in range(0, 24):

    a.append(random.randint(1, 50))

    b.append(random.randint(1, 50))



for number in a:
    if number in b and number not in c:
        c.append(number)
c.sort()
print c