def user_input():
    user_string = raw_input("Enter the string: ")
    if len(user_string) < 1:
        user_string = "My name is Michele"
    return user_string

def reversed():

    user_string = user_input()
    string_list = user_string.split(" ")
    print string_list[::-1]

reversed()