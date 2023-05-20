from board import Board
import time
import random
import copy
import math
# GAME LINK
# http://kevinshannon.com/connect4/
from board import PLAYER_PIECE
from minimax import *
from alpha_beta import *
from pynput import mouse
import threading


def wait_for_game_start():
    event = threading.Event()

    def on_click(x, y, button, pressed):
        if button == mouse.Button.left and pressed:
            event.set()

    listener = mouse.Listener(on_click=on_click)
    listener.start()
    event.wait()
    listener.stop()


def main(algorithm, depth):
    print("Waiting for game to start...")
    wait_for_game_start()

    board = Board()

    time.sleep(1)
    game_end = False
    while not game_end:
        (game_board, game_end) = board.get_game_grid()

        # FOR DEBUG PURPOSES
        board.print_grid(game_board)

        # YOUR CODE GOES HERE
        # Insert here the action you want to perform based on the output of the algorithm
        # You can use the following function to select a column
        # random_column = random.randint(0, 6)
        if algorithm == "Minimax":
            best_move = minimax(board, int(depth), PLAYER_PIECE)[0]
        elif algorithm == "Alpha beta pruning":
            best_move = alpha_beta(board, int(
                depth), -math.inf, math.inf, PLAYER_PIECE)[0]

        print(best_move)
        board.select_column(best_move)

        time.sleep(2)
