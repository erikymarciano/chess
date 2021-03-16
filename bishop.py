from piece import *

class Bishop(Piece):
    def __init__(self, color, image_file, frames = 4):
        super().__init__("Bispo", color, image_file, frames)
    
    # position eh uma tupla coordenada (linha,coluna)
    def move(self, position, board):
        # implementar movimentacao
        pass
    
    def attack(self, position, board):
        # implementar ataque
        pass