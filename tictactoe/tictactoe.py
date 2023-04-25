"""
Tic Tac Toe Player
"""

import math
import copy


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
    """
    Returns player who has the next turn on a board.
    """
    if terminal(board) == True:
        return None

    # Calculate numbers of empty cells and tell whose turn.
    if board == initial_state():
        return X
    else:
        k = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    k = k + 1

        if ((9-k) % 2) == 0:
            return X
        else:
            return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board) == True:
        return None

    action = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action.add((i, j))

    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if len(action) != 2:
        raise ValueError

    if isinstance(action, tuple):
        if not isinstance(action[0], int) and (action[1], int):
            raise ValueError

    if action[0] < 0 or action[0] > 2 or action[1] < 0 or action[1] > 2:
        raise ValueError

    board_new = copy.deepcopy(board)

    act = player(board)

    board_new[action[0]][action[1]] = act

    return board_new


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == X and board[i][1] == X and board [i][2] == X:
            return X
        if board[0][i] == X and board[1][i] == X and board [2][i] == X:
            return X
        if board[i][0] == O and board[i][1] == O and board [i][2] == O:
            return O
        if board[0][i] == O and board[1][i] == O and board [2][i] == O:
            return O

    diag1 = set()
    for i in range(3):
        diag1.add(board[i][i])
    if len(diag1) == 1:
        for i in diag1:
            if i != EMPTY:
                return i

    diag2 = set()
    for i in range(3):
        diag2.add(board[i][2-i])
    if len(diag2) == 1:
        for i in diag2:
            if i != EMPTY:
                return i

    k = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                k = k + 1

    if k == 0:
        return None

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if not winner(board) == None:
        return True

    k = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                k = k + 1
    if k == 0:
        return True


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


def minimax(board):
    if terminal(board) == True:
        return None

    def max_value(board):
        if terminal(board) == True:
            return utility(board)

        v = -math.inf
        for action in actions(board):
            x = min_value(result(board, action))
            if type(x) == int:
                v = max(v, x)
        return v

    def min_value(board):
        if terminal(board) == True:
            return utility(board)

        v = math.inf
        for action in actions(board):
            x = max_value(result(board, action))
            if type(x) == int:
                v = min(v, x)
        return v

    if player(board) == X:
        dic = {}
        for action in actions(board):
            s = min_value(result(board,action))
            dic.update({action: s})
            if s == 1:
                return action

        for i, j in dic.items():
            if j == 0:
                return i

    elif player(board) == O:
        dic1 = {}
        for action in actions(board):
            s = max_value(result(board,action))
            dic1.update({action: s})
            if s == -1:
                return action
        for i, j in dic1.items():
            if j == 0:
                return i

    else:
    	return None


