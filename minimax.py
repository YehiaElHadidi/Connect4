from board import *
from helper_functions import *
import math
import random
import copy


def minimax(board, depth, player):
    valid_locations = board.get_valid_locations()
    print(valid_locations)
    # terminal_node posibilities: agent wins, opponent wins, out of pieces
    terminal_node = is_terminal(board.get_board(), valid_locations)

    if depth == 0 or terminal_node:
        if terminal_node:  # return the heuristic value of node
            if wining_move(board.get_board(), PLAYER_PIECE):
                return (None, 10000000000)
            elif wining_move(board.get_board(), COMPUTER_PIECE):
                return (None, -10000000000)
            else:  # out of moves , Drawn
                return (None, 0)
        else:
            return (None, score_position(board, player))

    # algorithm tries to maximize the score by selecting the move that leads to the highest score.
    if player == PLAYER_PIECE:
        score = -math.inf
        best_col = random.choice(valid_locations)

        for c in valid_locations:
            row = board.get_next_open_row(c)
            board_temp = copy.deepcopy(board)
            board_temp.drop_piece(row, c, PLAYER_PIECE)

            # get the first index of the returned
            new_score = minimax(board_temp, depth-1, False)[1]

            if new_score > score:
                score = new_score
                best_col = c

        return best_col, score

    else:  # minimizing player turn , the algorithm tries to minimize the score by selecting the move that leads to the lowest score.
        score = math.inf
        col = random.choice(valid_locations)

        for c in valid_locations:
            row = board.get_next_open_row(c)
            board_temp = copy.deepcopy(board)
            board_temp.drop_piece(row, c, COMPUTER_PIECE)
            new_score = minimax(board_temp, depth-1, True)[1]

            if new_score < score:
                score = new_score
                col = c

        return col, score
