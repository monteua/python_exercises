import random

myfile = open('sowpods.txt', 'r')
lines = myfile.readlines()
def random_word():
    print random.choice(lines).strip()

random_word()