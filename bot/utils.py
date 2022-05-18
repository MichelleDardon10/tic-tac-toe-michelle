"""
[Module] Tic-tac-toe bot utilities.
"""
from random import randint
import requests
from urllib.parse import unquote


API_URL = "http://127.0.0.1:8000" 


def is_registry_open() -> bool:
    """
    Checks if registry is available via API.
    """
    try:
        url = "{}/registry".format(API_URL)
        res = requests.get(url)

        if res.text == "true":
            return True
        elif res.text == "false":
            return False

    except:
        return False


def register_user(name: str) -> str:
    """
    Registers user in API game.
    """
    url = "{}/register_player/{}".format(API_URL, name)
    res = requests.post(url)
    player_id = res.text[1]
    return player_id


def is_my_turn(player_id: str) -> bool: #CHAR is assigned radomly to player_id
    """
    Checks if it is our turn via API.
    """
    url = "{}/turn/{}".format(API_URL, player_id)
    res = requests.get(url)
    
    if res.text == "true":
        return True
    elif res.text == "false":
        return False


def read_board() -> list:
    """
    Gets game board via API.
    """
    url = "{}/board".format(API_URL)
    res = requests.get(url)
    board_str = res.text
    board = [
        [board_str[1], board_str[2], board_str[3]], 
        [board_str[4], board_str[5], board_str[6]], 
        [board_str[7], board_str[8], board_str[9]]
    ]

    return board


def decide_move(board: list, player_id: str): #Two strategies needed
    """
    Decides next move to make.
    """
    print(player_id)

    posicion_r = 0
    posicion_c = 0


    if(player_id == "X" and board[posicion_r][posicion_c]=="-"):

        row = posicion_r
        column = posicion_c
        print("1")

        return [row, column]

    elif(player_id =="X" and board[0][2]=="-"):
        row = posicion_r
        column = posicion_c +2

        print("2")

        return [row, column]

    elif(player_id == "X" and board[0][0]=="X" and board[0][2]=="X" and board[0][1]=="-"):
        row= posicion_r
        column=posicion_c+1

        print("3")

        return [row, column]
    

    elif(player_id =="X" and board[2][2]=="-"):
        row = posicion_r +2
        column = posicion_c +2

        print("4")

        return [row, column]


    elif(player_id == "X" and (board[0][0]=="X" and board[2][0]=="X" and board[1][2]=="-")):
        row= posicion_r+1
        column=posicion_c+2

        print("5")

        return [row, column]

    #Fin estrategia principal
    

    elif(player_id =="X" and board[0][2]=="X" and board[2][2]=="-" and board[2][2]=="-"):
        row = posicion_r +2
        column = posicion_c +2

        print("6")

        return [row, column]


    elif(player_id == "X" and (board[0][0]=="X" and board[2][2]=="X" and board[1][1]=="-")):
        row= posicion_r+1
        column=posicion_c+1

        print("7")

        return [row, column]

    elif(player_id =="X" and board[2][0]=="-"):
        row = posicion_r +2
        column = posicion_c 

        print("8")

        return [row, column]

    elif(player_id =="X" and board[0][0]=="X" and board[2][0]=="X" and board[1][0]=="-"):
        row = posicion_r +1
        column = posicion_c

        print("9")

        return [row, column]

    #defensive strategy X

    #vertical

    #column 0

    elif(player_id =="X" and board[0][0]=="O" and board[1][0]=="O"):
        row = 2
        column = 0

        print("a")

        return [row, column]


    elif(player_id =="X" and board[1][0]=="O" and board[2][0]=="O"):
        row = 0
        column = 0

        print("b")

        return [row, column]



    elif(player_id =="X" and board[0][0]=="O" and board[2][0]=="O"):
        row = 1
        column = 0

        print("c")

        return [row, column]

    #column 1 

    elif(player_id =="X" and board[0][1]=="O" and board[1][1]=="O"):
        row = 2
        column = 1

        print("d")

        return [row, column]


    elif(player_id =="X" and board[1][1]=="O" and board[2][1]=="O"):
        row = 0
        column = 1

        print("e")

        return [row, column]


    elif(player_id =="X" and board[0][1]=="O" and board[2][1]=="O"):
        row = 1
        column = 1

        print("f")

        return [row, column]

    # column 2

    elif(player_id =="X" and board[0][2]=="O" and board[1][2]=="O"):
        row = 2
        column = 2

        print("g")

        return [row, column]

    elif(player_id =="X" and board[1][2]=="O" and board[2][2]=="O"):
        row = 0
        column = 2

        print("h")

        return [row, column]


    elif(player_id =="X" and board[0][2]=="O" and board[2][2]=="O"):
        row = 1
        column = 2

        print("i")

        return [row, column]
    
   






    #0 strategy

    if(player_id == "O" and board[posicion_r][posicion_c]=="-"):

        row = posicion_r
        column = posicion_c
        print("1")

        return [row, column]

    elif(player_id =="O" and board[0][2]=="-"):
        row = posicion_r
        column = posicion_c +2

        print("2")

        return [row, column]

    elif(player_id == "O" and board[0][0]=="O" and board[0][2]=="O" and board[0][1]=="-"):
        row= posicion_r
        column=posicion_c+1

        print("3")

        return [row, column]
    

    elif(player_id =="O" and board[2][2]=="-"):
        row = posicion_r +2
        column = posicion_c +2

        print("4")

        return [row, column]


    elif(player_id == "O" and (board[0][0]=="O" and board[2][0]=="O" and board[1][2]=="-")):
        row= posicion_r+1
        column=posicion_c+2

        print("5")

        return [row, column]

    #Fin estrategia principal
    

    elif(player_id =="O" and board[0][2]=="O" and board[2][2]=="-" and board[2][2]=="-"):
        row = posicion_r +2
        column = posicion_c +2

        print("6")

        return [row, column]


    elif(player_id == "O" and (board[0][0]=="O" and board[2][2]=="O" and board[1][1]=="-")):
        row= posicion_r+1
        column=posicion_c+1

        print("7")

        return [row, column]

    elif(player_id =="O" and board[2][0]=="-"):
        row = posicion_r +2
        column = posicion_c 

        print("8")

        return [row, column]

    elif(player_id =="O" and board[0][0]=="O" and board[2][0]=="O" and board[1][0]=="-"):
        row = posicion_r +1
        column = posicion_c

        print("9")

        return [row, column]

    
    row = randint(0, 2)
    column = randint(0, 2)

    
    row = randint(0, 2)
    column = randint(0, 2)
    
    return [row, column]


def validate_move(board: list, move: list) -> bool:
    """
    Checks if the desired next move hits an empty position.
    """
    row, col = move[0], move[1]

    if board[row][col] == "-":
        return True

    return False


def send_move(player_id: str, move: list) -> None:
    """
    Sends move to API.
    """
    row, col = move[0], move[1]
    url = "{}/move/{}/{}/{}".format(API_URL, player_id, row, col)
    res = requests.post(url)
    return None


def does_game_continue() -> bool:
    """
    Checks if the current match continues via API.
    """
    url = "{}/continue".format(API_URL)
    res = requests.get(url)

    if res.text == "true":
        return True
    elif res.text == "false":
        return False


def print_board(board: list) -> None:
    '''
    Prints the baord in console to watch the game.
    '''
    print("\nCurrent board: \n")
    print(board[0][0], "|", board[0][1], "|", board[0][2])
    print("----------")
    print(board[1][0], "|", board[1][1], "|", board[1][2])
    print("----------")
    print(board[2][0], "|", board[2][1], "|", board[2][2], "\n")
