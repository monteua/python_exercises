def print_hor():
    print " --- " * board_size

def print_vert():
    print "|    " * (board_size+1)

if __name__ == '__main__':
    board_size = int(raw_input("Enter the board size: "))

    for i in range(int(board_size)):
        print_hor()
        print_vert()
    print_hor()