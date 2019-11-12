# # tictactoe
#import
import time
import os
from colorama import Fore
from colorama import Style


def intro():
    ##################################### Intro #################################
    #     print(f'''{Fore.YELLOW}
    # __________     ___.  ___.                  ________                 __    
    # \______   \__ _\_ |__\_ |__   ___________  \______ \  __ __   ____ |  | __
    #  |       _/  |  \ __ \| __ \_/ __ \_  __ \  |    |  \|  |  \_/ ___\|  |/ /
    #  |    |   \  |  / \_\ \ \_\ \  ___/|  | \/  |    `   \  |  /\  \___|    < 
    #  |____|_  /____/|___  /___  /\___  >__|    /_______  /____/  \___  >__|_  |
    #         \/          \/    \/     \/                \/            \/     \/
    #     {Style.RESET_ALL}''')
    #     time.sleep(2)                 #finalnie 2 sekundy
    #     os.system('clear')
    #     print("Presents:")
    #     time.sleep(2)
    #     os.system('clear')
    #     print('''
    # __ __|_)      __ __|          __ __|          
    #    |   |  __|    |  _` |  __|    |  _ \   _ \ 
    #    |   | (       | (   | (       | (   |  __/ 
    #   _|  _|\___|   _|\__,_|\___|   _|\___/ \___|   
    #     ''')
    #     time.sleep(2)
        print('''
        Possible moves: 1, 2, 3, 4, 5, 6, 7, 8, 9 ; try to fill a row!
        |¹|²|³|     =     1 | 2 | 3
        |⁴|⁵|⁶|     =     4 | 5 | 6
        |⁷|⁸|⁹|     =     7 | 8 | 9
        ''')




def printmove(player_move , board, char):    #print board and player move
    index = 0
    char = char
    player_move = player_move
    if player_move == 1:
        index = 1
    if player_move == 2:
        index = 3
    if player_move == 3:
        index = 5
    if player_move == 4:
        index = 9
    if player_move == 5:
        index = 11
    if player_move == 6:
        index = 13
    if player_move == 7:
        index = 17
    if player_move == 8:
        index = 19
    if player_move == 9:
        index = 21
    board = board[0:index] + char + board[index + 1:]
    print(board)
    return board    

def show_scores(player_one_wins, player_two_wins, name_first, name_second):
    os.system('clear')                                          
    if player_one_wins == 1:                                            #exception for one game won
        print(name_first, "won:" , player_one_wins , "game.")
    else:
        print(name_first, "won:" , player_one_wins , "games.")
    if player_two_wins == 1:                                            #exception for one game won
        print(name_second, "won:" , player_two_wins , "game.")
    else:
        print(name_second, "won:" , player_two_wins , "games.")
    print("\nThank you for playing! #rubberduck @ discord \n")
    print(f'''{Fore.YELLOW}
__________     ___.  ___.                  ________                 __    
\______   \__ _\_ |__\_ |__   ___________  \______ \  __ __   ____ |  | __
 |       _/  |  \ __ \| __ \_/ __ \_  __ \  |    |  \|  |  \_/ ___\|  |/ /
 |    |   \  |  / \_\ \ \_\ \  ___/|  | \/  |    `   \  |  /\  \___|    < 
 |____|_  /____/|___  /___  /\___  >__|    /_______  /____/  \___  >__|_  |
        \/          \/    \/     \/                \/            \/     \/
    {Style.RESET_ALL}''')


def game_loop():

        #declare variables
    board = "|¹|²|³|\n|⁴|⁵|⁶|\n|⁷|⁸|⁹|"
    char = ""
    playeronethinking = True
    possible_moves = [1,2,3,4,5,6,7,8,9]
    player_one_wins = 0
    player_two_wins = 0   
    player_one_moves = []
    player_two_moves = [] 
    player_one_name = input("Write first player name:")
    player_two_name = input("Write second player name:")
    wining_moves = [[1 , 2 , 3] , [4 , 5 , 6] , [7 , 8 , 9] , [1 , 5 , 9] ,
                    [ 7, 5, 3] , [1 , 4 , 7] , [2 , 5 , 8] , [3 , 6 , 9]]
    current_player=1
    endgame = False
    show_play_again=0

    # main game loop

    while endgame != True:
        if current_player==1:
            char = "X"
        elif current_player==2:
            char = "O"
        isCorrect = False
        while isCorrect == False:
            if current_player==1:
                player_move_str = input(f"{Fore.GREEN}{player_one_name} - please make your move:{Style.RESET_ALL}")
            elif current_player==2:
                player_move_str = input(f"{Fore.BLUE}{player_two_name} - please make your move:{Style.RESET_ALL}")
            try:
                player_move = int(player_move_str)
                possible_moves.index(player_move)
                possible_moves.remove(player_move)
                if current_player==1:
                    player_one_moves.append(player_move)
                elif current_player==2:
                    player_two_moves.append(player_move)
                isCorrect = True
            except ValueError:
                print("This is not a valid move!")
                
        print("\n")
        board= printmove(player_move , board , char)
        print("\n")

        if current_player==1:
            current_player=2
        elif current_player==2:
            current_player=1

        # playeronethinking = False                                   #variables for switching players
        # playertwothinking = True
        for x in range(0, 8):                                       #check for win condition
            list_0=list(set(wining_moves[x]).intersection(set(player_one_moves)))
            list_1=list(set(wining_moves[x]).intersection(set(player_two_moves)))
            if len(list_0) == 3:
                print(player_one_name, "Wins!")
                player_one_wins += 1
                show_play_again = True
            elif len(list_1) == 3:
                print(player_two_name, "Wins!")
                player_two_wins += 1
                show_play_again = True

        if show_play_again == True: 
            show_play_again = False
            
            play_again = input("Play again? (y/n)")
            if play_again == "y":
                print("Starting new game")
                possible_moves = [1,2,3,4,5,6,7,8,9]
                board = "|¹|²|³|\n|⁴|⁵|⁶|\n|⁷|⁸|⁹|"
                player_one_moves = []
                player_two_moves = []
                continue
            else:
                endgame = True
                    
        if not possible_moves:                          #check for tie
            print("It's a tie.")
            play_again = input("Play again? (y/n)")
            if play_again == "y":
                print("Starting new game")
                possible_moves = [1,2,3,4,5,6,7,8,9]
                board = "|¹|²|³|\n|⁴|⁵|⁶|\n|⁷|⁸|⁹|"
                player_one_moves = []
                player_two_moves = []
                continue
            else:
                endgame = True
    show_scores(player_one_wins, player_two_wins, player_one_name, player_two_name)


def main():                                               #main
    intro()                                               #show intro and initial board
    game_loop()
###########################endgame stats and credits##################################
    
    
main()