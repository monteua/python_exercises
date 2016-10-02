import random

playing = True

print "Choose any number from 0 to 100".center(100, '-')
print "After each computer attempt enter 'b' - if your number is bigger and 'l' if lower".center(100, '=')
print "if computer guess is correct just press enter".center(100, '-')

computer_guess = random.randint(0, 101)

print "My guess: ", computer_guess

user_input = raw_input("> ")

g_list = list()

if user_input.lower() == 'b':
    g_list = range(computer_guess+1, 100)
elif user_input.lower() == 'l':
    g_list = range(0, computer_guess-1)
elif len(user_input) < 1:
    print "Good game!"
    playing = False
while playing == True:

    if len(g_list) > 1:
        new_choice = random.choice(g_list)
        print "My guess: ", new_choice
    else:
        #print "Good game"
        print "My guess: ", g_list[0]

        playing = False


    new_input = raw_input("> ")

    if new_input.lower() == 'b':
        g_list = range(new_choice+1, max(g_list))
    elif new_input.lower() == 'l':
        g_list = range(min(g_list), new_choice-1)
    elif len(new_input) < 1:
        print "Good game!"
        playing = False




