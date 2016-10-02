import random

def compare_data(random_number, user_guess):
    #random_number = str(get_random_number())
    #user_guess = str(get_user_guess())

    cows_and_bulls = [0,0]
    for i in range(len(user_guess)):
        if random_number[i] == user_guess[i]:
            cows_and_bulls[0] += 1
        else:
            cows_and_bulls[1] += 1
    return cows_and_bulls


if __name__ == "__main__":
    playing = True
    random_number = str(random.randint(1000, 9999))
    guesses = 0

    print("Let's play a game of Cowbull!") #explanation
    print("I will generate a number, and you have to guess the numbers one digit at a time.")
    print("For every number in the wrong place, you get a cow. For every one in the right place, you get a bull.")
    print("The game ends when you get 4 bulls!")
    print("Type exit at any prompt to exit.")


    while playing:
        user_guess = raw_input("Enter your 4-digits guess: ")
        if user_guess == "exit":
            break

        cowbullcount = compare_data(random_number,user_guess)
        guesses+=1
        print random_number
        print("You have "+ str(cowbullcount[1]) + " cows, and " + str(cowbullcount[0]) + " bulls.")

        if cowbullcount[0]==4:
            playing = False
            print "You win the game after " + str(guesses) + "! The number was "+str(random_number)
            break #redundant exit
        else:
            print("Your guess isn't quite right, try again.")