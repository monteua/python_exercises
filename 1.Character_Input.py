import datetime

print "Hello!"
print "What's your name?"

user_name = raw_input(">")

print "Hello " + user_name
print "How old are you?"

user_age = raw_input(">")

print "Thank you " + user_name

new_age = 100 - int(user_age) + datetime.date.today().yeard

print "You will be 100 years old in ", new_age
