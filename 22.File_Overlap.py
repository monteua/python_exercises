file1 = open('primenumbers.txt', 'r')
file2 = open('happynumbers.txt', 'r')

file1_list = []
file2_list = []

line1 = file1.readline()
line2 = file2.readline()

while line1:
    line1 = line1.strip()
    file1_list.append(line1)
    #print "Appended: ", line1
    line1 = file1.readline()
while line2:
    line2 = line2.strip()
    file2_list.append(line2)
    #print "Appended: ", line2
    line2 = file2.readline()

for num1 in file1_list:
    for num2 in file2_list:
        if num1 == num2:
            print "Number", num1, ' is in two files'