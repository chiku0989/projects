from IPython.display import clear_output


#UserDefine Functions
#Welcome funtion
def welcome():
    print("********WELCOME TO THE TIC TOE GAME********")
    print("This is a two player game")
    print("Both the players can play from the same device")
    print("Please consider the following gamepad as a reference")
    print('     |     |     ')
    print(f'  {" "}  |  {" "}  |  {" "}  ')
    print('     |     |     ')
    print('-----|-----|-----')
    print('     |     |     ')
    print(f'  {" "}  |  {" "}  |  {" "}  ')
    print('     |     |     ')
    print('-----|-----|-----')
    print('     |     |     ')
    print(f'  {" "}  |  {" "}  |  {" "}  ')

#Printing board function
def printBoard(rows):
    print('     |     |     ')
    print(f'  {rows[0][0]}  |  {rows[0][1]}  |  {rows[0][2]}  ')
    print('     |     |     ')
    print('-----|-----|-----')
    print('     |     |     ')
    print(f'  {rows[1][0]}  |  {rows[1][1]}  |  {rows[1][2]}  ')
    print('     |     |     ')
    print('-----|-----|-----')
    print('     |     |     ')
    print(f'  {rows[2][0]}  |  {rows[2][1]}  |  {rows[2][2]}  ')
    print('     |     |     ')
    
#Function to take input
def takeInp():
    row = 'hello'
    col = 'hello'
    validRange = False
    while validRange == False:
        row = input("enter row(1-3): ")
        if row.isdigit() and int(row) in range(1,4):
            col = input(f"select cell in row {row} (1-3): ")
            if col.isdigit() and int(col) in range(1,4):
                return int(row)-1, int(col)-1
            else:
                print("Invalid input, Try again!")
        else:
            print('Invalid Input Please try again')

#Function to choose X or O
def chooseXorO():
    player1 =' '
    while player1 not in ('X','O'):
        player1 = input("Choose X or O: ")
        if player1 == 'X':
            player2 = 'O'
            return player1,player2
        elif player1 == 'O':
            player2 = 'X'
            return player1,player2
        else:
            print('Invalid Option try again!')

#Function to determine current Player
def currentPlayer(player1,player2,alt):
    if alt%2 == 0:
        return player1
    else:
        return player2


#Function to determine who is the winner
def checkWin(board, player_sign):
    # Check rows
    for row in board:
        if all(cell == player_sign for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(row[col] == player_sign for row in board):
            return True

    # Check diagonals
    if all(board[i][i] == player_sign for i in range(3)) or \
       all(board[i][2-i] == player_sign for i in range(3)):
        return True

    return False


#Function to Check for Draw
def checkDraw(rows):
    for row in rows:
        for cell in row:
            if cell == ' ':
                return False
    return True


#Function to check if player wants to cotinue the game 
def gameOn():
    choice  = 'Hello'
    while choice not in ('Y','N'):
        choice = input('Do you want to play agian? (Y or N): ')
        if choice == "Y":
            return True 
        elif choice == "N":
            return False
        else:
            print("Sorry I dont understand Please try again?")


#Main Function
def TicTacToe():
    #variables 
    
    gameon = True
    
    #game on
    while gameon:
        rows = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        alt = 0
        pos = False
        draw = False
        win = False
        
        welcome()
        
        player1,player2 = chooseXorO()
        
        while draw == False or win == False:
            
            cp = currentPlayer(player1,player2,alt)
            
            alt+=1
            print(f"{cp}\'s turn")
            
            pos =False
            while pos ==False:
                row,col=takeInp()
                if rows[row][col] == ' ':
                    rows[row][col] = cp
                    pos = True
                else:
                    print('That cell is already taken, please try again!')
                    
                    
            printBoard(rows)
            win = checkWin(rows,cp)
            if win == False:
                draw = checkDraw(rows)
                if draw == True:
                    print("Game Over!")
                    gameon = gameOn()
                    break
            if win == True:
                print(f"Congratulations {cp} won!")
                gameon = gameOn()
                break


TicTacToe();