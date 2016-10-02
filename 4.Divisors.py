user_number = raw_input("Enter the number: ")
user_number = int(user_number)

divisors = range(2, 11)

for number in divisors:
    if user_number % number == 0:
        print "Your number can be divided by " + str(number)
    else:
        continue
