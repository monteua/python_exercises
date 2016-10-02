a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = []

user_number = raw_input("Enter your number: ")
user_number = int(user_number)

#for i in a:
#    if i < user_number:
#        b.append(i)
b = [i for i in a if i < user_number]

print b