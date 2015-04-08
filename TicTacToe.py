__author__ = 'atma6951'
# Print welcome
print("Welcome to TicTacToe game")

#set up game data structure
x = 1
o = -1
e = 0  #empty
game = [[e, e, e],
        [e, e, e],
        [e, e, e]]

#region print the board
def printBoard(gameboard):
    for outerloopE in gameboard:
        for innerloopE in outerloopE:
            var = ""
            if innerloopE == e:
                var = "."
            elif innerloopE == o:
                var = "o"
            else:
                var = "x"
            print(var, end=" ")
        print("\n")


#endregion

#region check winner or impasse
def checkwinner(game):
    #count rows
    for rowloop in game:
        if (sum(rowloop) == 3):
            return "x"
        elif (sum(rowloop) == -3):
            return "o"
    #count cols
    for colloop in range(len(game)):
        if (game[0][colloop] + game[1][colloop] + game[2][colloop]) == 3:
            return "x"
        elif (game[0][colloop] + game[1][colloop] + game[2][colloop]) == -3:
            return "o"
    #count diagonal
    if (game[0][0] + game[1][1] + game[2][2]) == 3:
        return "x"
    elif (game[0][0] + game[1][1] + game[2][2]) == -3:
        return "o"
    elif (game[0][2] + game[1][1] + game[2][0]) == 3:
        return "x"
    elif (game[0][2] + game[1][1] + game[2][0]) == -3:
        return "o"

    #nobody won
    return ""

def isImpasse(game):
    for rows in game:
        if e in rows:
            return False #still scope to play
    return True
#endregion

#region loop game until win
def loopgame():
    turn = "x"  #x starts first
    winner = ""
    while (not winner):
        print("{}'s turn".format(turn))
        #get row and col of input
        row = int(input("Enter row number of your entry: "))
        col = int(input("Enter col number of your entry: "))
        if (row in [0, 1, 2]) and (col in [0, 1, 2]):
            if game[row][col] == e:
                game[row][col] = x if turn == "x" else o
            else:
                print("Value not empty")
                printBoard(game)
                continue
        else:
            print("Index out of bounds. Try values between 0 - 2")
            continue
        #evaluate if someone has won
        print()
        printBoard(game)
        winner = checkwinner(game)
        if winner:
            print("{} has won!!!".format(winner))
            break

        #check if game has reached impasse
        if isImpasse(game):
            print("Game has reached an impasse. Lets end it")
            break
        #switch turn
        if turn == "x":
            turn = "o"
        else:
            turn = "x"
#endregion

if __name__ == "__main__":
    printBoard(game)
    loopgame()
