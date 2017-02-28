#!/usr/bin/python3
from gtp_connection import GtpConnection
from board_util import GoBoardUtil

class RandomPlayer():
    def __init__(self):
        """
        Player that selects moves randomly from the set of legal moves.
        Does not fill single-point eyes.

        Parameters
        ----------
        name : str
            name of the player (used by the GTP interface).
        version : float
            version number (used by the GTP interface).
        """
        self.name = "NoGo2"
        self.version = 0.1
    def get_move(self, board, color, timelimit = 1):
        board_copy = board.copy()
        board_copy.to_play = color
        winner, last_move, first_move = GoBoardUtil.solve(board, timelimit)
        
        print(winner, color)
        if winner is color:
            return first_move
        else:
            return GoBoardUtil.generate_random_move(board, color)
    

def run():
    """
    start the gtp connection and wait for commands.
    """
    con = GtpConnection(RandomPlayer())
    con.start_connection()

if __name__=='__main__':
    run()
