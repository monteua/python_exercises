#a = [5, 10, 15, 20, 25]

#print a[0]
#print a[-1]
import random

def first_and_last():
    list1 = list()
    for i in range(0, 20):
        list1.append(random.randint(1, 100))
    list2 = list()
    list2.append(list1[0])
    list2.append(list1[-1])
    print list1
    print "First and Last element of the first list: "
    print list2

first_and_last()
