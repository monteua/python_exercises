divisors_list = list()
def get_number():
    u_num = raw_input("Enter the number: ")
    return int(u_num)

def check_divisor():
    for number in divisors:
        if user_number % number == 0:
            #print "Your number " + str(user_number) + " is Prime!"
            divisors_list.append(number)
        else:
            #print "Your number " + str(user_number) + " can be divided by " + str(number)
            continue

user_number = get_number()

print "You entered " + str(user_number)

divisors = range(1, user_number)
check_divisor()
#print divisors_list
if len(divisors_list) > 1:
    print "Your number is not Prime"
else:
    print "Your number is Prime"

#get_number()

print "Do you want to try another number (y/n)?"
user_input = raw_input("> ")
user_input = user_input.lower()
if user_input == "y" or user_input == "yes":
    get_number()
    #print "You entered " + str(user_input)
    check_divisor()
    divisors = range(1, user_number)
    check_divisor()
    #print divisors_list
    if len(divisors_list) > 1:
        print "Your number is not Prime"
    else:
        print "Your number is Prime"
else:
    print "Bye!"