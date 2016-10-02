user_string = raw_input("Enter the string: ")

user_string = str(user_string)
reversed_string = user_string[::-1]
if user_string == reversed_string:
    print "Your string is palindrome!"
else:
    print "Your string is not palindrome!"
