#this is a tic-tac-toe game of two players and a 3x3 table
#this is an expansion of a project of the book ATBSWP

import numpy as np
import function

player_x=0
player_o=0

#we define a function that maps all the table to see if any of the players have won
table=np.array([[" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "]])
new_table=table.copy()
#first we make the table to play both players
print("Welcome to my tic-tac-toe game. Enjoy playing :)")
print("Use row from 0 to 2, and column from 0 to 2. Ex.: 2-1. First the row, and then the column.")
print("Enjoy")
#explanation of how to write the place to place your choice
i=9
current_winner=(0, 0)
print(table)
while i>0:
    if i%2==0:
        turn="X"
        print("X, where do you want to place?")
    else:
        turn="O"
        print("O, where do you want to place?")
    try:
        enter=list(map(int, input().split("-")))
    except ValueError:
        print(f"Player X have won {player_x} time(s) and player O {player_o} time(s)")
        break
    if table[enter[0]][enter[1]]!=" ":
        print("This site is taken. Enter one that is empty.")
        continue
        #if you introduce a place that is taken you can enter another place
        #and this dont make any negative consecuence on the player
    else:
        table[enter[0]][enter[1]]=turn
    print(table)
    function.winner(table)
    if function.winner(table)!=current_winner:
        n=0
        for x, o in zip(current_winner, function.winner(table)):
            if x!=o and n==0:
                player_x+=1
                print(f"Player X have won {player_x} time(s)")
                print("\U0001f600")
                table=new_table
                i=10
                continue
            elif x!=o and n==1:
                player_o+=1
                print(f"Player O have won {player_o} time(s)")
                print("\U0001f600")
                table=new_table
                i=10
                continue
            n+=1
    current_winner=function.winner(table)
    i-=1
    if i==0:
        i=9
        print("-----TIE----")
        table=new_table
