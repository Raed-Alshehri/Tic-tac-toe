"""
Tic Tac Toe Player
"""

import copy
import math
from os import PathLike

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
# In the initial game state, X gets the first move
    if board == initial_state(): 
        return X
# using itteration method:
#board is 3X3 array: need two itterations to reach positions on board to check which player has > num of positions 
    X_times, O_times = 0, 0
    # using count on a list after looping over 1st dimention (rows)
    for row in board:
        X_times += row.count(X)
        O_times += row.count(O)
    # the player who has lower numbers of position on board (more remaining moves) will have the next move
    if X_times <= O_times:
        return X
    else:
        return O
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
# Checking for all possible actions:
# loop through 2D array and check whether the position is EMPTY or not. If so, return a set of possible_moves
    possible_moves = set() # empty set
    for i in range(len(board)):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_moves.add((i, j))

    return possible_moves
    

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # transition model return a newBoard (state) after board takes an action and return a newboard (newstate)
    if action not in actions(board):
        raise Exception("Out of bound Position")
        
    newBoard = copy.deepcopy(board) 
    
    if newBoard[action[0]][action[1]] != EMPTY:
        raise Exception("Position has already been taken")

    newBoard[action[0]][action[1]] = player(board)
    return newBoard


def winner(board):
    # To be a Winner, must have same positions across top, middle and bottom rows.
    for i in range(len(board)): # for row in board (3)
        if board[i][0] == board[i][1] == board[i][2]: # if all columns (0,1,2) in the row (i) are equal
            if board[i][0] == X: # and if the element is x
                return X # winner is x
            elif board[i][0] == O: # or if the element is o
                return O # the winner is o

    # or same position across left middle and right.
    for i in range(3): # for column in board (3)
        if board[0][i] == board[1][i] == board[2][i]: # if all rows (0,1,2) in the column (i) are equal
            if board[0][i] == X: # and if the element is x
                return X # x wins
            elif board[0][i] == O: # or if the element is o
                return O # o wins

    # or must have same elements across diagonallly
    if board[0][0] == board[1][1] == board[2][2]: 
        if board[0][0] == X:
            return X
        elif board[0][0] == O:
            return O
    elif board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == X:
            return X
        elif board[0][2] == O:
            return O


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board) == X or winner(board) == O):
        return True
    else:
        count = 0
        for each_arr in board:
            count += each_arr.count(X)
            count += each_arr.count(O)
        if count == 9: # after eight moves the game ends (either by a win or tie)
            return True
        else:
            return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board): # possible action (i,j)
        value = max_value(result(board, action))
        if value < v:
            v = value
    return v


def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        value = min_value(result(board, action))
        if value > v:
            v = value
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    opt_act = None
    if terminal(board):
        return None
    if player(board) == X:
        inf = -math.inf
        for action in actions(board):
            value = min_value(result(board, action))
            if value > inf:
                inf = value
                opt_act = action

    elif player(board) == O:
        inf = math.inf
        for action in actions(board):
            value = max_value(result(board, action))
            if value < inf:
                inf = value
                opt_act = action
    return opt_act