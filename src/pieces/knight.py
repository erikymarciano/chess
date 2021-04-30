from .piece import *
from ..possibleplays import *

class Knight(Piece):
    def __init__(self, color, image_file, frames = 4):
        super().__init__("Cavalo", color, image_file, frames)
        self.all_plays = [( 2, -1), ( 2,  1), (-2, -1), (-2,  1), ( 1,  2), (-1,  2), (-1, -2), ( 1, -2) ]
    
    # position eh uma tupla coordenada (linha,coluna)
    def move(self, position, board):
        possible_plays = PossibleMoves(position[0], position[1], board, self.color, self.all_plays)
        return possible_plays.moves
    
    def attack(self, position, board):
        possible_plays = PossibleAttacks(position[0], position[1], board, self.color, self.all_plays)
        return possible_plays.attacks