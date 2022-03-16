#Code by Matt Cadel

#Import Libraries
import numpy as np

#Creating the blank boards
Board = np.zeros([3,3])   #Board used for scoring
string = np.array(["_","_","_","_","_","_","_","_","_"]).reshape((3,3))    #Board used as display board

#While loop continues running until there is a winner
win=0  
while win==0:
    print("The board as it currently stands: \n")
    print(string)
    print("\nIt's X's turn!")
    clear = 0
    while clear == 0:
        #X's Turn - Row Selection - must play a non-charcter, and must be within limits of the board
        try:
            Xrow = abs(int(input("Which row would you like to play?: ")))
            while abs(Xrow) >2:
                print("You can't play that, how big do you think the board is!!")
                Xrow = abs(int(input("\nEnter the row would you like to play (normal board size this time): ")))
        except ValueError:
            print("You have tried entering a character, please try again!\n")
            while abs(Xrow) >2:
                Xrow = abs(int(input("Enter the row would you like to play (non-character value this time): ")))
        
        #X's Turn - Column Selection - must play a non-charcter, and must be within limits of the board
        try:
            Xcolumn = abs(int(input("Which column would you like to play?: ")))
            while abs(Xcolumn) >2:
                print("You can't play that, how big do you think the board is!!")
                Xcolumn = abs(int(input("\nEnter the column would you like to play (normal board size this time): ")))
        except ValueError:
            print("You have tried entering a character, please try again!\n")
            while abs(Xcolumn) >2:
                Xcolumn = abs(int(input("Enter the column would you like to play (non-character value this time): ")))
        
        #This evaluates whether X or O has already played in the spot selected. Will only pass if the place is free.
        if Board[Xrow,Xcolumn] == 0:
            clear=1
        elif Board[Xrow,Xcolumn] == 1:
            print("\nYou have already played here! Have another go at playing")
        else:
            print("\nO has already played here! Have another go at playing")
    
    #X board position updated
    Board[Xrow,Xcolumn] = 1
    
    #X's Turn - Turn is registered in visual using loop, then code evaluates whether X has won or not
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
    clear = 0
    while clear == 0:
        #O's Turn - Row Selection - must play a non-charcter, and must be within limits of the board
        try:
            Orow = abs(int(input("Which row would you like to play?: ")))
            while abs(Orow) >2:
                print("You can't play that, how big do you think the board is!!")
                Orow = abs(int(input("\nEnter the row would you like to play (normal board size this time): ")))
        except ValueError:
            print("You have tried entering a character, please try again!\n")
            while abs(Orow) >2:
                Orow = abs(int(input("Enter the row would you like to play (non-character value this time): ")))
        
        #O's Turn - Column Selection - must play a non-charcter, and must be within limits of the board
        try:
            Ocolumn = abs(int(input("Which column would you like to play?: ")))
            while abs(Ocolumn) >2:
                print("You can't play that, how big do you think the board is!!")
                Ocolumn = abs(int(input("\nEnter the column would you like to play (normal board size this time): ")))
        except ValueError:
            print("You have tried entering a character, please try again!\n")
            while abs(Ocolumn) >2:
                Ocolumn = abs(int(input("Enter the column would you like to play (non-character value this time): ")))
        
        #This evaluates whether X or O has already played in the spot selected. Will only pass if the place is free.
        if Board[Orow,Ocolumn] == 0:
            clear=1
        elif Board[Orow,Ocolumn] == -1:
            print("\nYou have already played here! Have another go at playing")
        else:
            print("\nX has already played here! Have another go at playing")
    
    #O board position updated
    Board[Orow,Ocolumn] = -1
    
    #X's Turn - Turn is registered in visual using loop, then code evaluates whether X has won or not
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
