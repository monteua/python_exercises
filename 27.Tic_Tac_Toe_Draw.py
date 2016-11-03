game = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]

while True:
    user_input = map(int, raw_input("Enter the col,row").split(","))
    game[user_input[1]-1][user_input[0]-1] = "X"

    for i in range(len(game)):
        print game[i]
