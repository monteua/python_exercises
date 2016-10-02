file_name = open('Training_01.txt', 'r')

line = file_name.readline()

dict = {}

while line:

    cat = line.split('/')
    if cat[2] not in dict:
        dict[cat[2]] = 1
    else:
        dict[cat[2]] += 1

    line = file_name.readline()

for key in dict.items():
    print key[0], ": ", key[1]

