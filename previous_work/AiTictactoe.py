#!/usr/bin/python3
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
count = 0
print(f"{board[6]}|{board[7]}|{board[8]}")
print("------")
print(f"{board[3]}|{board[4]}|{board[5]}")
print("------")
print(f"{board[0]}|{board[1]}|{board[2]}")
        
# print(len(board))
inputs = []

with open("log.txt" , "r") as f:
    log = f.read().splitlines()
with open("allMoves.txt" , 'r') as f:
    com_list = f.read().splitlines()
p1 = log[0].split(":")[1]
p2 = log[1].split(":")[1]
com = com_list[0]
while count < 9:
    if count%2 == 0:
        inp = int(input("place: "))
        inp = inp -1
        if board[inp] == ' ':
            board[inp] = "X"
            inputs.append(inp)
            # prediction = pred(inputs)

            if (board[6] == board[7] == board[8] == "X") or (board[3] == board[4] == board[5] == "X") or (board[0] == board[1] == board[2] == "X") or (board[6] == board[3] == board[0] == "X") or (board[7] == board[4] == board[1] == "X") or (board[8] == board[5] == board[2] == "X") or (board[6] == board[4] == board[2] == "X") or (board[0] == board[4] == board[8] == "X"):
                print("player 1 won")
                with open("log.txt" , "a") as f:
                    # log[0].split(":")[1] = int(log[0].split(":")[1]) + 1
                    f.write(f"player1:{str(int(p1)+1)}\n{log[1]}\n")
                break

    elif count%2 == 1:
        inp = int(com[count])
        if board[inp] == ' ':
            board[inp] = "O"
            inputs.append(inp)
            # prediction = pred(inputs)
            if (board[6] == board[7] == board[8] == "O") or (board[3] == board[4] == board[5] == "O") or (board[0] == board[1] == board[2] == "O") or (board[6] == board[3] == board[0] == "O") or (board[7] == board[4] == board[1] == "O") or (board[8] == board[5] == board[2] == "O") or (board[6] == board[4] == board[2] == "O") or (board[0] == board[4] == board[8] == "O"):
                print("player 2 won")
                with open("log.txt" , "a") as f:
                    # log[1].split(":")[1] = int(log[1].split(":")[1]) + 1
                    f.write(f"{log[0]}\nplayer2:{str(int(p2)+1)}\n")
                break
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print("------")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("------")
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print(inputs)
    # print(prediction)
    count = count + 1
else:
    print("Invalid")