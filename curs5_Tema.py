# TIC TAC TOE human vs robot
state_of_game = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def draw_state_of_game():
    """
    just print the current state of the game
    """
    global state_of_game
    print(f"{state_of_game[1]}|{state_of_game[2]}|{state_of_game[3]}")
    print(f"{state_of_game[4]}|{state_of_game[5]}|{state_of_game[6]}")
    print(f"{state_of_game[7]}|{state_of_game[8]}|{state_of_game[9]}")


def human():
    """
    :return: return False if the move cannot be made
             return True and change the state of the game if the move can be made
    """
    global state_of_game
    move = input("Make your move! Enter a number between 1-9: ")
    if int(move) < 1 or int(move) > 9 or not move.isdigit():
        return False
    elif not state_of_game[int(move)].isdigit():
        return False
    else:
        state_of_game[int(move)] = "X"
        return True


def robot():
    """
    modify the state of the game accordingly to
    the first position open
    """
    global state_of_game
    move = 0
    if state_of_game[5].isdigit():
        move = 5
    elif state_of_game[1].isdigit():
        move = 1
    elif state_of_game[3].isdigit():
        move = 3
    elif state_of_game[7].isdigit():
        move = 7
    elif state_of_game[9].isdigit():
        move = 9
    elif state_of_game[2].isdigit():
        move = 2
    elif state_of_game[4].isdigit():
        move = 4
    elif state_of_game[6].isdigit():
        move = 6
    elif state_of_game[8].isdigit():
        move = 8
    state_of_game[move] = "O"


def check_if_won():
    """
    :return: 1 if the game was won by human
             2 if the game was won by robot
             3 if the game isn't won yet
    """
    global state_of_game

    if state_of_game[1] == state_of_game[2] == state_of_game[3] == "X":
        return 1
    elif state_of_game[1] == state_of_game[4] == state_of_game[7] == "X":
        return 1
    elif state_of_game[3] == state_of_game[5] == state_of_game[7] == "X":
        return 1
    elif state_of_game[7] == state_of_game[8] == state_of_game[9] == "X":
        return 1
    elif state_of_game[3] == state_of_game[6] == state_of_game[9] == "X":
        return 1
    elif state_of_game[2] == state_of_game[5] == state_of_game[8] == "X":
        return 1

    elif state_of_game[1] == state_of_game[2] == state_of_game[3] == "O":
        return 2
    elif state_of_game[1] == state_of_game[4] == state_of_game[7] == "O":
        return 2
    elif state_of_game[3] == state_of_game[5] == state_of_game[7] == "O":
        return 2
    elif state_of_game[7] == state_of_game[8] == state_of_game[9] == "O":
        return 2
    elif state_of_game[3] == state_of_game[6] == state_of_game[9] == "O":
        return 2
    elif state_of_game[1] == state_of_game[5] == state_of_game[9] == "O":
        return 2
    elif state_of_game[2] == state_of_game[5] == state_of_game[8] == "O":
        return 2

    else:
        return 3


while check_if_won() == 3:
    if human():
        draw_state_of_game()
        print()
        if check_if_won() == 1:
            print("Felicitari!")
            break
        
        robot()
        draw_state_of_game()
        print()
        if check_if_won() == 2:
            print("Ati pierdut! :(")
            break
    else:
        draw_state_of_game()
        print("Try Again!")
