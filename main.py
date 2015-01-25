import numpy as np
from copy import copy
from abc import ABCMeta, abstractmethod

class Connect4Game():
    def __init__(self, player1,player2):
        self.player1 = player1
        self.player2 = player2
        self.player_names = {player1: player1, player2: player2}
        self.board = np.zeros((6,7), dtype=np.int8)
        self.turn = player1
        self.last_move = ()
        self.winner = None

    def gameover(self):
        if self.last_move == ():
            return False

        rind, cind = self.last_move
        row = self.board[rind, :]
        col = self.board[:, cind]
        diag1 = np.diagonal(self.board, cind - rind)
        diag2 = np.diagonal(np.fliplr(self.board), -(cind + rind - 6))

        for line in [row, col, diag1, diag2]:
            if line.shape[0] < 4:
                continue

            for four in [line[i:i+4] for i in range(len(line)-3)]:
                if sum(four == 1) == 4:
                    self.winner = self.player1
                    return True
                elif sum(four == 2) == 4:
                    self.winner = self.player2
                    return True
        if sum(self.board[0] == 0) == 0:
            return True
        return False
               
        
