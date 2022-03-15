import numpy as np

Board = np.zeros([3,3])
string = np.array(["_","_","_","_","_","_","_","_","_"]).reshape((3,3))

win=0  
while win==0:
    print("The board as it currently stands: \n")
    print(string)
    print("\nIt's X's turn!")
    Xrow = int(input("Which row would you like to play?: "))
    Xcolumn = int(input("Which column would you like to play?: "))
    Board[Xrow,Xcolumn] = 1
    for x in range(3):
        for y in range(3):
            if Board[x,y] == 1:
                string[x,y] = "X"
            elif Board[x,y] == -1:
                string[x,y] = "O"
    for n in range(2):
            for m in range(3):
                total = np.sum(Board,axis=n)[m]
                if total == 3:
                    print("\nX Wins!")
                    win=1
    if Board[0,0]+Board[1,1]+Board[2,2] ==3 or Board[2,0]+Board[1,1]+Board[0,2] ==3:
        print("\nX Wins!")
        win=1
    if win==1:
        break
    print("The board as it currently stands: \n")
    print(string)
    print("\nIt's O's turn!")
    Orow = int(input("Which row would you like to play?: "))
    Ocolumn = int(input("Which column would you like to play?: "))
    Board[Orow,Ocolumn] = -1
    for x in range(3):
        for y in range(3):
            if Board[x,y] == 1:
                string[x,y] = "X"
            elif Board[x,y] == -1:
                string[x,y] = "O"
    for n in range(2):
            for m in range(3):
                total = np.sum(Board,axis=n)[m]
                if total == -3:
                    print("\nO Wins!")
                    win=1
    if Board[0,0]+Board[1,1]+Board[2,2] ==-3 or Board[2,0]+Board[1,1]+Board[0,2] ==-3:
        print("\nO Wins!")
        win=1
    if win==1:
        break
                
            


# while np.sum(x_board,axis=0) <=2 and np.sum(x_board,axis=1) <=2 and np.sum(x_board,axis=2) <=2:
#     row = int(input("Which row: "))
#     column = int(input("Which column: "))
#     x_board[row,column] = 1

# print(x_board)

# for x,y in range(3):
#     if x_board[x,y] == 1:
#         x_board[x,y] ==