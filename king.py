from piece import *

class King(Piece):
    def __init__(self, color, image_file, frames = 2):
        super().__init__("Rei", color, image_file, frames)
    
    # position eh uma tupla coordenada (linha,coluna)
    def move(self, position, board):
        possible_moves = []

        x = position[0] + 1
        y = position[1]
        if x >= 0 and x <= 7:
            if board.board_state[x][y] == None:
                possible_moves.append((x, y))

        x = position[0] - 1
        y = position[1]
        if x >= 0 and x <= 7:
            if board.board_state[x][y] == None:
                possible_moves.append((x, y))

        x = position[0]
        y = position[1] + 1
        if y >= 0 and y <= 7:
            if board.board_state[x][y] == None:
                possible_moves.append((x, y))

        x = position[0]
        y = position[1] - 1
        if y >= 0 and y <= 7:
            if board.board_state[x][y] == None:
                possible_moves.append((x, y))

        x = position[0] + 1
        y = position[1] + 1
        if x >= 0 and x <= 7 and y >= 0 and y <= 7:
            if board.board_state[x][y] == None:
                possible_moves.append((x, y))

        x = position[0] - 1
        y = position[1] + 1
        if x >= 0 and x <= 7 and y >= 0 and y <= 7:
            if board.board_state[x][y] == None:
                possible_moves.append((x, y))

        x = position[0] + 1
        y = position[1] - 1
        if x >= 0 and x <= 7 and y >= 0 and y <= 7:
            if board.board_state[x][y] == None:
                possible_moves.append((x, y))

        x = position[0] - 1
        y = position[1] - 1
        if x >= 0 and x <= 7 and y >= 0 and y <= 7:
            if board.board_state[x][y] == None:
                possible_moves.append((x, y))

        return possible_moves
    
    def attack(self, position, board):
        possible_attacks = []

        x = (position[0] + 1)
        y = position[0]
        if x >= 0 and x <= 7: 
            if(board.board_state[x][y] != None and board.board_state[x][y].color != self.color):
                possible_attacks.append((x,y))

        x = (position[0] - 1)
        y = position[1]
        if x >= 0 and x <= 7: 
            if(board.board_state[x][y] != None and board.board_state[x][y].color != self.color):
                possible_attacks.append((x,y))

        x = position[0]
        y = (position[1] + 1)
        if y >= 0 and y <= 7: 
            if(board.board_state[x][y] != None and board.board_state[x][y].color != self.color):
                possible_attacks.append((x,y))

        x = position[0]
        y = (position[1] - 1)
        if y >= 0 and y <= 7: 
            if(board.board_state[x][y] != None and board.board_state[x][y].color != self.color):
                possible_attacks.append((x,y))

        x = (position[0] + 1)
        y = (position[1] + 1)
        if x >= 0 and x <= 7 and y >= 0 and y <= 7: 
            if(board.board_state[x][y] != None and board.board_state[x][y].color != self.color):
                possible_attacks.append((x,y))

        x = (position[0] - 1)
        y = (position[1] + 1)
        if x >= 0 and x <= 7 and y >= 0 and y <= 7: 
            if(board.board_state[x][y] != None and board.board_state[x][y].color != self.color):
                possible_attacks.append((x,y))

        x = (position[0] - 1)
        y = (position[1] - 1)
        if x >= 0 and x <= 7 and y >= 0 and y <= 7: 
            if(board.board_state[x][y] != None and board.board_state[x][y].color != self.color):
                possible_attacks.append((x,y))
                
        x = (position[0] + 1)
        y = (position[1] - 1)
        if x >= 0 and x <= 7 and y >= 0 and y <= 7: 
            if(board.board_state[x][y] != None and board.board_state[x][y].color != self.color):
                possible_attacks.append((x,y))
        
        return possible_attacks