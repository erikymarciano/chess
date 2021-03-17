from PPlay.sprite import *

class Piece(Sprite):
    def __init__(self, name, color, image_file, frames=1):
        self.name = name
        self.color = color # W = branca, B = preta
        self.moved = False # diz se a peca ja se moveu
        super().__init__(image_file, frames)

    def move(self, position, board): pass

    def attack(self, positon, board): pass

    def on_choose(self, position, board):
        return {"move": self.move(position, board), "attack": self.attack(position, board)}