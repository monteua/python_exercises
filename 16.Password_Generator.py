import random
fhand = open("rand_words.txt", mode="r")
words = ["pass", "password", "admin"]

for word in fhand:
    word = word.strip()
    words.append(word)
#print words
numbers = []

def get_level_of_password():
    for number in range(10):
        num = random.randint(0, 99)
        numbers.append(num)
    print "what password you need?"
    print "1. Weak 2. Medium 3.Strong"
    user_input = raw_input("> ")

    if user_input == "1" or user_input.lower() == "weak":
        return 1
    elif user_input == "2" or user_input.lower() == "medium":
        return 2
    elif user_input == "3" or user_input.lower() == "strong":
        return 3
    else:
        print "Please make the correct choice!"
        exit(0)




def generate_password():
    #get_level_of_password()
    #print get_level_of_password()
    #print numbers
    level_of_pass = get_level_of_password()
    if level_of_pass == 1:
        generated_password = random.choice(words)

    elif level_of_pass == 2:
        generated_password = str(random.choice(numbers)) + str(random.choice(words)) + str(random.choice(numbers))
    elif level_of_pass == 3:
        generated_password = str(random.choice(words)).title() + str(random.choice(numbers)) \
                             + str(random.choice(words)).title() + str(random.choice(numbers))
    lenght = 16 - len(generated_password)
    generated_password = generated_password[:16]
    print "You new password is \n" + str(generated_password)

generate_password()