"""
Tic Tac Toe Player
"""
import copy
import math
import random

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
    x = 0
    o = 0

    for y in board:
        for c in y:
            if c == "X":
                x += 1
            
            if c == "O":
                o += 1

    if x == o:
        return "X"
    
    elif x > o: return "O"

    """
    Returns player who has the next turn on a board.
    """
    raise NotImplementedError


def actions(board):
    ## possible trouble here !!!
    possible_positions = set()

    y_value = 0
    for y in board:
        x_value = 0
        for x in y:
            if x == EMPTY:
                possible_positions.add((y_value,x_value))
            x_value += 1

        y_value += 1
    
    return possible_positions
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    raise NotImplementedError


def result(board, action):

    whose_time = player(board)

    if action not in actions(board):
        raise NameError('Invalid action')

    new_board = copy.deepcopy(board)
    
  
    new_board[int(action[0])][int(action[1])] = str(whose_time)  

    return new_board

    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    o_chars = 0
    x_chars = 0
    x_positions = []
    o_positions = []
    
    y_value = 0
    for y in board:

        x_value = 0

        for x in y:
            if x == 'O':
                o_chars +=1
                o_positions.append((y_value,x_value))
            
            if x== 'X':
                x_chars += 1
                x_positions.append((y_value,x_value))
            
            x_value +=1
        
        y_value += 1


    if x_chars <= 2 and o_chars <= 2:
        
        return None
    
    else:

        ys = []
        xs = []

        for c in x_positions:
            ys.append(c[0])
            xs.append(c[1])
        
        
        
        if ys.count(0) == 3 or ys.count(1) == 3 or ys.count(2) == 3 or xs.count(0) == 3 or xs.count(1) == 3 or xs.count(2) == 3:
            return "X"
            print('o erro ta aqui')
        
        if (1,1) in x_positions:
            if ((0,0) in x_positions) and ((2,2) in x_positions):
                return "X"
                
            
            if ((2,0) in x_positions) and ((0,2) in x_positions):
                return "X"
                



        ys = []
        xs = []

        for c in o_positions:
            ys.append(c[0])
            xs.append(c[1])
        
        
        
        if ys.count(0) == 3 or ys.count(1) == 3 or ys.count(2) == 3 or xs.count(0) == 3 or xs.count(1) == 3 or xs.count(2) == 3:
            return "O"
        
        if (1,1) in o_positions:
            if ((0,0) in o_positions) and ((2,2) in o_positions):
                return "O"
            
            if ((2,0) in o_positions) and ((0,2) in o_positions):
                return "O"

        return None
    
    return None
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    all = []
    for y in board:
        for x in y:
            all.append(x)

    
    if None not in all:
        return True
    
    if winner(board) != None:
        return True
    
    return False
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):

    vencedor = winner(board)

    if vencedor == 'X':
        return 1
    
    if vencedor == 'O':
        return -1
    
    if vencedor == None:
        return 0

    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    if terminal(board):
        return None
    
    moves = {}
    who = player(board)
    best_action = None

    if who == 'X':
        ideal_score = 1
        best_score = -math.inf
        for c in actions(board):

            score = minimax2(result(board, c), False)

            if score > best_score:
                best_score = score
                best_action = c
            
            if score == ideal_score:
                best_score = score
                best_action = c
                break
    
    if who == 'O':
        ideal_score = -1
        best_score = math.inf

        for c in actions(board):

            score = minimax2(result(board, c), True)
            if score < best_score:
                best_score = score
                best_action = c

            if score == ideal_score:
                best_score = score
                best_action = c
                break
    
    return best_action



    
        

    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError



    
def minimax2(teorical_board, maximizing):
    if terminal(teorical_board):
        return utility(teorical_board)
    
    if maximizing:
        best_score = -math.inf
        ideal_score = 1
        acts = actions(teorical_board)

        for c in acts:
            score = minimax2(result(teorical_board,c), False)
            
            if score > best_score:
                best_score = score
            
            if score == ideal_score:
                best_score = score
                break
        
        return best_score
    
    if not maximizing:
        best_score = math.inf
        ideal_score = -1
        acts = actions(teorical_board)

        for c in acts:
            score = minimax2(result(teorical_board,c), True)
            
            if score < best_score:
                best_score = score
            
            if score == ideal_score:
                best_score = score
                break
        
        return best_score





    
