print "Enter the number:"

num = raw_input("> ")
num = int(num)
if num % 4 == 0:
    print "Your number can be divided by 4"

elif num % 2 == 0:
    print "Your number is Even"
else:
    print 'Your number is Odd'