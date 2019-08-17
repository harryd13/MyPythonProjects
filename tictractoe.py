from IPython.display import clear_output

def display_board(board):
    clear_output()
    print("\t\t|\t\t|\t\t\n")
    print(f"\t{board[7]}\t|\t{board[8]}\t|\t{board[9]}\t\n")
    print("\t\t|\t\t|\t\t\n")
    print("------------------------------------------------\n")
    print("\t\t|\t\t|\t\t\n")
    print(f"\t{board[4]}\t|\t{board[5]}\t|\t{board[6]}\t\n")
    print("\t\t|\t\t|\t\t\n")
    print("------------------------------------------------\n")
    print("\t\t|\t\t|\t\t\n")
    print(f"\t{board[1]}\t|\t{board[2]}\t|\t{board[3]}\t\n")
    print("\t\t|\t\t|\t\t\n")
    
def player_input():
    marker = ''
    while marker != 'X' and marker != 'O' : 
        marker = input("Player ,you want X or O ?").upper()
        if(marker != 'X' and marker != 'O'):
            print('please enter only X or O')
    
    if marker == 'X':
        player1_marker = "X"
        player2_marker = "O"
    else :
        player1_marker = "O"
        player2_marker = "X"
    
    return (player1_marker, player2_marker)
    
def place_marker(board, marker, position):
    while position > 10  and position < 1 :
        position = int(input("Enter the position of your move "))
    board[position] = marker


def win_check(board, mark):
    val = 0
    if(board[1] == board[2] == board[3] == mark or board[4] == board[5]==board[6]==mark or board[7]==board[8]==board[9]==mark):
        val = 1
    if(board[1] == board[4] == board[7] == mark or board[2] == board[5]==board[8]==mark or board[3]==board[6]==board[9]==mark):
        val = 1
    if(board[7] == board[5] == board[3] == mark or board[1] == board[5]==board[9]==mark):
        val = 1
    if(val == 1):
        return True
    else:
        return False


import random

def choose_first():
    x = random.randint(1,2)
    if(x == 1):
        print("player1 goes first\n")
        return 1
    else:
        print("player2 goes first\n")
        return 2

def space_check(board, position):
    if(board[position] != 'X' and board[position] != 'O'):
        return True
    else:
        return False

        

def full_board_check(board):
    
    cnt = 0
    for place in board:
        if place == "X" or place  == 'O':
            cnt = cnt + 1
    
    if(cnt == 9):
        return True
    else:
        return False


def player_choice(board):
    pos = int(input("please enter the position:"))
    if(space_check(board,pos)):
        return pos
    else:
        return -1

def replay():
    ans  = ''
    while(ans != 'yes' and ans != 'no'):
        ans = input("Do you want to play again? (yes or no)")
    if(ans == 'yes'):
        return True
    else :
        return False


play = True
print("Welcome to Tic Tac Toe!")

while play :
    board = ['#','1','2','3','4','5','6','7','8','9']
    display_board(board)
    startinig_player = choose_first()
    if(startinig_player == 1):
        (player1_mark,player2_mark) = player_input()
    else:
        (player2_mark,player1_mark) = player_input()
        
    print(player1_mark)
    print(player2_mark)
    
    #pass
    tie = 0
    c = 0
    if(startinig_player == 1):
        while (full_board_check(board) == False):
            c += 1
            print(c)
            #Player 1 Turn
            print("player1 turn\n")
            position = player_choice(board)
            while -1 < position <= 0 or position < -1:
                position = player_choice(board)
            if(position == -1):
                break
            place_marker(board,player1_mark,position)
            display_board(board)
            if(win_check(board,player1_mark)):
                print("CNOGRATS!! player1 wins\n")
                tie = 1
                break
            
            
        
            # Player2's turn.
            print("player2 turn\n")
            position = player_choice(board)
            while -1 < position <= 0 or position < -1:
                position = player_choice(board)
            if(position == -1):
                break
            place_marker(board,player2_mark,position)
            display_board(board)
            if(win_check(board,player2_mark)):
                print("CNOGRATS!! player2 wins\n")
                tie = 1
                break
            
    else:
        while full_board_check(board) == False:
            c += 1
            print(c)
            # Player2's turn.
            print("player2 turn\n")
            position = player_choice(board)
            while -1 < position <= 0 or position < -1:
                position = player_choice(board)
            if(position == -1):
                break
            place_marker(board,player2_mark,position)
            display_board(board)
            if(win_check(board,player2_mark)):
                print("CNOGRATS!! player2 wins\n")
                tie = 1
                break    
            #Player 1 Turn
            print("player1 turn\n")
            position = player_choice(board)
            while -1 < position <= 0 or position < -1:
                position = player_choice(board)
            if(position == -1):
                break
            place_marker(board,player1_mark,position)
            display_board(board)
            if(win_check(board,player1_mark)):
                print("CNOGRATS!! player1 wins\n")
                tie = 1
                break
           
        
    if(tie == 0):
        print('oops! match tied')
    play = replay()
    