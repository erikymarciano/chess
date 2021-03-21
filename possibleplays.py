class PossibleMoves:
    def __init__(self, position_x, position_y, board, color, plays):
        self.color = color
        self.board = board
        self.plays = plays

        self.position_x = position_x
        self.position_y = position_y

        self.moves = []
        
        self.add_moves()


    def add_moves(self):
        for move in self.plays:
            self.__add_move(move)

    def __add_move(self, move):
        move = self.do_move(move)
        
        if self.__move_is_inside_board(move):
            board_state = self.board.board_state[move[0]][move[1]]

            if self.__can_move(board_state):
                self.moves.append(move)
        
    def do_move(self, direction):
        return (self.position_x + direction[0], self.position_y + direction[1])
    
    def __move_is_inside_board(self, move):
        return self.__in_board(move[0]) and self.__in_board(move[1])
   
    def __can_move(self, board_state):
        return board_state == None

    def __in_board(self, next_position):
        return 0 <= next_position <= 7



###


class PossibleAttacks:
    def __init__(self, position_x, position_y, board, color, plays):
        self.color = color
        self.board = board
        self.plays = plays

        self.position_x = position_x
        self.position_y = position_y
        
        self.attacks = []
        
        self.add_moves()


    def add_moves(self):
        for move in self.plays:
            self.__add_attack(move)

    def __add_attack(self, attack):
        attack = self.do_attack(attack)
        
        if self.__attack_is_inside_board(attack):
            board_state = self.board.board_state[attack[0]][attack[1]]

            if self.__can_attack(board_state):
                self.attacks.append(attack)
            
        
    def do_attack(self, direction):
        return (self.position_x + direction[0], self.position_y + direction[1])
    
    
    def __attack_is_inside_board(self, move):
        return self.__in_board(move[0]) and self.__in_board(move[1])
 
    def __can_attack(self, board_state):
        return board_state != None and board_state.color != self.color

    def __in_board(self, next_position):
        return 0 <= next_position <= 7

