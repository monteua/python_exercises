#http://www.practicepython.org/

import random

print "Make your choice - rock, paper, scissors. If you want to close the game - write 'exit'"
#user_choice = raw_input("> ")

#computer_choice = random.choice([rock, paper, scissors])

game_on = True

while game_on == True:

    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    user_choice = raw_input("> ")

    if user_choice.lower() == computer_choice:
        print 'You choose ' + str(user_choice)
        print "Computer choose " + str(computer_choice)
        print "Draw"
        #break

    elif user_choice.lower() == 'rock' and computer_choice == 'scissors':
        print 'You choose ' + str(user_choice)
        print "Computer choose " + str(computer_choice)
        print "You win!"
        #break

    elif user_choice.lower() == 'paper' and computer_choice == 'rock':
        print 'You choose ' + str(user_choice)
        print "Computer choose " + str(computer_choice)
        print "You win!"
        #break

    elif user_choice.lower() == 'scissors' and computer_choice == 'paper':
        print 'You choose ' + str(user_choice)
        print "Computer choose " + str(computer_choice)
        print "You win!"
        #break

    elif user_choice.lower() == 'exit':
        print "Bye!"
        game_on = False

    elif user_choice.lower() not in ['rock', 'paper', 'scissors', 'exit']:
        print "Error! Make a correct choice!"

    else:
        print 'You choose ' + str(user_choice)
        print "Computer choose " + str(computer_choice)
        print "Computer wins!"
        #break
