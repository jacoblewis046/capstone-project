import numpy as np

def valid_input(text):
    while True:
        user_input = input(text)
        if user_input == "quit":
            print("Exiting connect 4...")
            quit()
        try:
            user_input = int(user_input)
            if user_input >= 1 and user_input <= 7:
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid input. Enter a number between 1 and 7 or type 'quit' to exit.")

    return user_input

        
def showboard(board):
    for y in board:
        for x in y:
            print(x,end=" ")
        print("")

def dropcounter(x, board):
    row = 5

    if board[0][x] != 0:
        return "error"
    
    for i,y in enumerate(board):
        if y[x] != 0:
            row = i-1
            break

    return row

def is_sublist(a, b):
    if len(a) > len(b):
        return False
    for i in range(0, len(b) - len(a) + 1):
        if b[i:i+len(a)] == a:
            return True
    return False

def winner3(board,y,x):
    player = board[y][x]
    connect4 = [player,player,player,player]
    
    x_subarray = board[y]
    if is_sublist(connect4, x_subarray):
        # print("x subarray")
        return True
    
    y_subarray = []
    for row in board:
        y_subarray.append(row[x])
    if is_sublist(connect4, y_subarray):
        # print("y subarray")
        return True

    diag_subarray = np.array(board).diagonal(x-y).tolist()
    if len(diag_subarray) >= 4:
        if is_sublist(connect4, diag_subarray):
            # print(f"diag subarray: {diag_subarray}")
            # print(connect4)
            # print(connect4 in diag_subarray)
            return True

    anti_diag_subarray = np.fliplr(np.array(board)).diagonal(6-x-y).tolist()
    if len(anti_diag_subarray) >= 4:    
        if is_sublist(connect4, anti_diag_subarray):
            # print("anti diag subarray")
            return True
    
    # for i in [x_subarray,y_subarray,diag_subarray,anti_diag_subarray]:
    #     print(i,connect4,is_sublist(connect4,i))

    return False



def turn(board, player):
    # print("The board as it stands: ")
    print("")
    print(f"Player {str(player)}, it's your turn. Enter keyword 'quit' to exit at any time.")
    
    while True:
        collumn = valid_input("Choose your collumn (1-7): ")
        collumn = int(collumn) - 1

        row = dropcounter(collumn, board)

        if row == "error":
            print("Error: That collumn is full. Try again.")
        else:
            board[row][collumn] = player
            break

    

    print("")
    print("The board as it stands: ")
    print("")
    showboard(board)

    if winner3(board,row,collumn):
        # print("You win !!")
        return f"Player {player} wins !!!!"


# def winner(board):
#     for yi, y in enumerate(board):
#         for xi, x in enumerate(y):
#             if x != 0:
#                 if board[xi][yi+1] == x and board[xi][yi+2] == x and board[xi][yi+3] == x:
#                     return x
#                 if board[xi][yi-1] == x and board[xi][yi-2] == x and board[xi][yi-3] == x:
#                     return x
                

            

print("""
      ********************************************
      ******** Welcome to connect 4 ! ************
      ********************************************
      """)


board = [
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
]

showboard(board)

while True:
    p1 = turn(board,1)
    if p1 != None:
        print(p1)
        break


    p2 = turn(board,2)
    if p2 != None:
        print(p2)
        break

    






