from piece import *

class King(Piece):
    def __init__(self, color, image_file, frames = 2):
        super().__init__("Rei", color, image_file, frames)
    
    # position eh uma tupla coordenada (linha,coluna)
    def move(self, position, board):
        # implementar movimentacao
        pass
    
    def attack(self, position, board):
        # implementar ataque
        pass