from piece import *

class Tower(Piece):
    def __init__(self, color, image_file):
        super().__init__("Torre", color, image_file)
    
    # position eh uma tupla coordenada (linha,coluna)
    def move(self, position, board):
        # implementar movimentacao
        pass
    
    def attack(self, position, board):
        # implementar ataque
        pass