import random
#basic lists for test
#list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#create empty lists
list1 = list()
list2 = list()
list3 = list()

#generating random lists
for i in range(0, 1024):

    list1.append(random.randint(1, 8196))

    list2.append(random.randint(1, 4096))



#loop
for number in list1:
    for num in list2:
        if number == num and num not in list3:
            list3.append(num)



    #if number in list2 == True and number in list3 == False:
    #    list3.append(number)
    #else:
    #    continue

print list3
