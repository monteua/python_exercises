def compare():
    ordered_list = [1, 5, 6, 8, 10, 255, 512, 556, 1256, 8569]

    user_number = raw_input("Enter a number: ")

    try:
        user_number = int(user_number)

        if user_number in ordered_list:
            print "In the list."
        else:
            print "Not in the list. Try again."

    except:
        print "Not a number."


def binary_search():
    ordered_list = [1, 5, 6, 8, 10, 255, 512, 556, 1256, 8569]
    user_number = raw_input("Enter a number: ")
    list_len = len(ordered_list) // 2
    #new_list = list()

    if int(user_number) < ordered_list[list_len]:
        new_list = ordered_list[0:list_len]
    elif user_number > ordered_list[list_len]:
        new_list = ordered_list[list_len:len(ordered_list)]
    #print new_list
    for x in new_list:
        if x == int(user_number):
            print "In the list."
            break
        else:
            print 'Not in list'
if __name__ == "__main__":
    choice = raw_input("Regular or binary search? ")
    choice = choice.lower()

    if str(choice) == 'regular' or str(choice) == 'r':
        compare()
    elif str(choice) == 'binary' or str(choice) == 'b':
        binary_search()
    else:
        print "Make the correct choice."
