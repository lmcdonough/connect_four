import numpy as np
from copy import copy
from abc import ABCMeta, abstractmethod

class Connect4Game():
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.player_names = {player1 : "Player1", player2 : "Player2"}
        self.board = np.zeros((6, 7), dtype=np.int8)
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

    def move(self, cind):
        free_index = sum(self.board[:, cind] == 0) - 1
        if free_index == -1:
            return False

        if self.turn is self.player1:
            self.board[free_index, cind] = 1
            self.turn = self.player2
        else:
            self.board[free_index, cind] = 2
            self.turn = self.player1

        self.last_move = (free_index, cind)
        return True

    def play(self):
        while not self.gameover():
            print(self.board)
            print(self.player_names[self.turn]+"'s turn.")

            self.move(self.turn.get_move(copy(self.board)))

        print(self.board)

        if self.winner is self.player1:
            print("Winner: player1")
        elif self.winner is self.player2:
            print("Winner: player2")
        else:
            print("Tie")

class BasePlayer(object):
    __metaclass__ = ABCMeta
      
    @abstractmethod
    def __init__(self, empty, me, opponent):
        pass

    @abstractmethod
    def get_move(self, board):
        pass

class HumanPlayer(BasePlayer):
    def __init__(self, empty, me, opponent):
        pass

    def get_move(self, board):
        col = input("Your move (0-6): ")
        return int(col)

class RandomPlayer(BasePlayer):
    def __init__(self, empty, me, opponent):
        pass

    def get_move(self, board):
        free_columns = np.where(board[0] == 0)[0]
        return np.random.choice(free_columns)

def main():
    player1 = HumanPlayer(0, 1, 2)
    player2 = RandomPlayer(0, 2, 1)
    
    game = Connect4Game(player1, player2)
    game.play()

if __name__ == "__main__":
    main()
