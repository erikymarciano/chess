from piece import *

class Queen(Piece):
    def __init__(self, color, image_file):
        super().__init__("Rainha", color, image_file)
    
    # position eh uma tupla coordenada (linha,coluna)
    def move(self, position, board):
        possible_moves = []
        directions = [(1,0),(0,1),(1,1),(-1,0),(0,-1),(-1,-1),(1,-1),(-1,1)]

        for direction in directions:
            aux = 1
            x = position[0] + aux*direction[0]
            y = position[1] + aux*direction[1]
            while  0 <= x <= 7 and 0 <= y <= 7 and board.board_state[x][y] == None:
                possible_moves.append((x,y))
                aux += 1
                x = position[0] + aux*direction[0]
                y = position[1] + aux*direction[1]

        return possible_moves
    
    def attack(self, position, board):
        possible_attacks = []
        directions = [(1,0),(0,1),(1,1),(-1,0),(0,-1),(-1,-1),(1,-1),(-1,1)]

        for direction in directions:            
            aux = 1
            x = position[0] + aux*direction[0]
            y = position[1] + aux*direction[1]
            while  0 <= x <= 7 and 0 <= y <= 7 :
                if(board.board_state[x][y] != None and board.board_state[x][y].color == self.color):                    
                    break
                if(board.board_state[x][y] != None and board.board_state[x][y].color != self.color):
                    possible_attacks.append((x,y))
                    break
                aux += 1
                x = position[0] + aux*direction[0]
                y = position[1] + aux*direction[1]

        return possible_attacks