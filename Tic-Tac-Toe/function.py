#to be cleaner, I prefer to set the function in another script

def winner(tab):
    win_player_x=0
    win_player_o=0
    #we define the times each player win a game
    if tab[0][0]==tab[0][1]==tab[0][2]:
        if tab[0][0]=="X":
            win_player_x+=1
        elif tab[0][0]=="O":
            win_player_o+=1
    elif tab[1][0]==tab[1][1]==tab[1][2]:
        if tab[1][0]=="X":
            win_player_x+=1
        elif tab[1][0]=="O":
            win_player_o+=1
    elif tab[2][0]==tab[2][1]==tab[2][2]:
        if tab[2][0]=="X":
            win_player_x+=1
        elif tab[2][0]=="O":
            win_player_o+=1
    elif tab[0][0]==tab[1][0]==tab[2][0]:
        if tab[0][0]=="X":
            win_player_x+=1
        elif tab[0][0]=="O":
            win_player_o+=1
    elif tab[0][1]==tab[1][1]==tab[2][1]:
        if tab[0][1]=="X":
            win_player_x+=1
        elif tab[0][1]=="O":
            win_player_o+=1
    elif tab[0][2]==tab[1][2]==tab[2][2]:
        if tab[0][2]=="X":
            win_player_x+=1
        elif tab[0][2]=="O":
           win_player_o+=1
    elif tab[0][0]==tab[1][1]==tab[2][2]:
        if tab[0][0]=="X":
            win_player_x+=1
        elif tab[0][0]=="O":
           win_player_o+=1
    elif tab[0][2]==tab[1][1]==tab[2][0]:
        if tab[0][2]=="X":
            win_player_x+=1
        elif tab[0][2]=="O":
            win_player_o+=1
    return win_player_x, win_player_o