# tic tac toe
# version 1
# Name: ahmed shaaban ahmed
# ID: 20210022


# Display board on screen.


def display_board():
    global board
    # board 3X3
    columns = 3
    rows = 3
    board = [['' for i in range(columns)] for j in range(rows)]  # 3list
    # print  board 3X3
    for i in range(3):
        print(board[i])


# show who is playing
def user_input(turn):
    global p1turn, p2turn, row, colunm, list1, list2
    # list of player1
    if turn == 0:
        list1 = [1, 3, 5, 7, 9]
    if turn % 2 == 0:
        print("Player 1 Turn: ")
        while True:

            while True:
                # try to avoid input error
                try:
                    p1turn = int(input("Enter odd number: "))
                    break
                except:
                    print("Entre numbers only")
                    continue
            if p1turn not in list1:
                print("enter odd number between 0-9, do not repeat the number")
                continue
            else:
                list1.remove(p1turn)
                break
    # list of player2
    if turn == 0:
        list2 = [0, 2, 4, 6, 8]
    if turn % 2 == 1:
        print("Player 2 Turn: ")
        while True:
            while True:
                try:
                    p2turn = int(input("Enter even number: "))
                    break
                except:
                    print("Entre numbers only")
                    continue
            if p2turn not in list2:
                print("enter even number between 0-8, do not repeat the number")
                continue
            else:
                list2.remove(p2turn)
                break
    # Rows and Columns
    while True:
        while True:
            try:
                row = int(input("Enter number of row: "))
                break
            except:
                print(" Entre numbers only")
                continue
        while True:
            try:
                colunm = int(input("Enter number of colunm: "))
                break
            except:
                print(" Entre numbers only")
                continue

        if row > 3 or row < 1 or colunm > 3 or colunm < 1:
            print(" please enter row and colunm between1-3")
            continue
            # place is full or no
        else:
            if board[row - 1][colunm - 1] != '':
                print("choose another place")
                continue
            else:
                break


# update bourd after every turn
def uptade(row, colunm, i):
    row = row - 1
    colunm = colunm - 1
    if i % 2 == 0:
        board[row][colunm] = p1turn
    if i % 2 == 1:
        board[row][colunm] = p2turn
    for i in range(3):
        print(board[i])


# Check win
def check():
    global counter
    counter = 0
    for i in range(0, 2):
        try:
            if board[i][0] + board[i][1] + board[i][2] == 15:  # Check Rows
                counter = 1
        except:
            pass
        try:
            if board[0][i] + board[1][i] + board[2][i] == 15:  # Check Columns
                counter = 1
        except:
            pass
        try:
            if board[0][0] + board[1][1] + board[2][2] == 15:
                counter = 1
        except:
            pass
        try:
            if board[0][2] + board[1][1] + board[2][0] == 15:
                counter = 1
        except:
            pass


display_board()
for i in range(50):
    if i == 0:
        y = 0

    user_input(i)
    y += 1
    uptade(row, colunm, i)
    check()
    if counter == 1:
        if i % 2 == 0:
            print("Player 1 Win!")
            break
        if i % 2 == 1:
            print("Player 2 Win!")
            break
    if y == 9:
        print("Draw!")
        break

