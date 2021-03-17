from piece import *

class Pawn(Piece):
    def __init__(self, color, image_file, direction):
        self.direction = direction # direcao na qual o peao se move
        super().__init__("Peão", color, image_file)
    
    # position eh uma tupla coordenada (linha,coluna)
    def move(self, position, board):
        possible_moves = []
        
        x = position[0] + self.direction
        y = position[1]

        if board.board_state[x][y] != None: return possible_moves # tem uma peca no caminho

        possible_moves.append((position[0] + self.direction, position[1]))
        # se o peao ainda n se moveu, ele pode andar duas casas
        if not self.moved:
            x = position[0] + 2*self.direction
            if board.board_state[x][y] != None: return possible_moves # tem uma peca no caminho

            possible_moves.append((position[0] + 2 * self.direction, position[1]))
        
        return possible_moves
    
    def attack(self, position, board):

        possible_attacks = []
        x = position[0] + self.direction
        y = position[1] + 1
        if y < 0 or y > 7: return possible_attacks
        if(board.board_state[x][y] != None and board.board_state[x][y].color != self.color):
            possible_attacks.append((x,y))

        y = position[1] - 1
        if y < 0 or y > 7: return possible_attacks
        if(board.board_state[x][y] != None and board.board_state[x][y].color != self.color):
            possible_attacks.append((x,y))

        return possible_attacks