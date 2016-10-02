import random

user_want_to_play = True
guess_count = 0

random_number = random.randint(1, 9)

print "If you want to stop playing type 'exit'"
#print "Enter your guess: "

while user_want_to_play == True:

    print "Enter your guess: "
    user_guess = raw_input("> ")
    #user_guess = int(user_guess)

    #random_number = random.randint(1, 10)
    if user_guess != "exit":
        try:
            user_guess = int(user_guess)
        except ValueError:
            print "Not a number"
            user_guess = raw_input("> ")


    if user_guess == 'exit':
        print "bye!"
        user_want_to_play = False

    elif int(user_guess) == random_number:

        guess_count = guess_count + 1

        print "You win!"
        print "Total number of guesses " + str(guess_count)
        print "Number was " + str(random_number)

        random_number = random.randint(1, 10)
        guess_count = 0

    elif int(user_guess) < random_number:

        print "Higher!"

        guess_count = guess_count + 1

        print "Total number of guesses so far " + str(guess_count)

    elif int(user_guess) > random_number:

        print "Lower!"

        guess_count = guess_count + 1

        print "Total number of guesses so far " + str(guess_count)

#    elif str(user_guess) == "exit":
 #       print "bye!"
  #      user_want_to_play = False
        #break





