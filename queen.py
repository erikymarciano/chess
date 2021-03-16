from piece import *

class Queen(Piece):
    def __init__(self, color, image_file):
        super().__init__("Rainha", color, image_file)
    
    # position eh uma tupla coordenada (linha,coluna)
    def move(self, position, board):
        # implementar movimentacao
        pass
    
    def attack(self, position, board):
        # implementar ataque
        pass