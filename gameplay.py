from board import *
# from PPlay.sound import *

class Gameplay():
    def __init__(self, choosen_color, janela, mouse):
        self.janela = janela
        self.janela.set_background_color((0,0,0))
        self.mouse = mouse
        self.player1_color = choosen_color

        # self.sound_effect = Sound("assets/sound/piece_move_sound.ogg")

        self.board = Board("assets/game/Top Down/Boards/Full Boards/Wood and Marble 512x552.png")
        self.white_king_location, self.black_king_location = self.board.initial_state(self.player1_color)
        self.board.set_position(self.janela.width/2 - self.board.width/2, self.janela.height/2 - self.board.height/2)
        self.board.draw_board_state()

        self.color_on_play = "W" # as brancas comecam

        self.checkmate = False
        self.stalemate = False # empate

    def destiny_special_move(self, possible_actions, index ):

        if 'special_move' not in possible_actions: return False
        special_moves = possible_actions['special_move']

        if index == special_moves[0]['destiny']: return True
        return False

    def copy_board_state(self):
        temp_board = Board("assets/game/Top Down/Boards/Full Boards/Wood and Marble 512x552.png")
        temp_board.board_state = []

        for i in range(8):
            line = []
            for j in range(8):
                line.append(self.board.board_state[i][j])
            temp_board.board_state.append(line)
        return temp_board


    def get_valid_moves(self):
        moves = self.get_all_possible_moves(self.color_on_play, self.board)
        temp_king_position = None
            

        for i in range(len(moves)-1, -1, -1): # moves = [[piece_position, {"moves": [], "attack": []}], [piece_position, {"moves": [], "attack": []}]]
            # make moves
            piece_position = moves[i][0]
            for j in range(len(moves[i][1]["move"])-1, -1, -1):
                piece_move = moves[i][1]["move"][j]

                temp_board = self.copy_board_state()

                piece = temp_board.board_state[piece_position[0]][piece_position[1]]

                temp_board.board_state[piece_position[0]][piece_position[1]] = None

                temp_board.board_state[piece_move[0]][piece_move[1]] = piece
                
                # atualiza posicao do Rei
                if piece.name == "Rei":
                    temp_king_location = piece_move
                else:
                    temp_king_location = None

                # in check?
                if self.in_check(temp_board, temp_king_location):
                    moves[i][1]["move"].remove(moves[i][1]["move"][j])
            
            for j in range(len(moves[i][1]["attack"])-1, -1, -1):
                piece_attack = moves[i][1]["attack"][j]

                temp_board = self.copy_board_state()

                piece = temp_board.board_state[piece_position[0]][piece_position[1]]

                temp_board.board_state[piece_position[0]][piece_position[1]] = None

                temp_board.board_state[piece_attack[0]][piece_attack[1]] = piece

                # atualiza posicao do Rei
                if piece.name == "Rei":
                    temp_king_location = piece_move
                else:
                    temp_king_location = None

                # in check?
                if self.in_check(temp_board, temp_king_location):
                    moves[i][1]["attack"].remove(moves[i][1]["attack"][j])
            
            if len(moves[i][1]["move"]) == 0 and len(moves[i][1]["attack"]) == 0: # a peca n pode se mover e nem atacar
                moves.remove(moves[i])
        
        if len(moves) == 0:
            if self.in_check(self.board):
                self.checkmate = True
                print("############# Checkmate ############")
            else:
                self.stalemate = True
                print("############# Stalemate ############")

        return moves

   
    def get_all_possible_moves(self, on_play, temp_board):
        pieces_position = self.board.get_all_pieces_from_color(on_play)

        all_possible_moves = []
        for piece_position in pieces_position:
            all_possible_moves.append([piece_position, temp_board.board_state[piece_position[0]][piece_position[1]].on_choose(piece_position, temp_board)])
        
        return all_possible_moves

    def in_check(self, temp_board, king_location = None):
        if king_location == None:
            if self.color_on_play == "W":
                return self.square_under_attack(self.white_king_location, temp_board)
            else:
                return self.square_under_attack(self.black_king_location, temp_board)
        else:
            return self.square_under_attack(king_location, temp_board)

    def square_under_attack(self, position, temp_board):
        if self.color_on_play == "W":
            opp_moves = self.get_all_possible_moves("B", temp_board) # moves = [[piece_position, {"moves": [], "attack": []}], [piece_position, {"moves": [], "attack": []}]]
        else:
            opp_moves = self.get_all_possible_moves("W", temp_board) # moves = [[piece_position, {"moves": [], "attack": []}], [piece_position, {"moves": [], "attack": []}]]
        
        for move in opp_moves:
            for attack in move[1]["attack"]:
                if attack[0] == position[0] and attack[1] == position[1]:
                    return True
        
        return False

    def player_turn(self):
        # verifica se o mouse esta dentro do tabuleiro
        piece_index = self.board.position_to_index(self.mouse.get_position())
        if piece_index == None: return False

        # verifica se o mouse esta sobre uma peca
        piece = self.board.board_state[piece_index[0]][piece_index[1]]
        if piece == None: return False

        # verifica se a peca clicada eh da cor do jogador da vez
        if self.mouse.is_button_pressed(1) and self.color_on_play == piece.color:
            #possible_actions = piece.on_choose(piece_index, self.board)
            valid_moves = self.get_valid_moves() # moves = [[piece_position, {"moves": [], "attack": []}], [piece_position, {"moves": [], "attack": []}]]
            rival_color = 'W' if self.color_on_play == 'B' else 'B'
            special_move = {}

            if piece.name == 'Rei':
                if not (piece.moved and self.in_check(self.board)) :
                    has_piece_until_tower = False
                    temporary_board = self.copy_board_state()

                    for i in range(piece_index[1] + 1 , 1, 7):
                        state = self.board.board_state[piece_index[0]][i]
                        temporary_board.board_state[piece_index[0]][i] = piece
                        if (state != None) or self.square_under_attack((piece_index[0],i), temporary_board):
                            has_piece_until_tower = True
                            break

                    if not has_piece_until_tower:
                        tower = self.board.board_state[piece_index[0]][piece_index[1] + 3]
                        if not tower.moved:
                            king_position_on_valid_moves = [i for i in range(len(valid_moves)) if valid_moves[i][0] == (6, 1)]

                            special_move = { 'special_move': [ 
                                {'origin': piece_index, 'destiny': (piece_index[0], piece_index[1] + 2), 'piece': piece },
                                {'origin': (7,7),       'destiny': (piece_index[0], piece_index[1] + 1), 'piece': self.board.board_state[7][7] }
                            ] }

            if len(valid_moves) == 0: return False

            possible_actions = None

            for piece_actions in valid_moves:
                if piece_actions[0] == piece_index:
                    possible_actions = piece_actions[1]
                    break
            if possible_actions == None: return False
            
            temp_possible_actions = possible_actions
            possible_actions = { **temp_possible_actions, **special_move}
   
            if "special_move" in possible_actions:
                special_move = possible_actions["special_move"]
                marker = GameImage("assets/game/Top Down/move_marker.png")
                position = self.board.index_to_position(special_move[0]['destiny'])
                marker.set_position(position[0], position[1])
                marker.draw()


            for move_index in possible_actions["move"]:
                marker = GameImage("assets/game/Top Down/move_marker.png")
                
                position = self.board.index_to_position(move_index)

                marker.set_position(position[0], position[1])
                marker.draw()
            for attack_index in possible_actions["attack"]:
                marker = GameImage("assets/game/Top Down/attack_marker.png")
                
                position = self.board.index_to_position(attack_index)

                marker.set_position(position[0], position[1])
                marker.draw()
            
            # movimentacao
            self.janela.delay(100)
            while True: # espera o jogador escolher a jogada ou cancelar
                self.janela.update()
                index = self.board.position_to_index(self.mouse.get_position())

                if self.mouse.is_button_pressed(1):
                    if index in possible_actions["move"] or index in possible_actions["attack"]:
                        self.board.board_state[piece_index[0]][piece_index[1]] = None
                        self.board.board_state[index[0]][index[1]] = piece
                        
                        piece.moved = True # a peca fez pelo menos 1 movimento

                        # atualiza posicao do Rei
                        if piece.name == "Rei":
                            if piece.color == "W": self.white_king_location = index
                            else: self.black_king_location = index

                        self.janela.set_background_color((0,0,0))
                        self.board.draw_board_state()
                        # self.sound_effect.play()
                        return True # o jogador realizou uma jogada

                    if self.destiny_special_move(possible_actions, index):
                        special_move = possible_actions['special_move']

                        for move in special_move:
                            self.board.board_state[move['origin'][0]][move['origin'][1]] = None
                            self.board.board_state[move['destiny'][0]][move['destiny'][1]] = move['piece']
                            move["piece"].moved = True
                    
                            self.janela.set_background_color((0,0,0))
                            self.board.draw_board_state()
                        return True

                    else:
                        self.board.draw_board_state()
                        return False # o jogador clicou em um local invalido

    def loop(self):
        while True:
            if self.player_turn():
                if self.color_on_play == "W": self.color_on_play = "B"
                else: self.color_on_play = "W"
            elif self.checkmate:
                message = GameImage("assets/game/checkmate.png")
                message.set_position(self.janela.width/2 - message.width/2, self.janela.height/2 - message.height/2)
                message.draw()
                self.janela.update()
                self.janela.delay(2000)
                return
            elif self.stalemate:
                message = GameImage("assets/game/stalemate.png")
                message.set_position(self.janela.width/2 - message.width/2, self.janela.height/2 - message.height/2)
                message.draw()
                self.janela.update()
                self.janela.delay(2000)
                return
            self.janela.update()