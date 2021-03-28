from PPlay.gameimage import *
from pawn import *
from tower import *
from knight import *
from bishop import *
from queen import *
from king import *

class Board(GameImage):
    def __init__(self, image_file):
        self.board_state = []
        super().__init__(image_file)
    
    def initial_state(self, player1_color):
        # 8x8
        def empty_line():
            return [None for x in range(8)]
        def back_line(color):
            if color == "W":
                return [
                        Tower(color, "assets/game/Top Down/Pieces/Marble/w_tower.png"),
                        Knight(color, "assets/game/Top Down/Pieces/Marble/w_knight.png"),
                        Bishop(color, "assets/game/Top Down/Pieces/Marble/w_bishop.png"),
                        Queen(color, "assets/game/Top Down/Pieces/Marble/w_queen.png"),
                        King(color, "assets/game/Top Down/Pieces/Marble/w_king.png"),
                        Bishop(color, "assets/game/Top Down/Pieces/Marble/w_bishop.png"),
                        Knight(color, "assets/game/Top Down/Pieces/Marble/w_knight.png"),
                        Tower(color, "assets/game/Top Down/Pieces/Marble/w_tower.png")
                    ]
            else:
                return [
                        Tower(color, "assets/game/Top Down/Pieces/Marble/b_tower.png"),
                        Knight(color, "assets/game/Top Down/Pieces/Marble/b_knight.png"),
                        Bishop(color, "assets/game/Top Down/Pieces/Marble/b_bishop.png"),
                        Queen(color, "assets/game/Top Down/Pieces/Marble/b_queen.png"),
                        King(color, "assets/game/Top Down/Pieces/Marble/b_king.png"),
                        Bishop(color, "assets/game/Top Down/Pieces/Marble/b_bishop.png"),
                        Knight(color, "assets/game/Top Down/Pieces/Marble/b_knight.png"),
                        Tower(color, "assets/game/Top Down/Pieces/Marble/b_tower.png")
                    ]
        def front_line(color, direction):
            line = []
            image_file = "w_pawn.png"
            if color == "B": image_file = "b_pawn.png"

            for i in range(8):
                piece = Pawn(color, "assets/game/Top Down/Pieces/Marble/" + image_file, direction)
                piece.set_total_duration(800)
                line.append(piece)
            return line

        if player1_color == "W":
            self.board_state.append(back_line("B"))
            self.board_state.append(front_line("B", 1))
            for x in range(4):
                self.board_state.append(empty_line())
            self.board_state.append(front_line("W", -1))
            self.board_state.append(back_line("W"))

            kings_positions = [(7, 3), (0, 4)]
            return kings_positions
        else:
            self.board_state.append(back_line("W"))
            self.board_state.append(front_line("W", 1))
            for x in range(4):
                self.board_state.append(empty_line())
            self.board_state.append(front_line("B", -1))
            self.board_state.append(back_line("B"))

            kings_positions = [(0, 4), (7, 3)]
            return kings_positions

    def get_all_pieces_from_color(self, color):
        pieces_position = []

        for i in range(8):
            for j in range(8):
                if self.board_state[i][j] != None and self.board_state[i][j].color == color:
                    pieces_position.append((i, j))
        
        return pieces_position

    def index_to_position(self, index):
        # cada coluna são 64 pixels
        # cada linha são 64 pixels
        #return (index[0] * 64, index[1] * 64)
        return (self.x + index[1] * 64, self.y + index[0] * 64)
    
    def position_to_index(self, position):
        index = (int((position[1] - self.y) / 64), int((position[0] - self.x) / 64))
        if 0 <= index[0] < 8 and 0 <= index[1] < 8:
            return index
        else:
            return None
    
    def draw_board_state(self):
        self.draw() # desenha o board

        # desenha as pecas
        for i in range(8):
            for j in range(8):
                if (self.board_state[i][j] != None):
                    position_window = self.index_to_position((i,j))
                    #self.board_state[i][j].x = self.x + position_window[1] - self.board_state[i][j].width/4
                    #self.board_state[i][j].y = self.y + position_window[0] - self.board_state[i][j].height/2
                    self.board_state[i][j].x = position_window[0] - self.board_state[i][j].width/4
                    self.board_state[i][j].y = position_window[1] - self.board_state[i][j].height/2
                    self.board_state[i][j].draw()
