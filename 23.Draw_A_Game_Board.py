l = " --- "
p = "|    "

def get_size():
    board_size = raw_input("3*3, 8*8, 19*19? ")
    return board_size

def tic_tac_toe():
    for i in range(3):
        print l * 3, '\n', p*4
    print l*3

def chess():
    for i in range(8):
        print l * 8, '\n', p*9
    print l*8

def go():
    for i in range(19):
        print l*19, '\n', p*20
    print l*19

def start():
    board_size = get_size()

    if board_size == "3*3":
        tic_tac_toe()
    elif board_size == '8*8':
        chess()
    elif board_size == '19*19':
        go()

start()