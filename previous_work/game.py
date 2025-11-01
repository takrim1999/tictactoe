with open("work.txt","r") as f:
    array = [i for i in f.read().strip().split("\n")]

def find_next_step(sub_array,full_array):
    for i in full_array:
        if sub_array == i.split()[:len(sub_array)]:
            element = i.split()
            break
    print("terminator's move " + str(element))
    return element[len(sub_array)]

def terminate(sub_array,full_array):
    to_remove = []
    print(sub_array)
    sub_array = sub_array[:-1]
    print(sub_array)
    for i in full_array:
        if sub_array == i.split()[:len(sub_array)]:
            to_remove.append(i)
    for j in to_remove:
        print("removing " + str(j))    
        full_array.remove(j)
    with open("work.txt","w") as f:
        for i in full_array:
            f.write(i+"\n")


def print_board(board):
    print(f"{board[6]} | {board[7]} | {board[8]} \n---------\n{board[3]} | {board[4]} | {board[5]} \n---------\n{board[0]} | {board[1]} | {board[2]}")
    return f"{board[6]} | {board[7]} | {board[8]} \n---------\n{board[3]} | {board[4]} | {board[5]} \n---------\n{board[0]} | {board[1]} | {board[2]}"
    
def result(board,moves,array):
    if (board[0] == board[1] == board[2] == 'X') or (board[3] == board[4] == board[5] == 'X') or (board[6] == board[7] == board[8] == 'X') or (board[0] == board[4] == board[8] == 'X') or (board[2] == board[4] == board[6] == 'X') or (board[0] == board[3] == board[6] == 'X') or (board[1] == board[4] == board[7] == 'X') or (board[2] == board[5] == board[8] == 'X'):
        with open("log.txt","a") as f:
            f.write(print_board(board))
            f.write("\nPlayer wins\n")
        # print_board(board)
        terminate(moves,array)
        print("Player wins")
        return 1
    elif (board[0] == board[1] == board[2] == 'O') or (board[3] == board[4] == board[5] == 'O') or (board[6] == board[7] == board[8] == 'O') or (board[0] == board[4] == board[8] == 'O') or (board[2] == board[4] == board[6] == 'O') or (board[0] == board[3] == board[6] == 'O') or (board[1] == board[4] == board[7] == 'O') or (board[2] == board[5] == board[8] == 'O'):
        with open("log.txt","a") as f:
            f.write(print_board(board))
            f.write("\nTerminator wins\n")
        # print_board(board)
        print("Terminator wins")
        return 2
    else:
        if ' ' not in board:
            with open("log.txt","a") as f:
                f.write(print_board(board))
                f.write("\nDraw\n")
            # print_board(board)
            print("Draw")
            return 0
        else:
            return None
 
move_list = []
board = [' ']*9 
# print_board(board)

while result(board,move_list,array) == None:
    print_board(board)
    if len(move_list) % 2 == 0:
        turn = int(input("Human's Turn: ")) - 1
        if board[turn] == ' ':
            board[turn] = 'X'
            move_list.append(str(turn))
        else:
            print("Invalid Turn, Try again")
    elif len(move_list) % 2 == 1:
        # turn = int(input("Terminator's Turn: ")) - 1
        turn = int(find_next_step(move_list,array))
        if board[turn] == ' ':
            board[turn] = 'O'
            move_list.append(str(turn))
        else:
            print("Invalid Turn, Try again")
    print(move_list)