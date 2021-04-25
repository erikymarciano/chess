from board import *
import random
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


    def check_tower_until_king(self, piece, piece_index):
        temporary_board = self.copy_board_state()
        tower_location = 0
        for i in range( tower_location + 1, piece_index[1] , 1):
            state = self.board.board_state[piece_index[0]][i]
            temporary_board.board_state[piece_index[0]][i-1] = None
            temporary_board.board_state[piece_index[0]][i] = piece
            if state != None or self.square_under_attack((piece_index[0], i), temporary_board):
                return False
    
        tower = self.board.board_state[piece_index[0]][tower_location]
        if tower.__class__ is not Tower: return False
        if not tower.moved:
            king_column = piece_index[1] - 2
            
            return [
                   {'origin': piece_index, 'destiny': (piece_index[0], king_column), 'piece': piece },
                   {'origin': (piece_index[0], tower_location), 'destiny': (piece_index[0], king_column + 1), 'piece': tower }
                   ]
        return False


    def check_king_until_tower(self, piece, piece_index):
      temporary_board = self.copy_board_state()
        
      tower_location = 7

      for i in range( piece_index[1]+1 ,tower_location, 1):
        state = self.board.board_state[piece_index[0]][i]
        temporary_board.board_state[piece_index[0]][i-1] = None
        temporary_board.board_state[piece_index[0]][i] = piece
        if state != None or self.square_under_attack((piece_index[0], i), temporary_board):
            return False
        
      tower = self.board.board_state[piece_index[0]][tower_location]
      if tower.__class__ is not Tower: return False
      if not tower.moved:
        king_column = piece_index[1] + 2
            
        return [
            {'origin': piece_index, 'destiny': (piece_index[0], king_column), 'piece': piece },
            {'origin': (piece_index[0], tower_location), 'destiny': (piece_index[0], king_column - 1), 'piece': tower }
        ]
      return False

    def promote(self):
        knight, bishop, queen, tower = [None for i in range(4)]
        color = self.color_on_play

        if self.color_on_play == "W":
            knight = Knight(color, "assets/game/Top Down/Pieces/Marble/w_knight.png")
            bishop = Bishop(color, "assets/game/Top Down/Pieces/Marble/w_bishop.png")
            queen = Queen(color, "assets/game/Top Down/Pieces/Marble/w_queen.png")
            tower = Tower(color, "assets/game/Top Down/Pieces/Marble/w_tower.png")
        else:
            knight = Knight(color, "assets/game/Top Down/Pieces/Marble/b_knight.png")
            bishop = Bishop(color, "assets/game/Top Down/Pieces/Marble/b_bishop.png")
            queen = Queen(color, "assets/game/Top Down/Pieces/Marble/b_queen.png")
            tower = Tower(color, "assets/game/Top Down/Pieces/Marble/b_tower.png")
        
        label = GameImage("assets/game/pawn_promotion.png")
        
        if self.player1_color == self.color_on_play:
            label.set_position(self.board.x + self.board.width + 10, self.janela.height - (2*knight.height + label.height + 10))
            knight.set_position(self.board.x + self.board.width + 10, self.janela.height - (knight.height + 10))
            bishop.set_position(self.board.x + self.board.width + knight.width + 10, self.janela.height - (knight.height + 10))
            queen.set_position(self.board.x + self.board.width + 10, self.janela.height - (2*knight.height + 10))
            tower.set_position(self.board.x + self.board.width + knight.width + 10, self.janela.height - (2*knight.height + 10))
        else:
            label.set_position(self.board.x - (2*knight.width + 10), 10)
            knight.set_position(self.board.x - (2*knight.width + 10), label.height + 10)
            bishop.set_position(self.board.x - (knight.width + 10), label.height + 10)
            queen.set_position(self.board.x - (knight.width + 10), label.height + knight.height + 10)
            tower.set_position(self.board.x - (2*knight.width + 10), label.height + knight.height + 10)

        knight.draw()
        bishop.draw()
        queen.draw()
        tower.draw()
        label.draw()

        while True:
            self.janela.update()
            if self.mouse.is_button_pressed(1):
                if self.mouse.is_over_object(knight):
                    return knight
                elif self.mouse.is_over_object(bishop):
                    return bishop
                elif self.mouse.is_over_object(queen):
                    return queen
                elif self.mouse.is_over_object(tower):
                    return tower
        
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
            special_move = {}
            if piece.name == 'Rei':
                if not (piece.moved and self.in_check(self.board)):

                    left_roque  = self.check_tower_until_king(piece, piece_index)
                    right_roque = self.check_king_until_tower(piece, piece_index)
       

                    if right_roque == False and left_roque == False:
                        special_move = {}
                    elif right_roque == False:
                        special_move = { 'special_move': left_roque}
                    elif left_roque == False:
                        special_move = { 'special_move': right_roque }
                    else:
                        special_move = { 'special_move': left_roque.append(right_roque[0]) }
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
                if len(possible_actions["special_move"]) != 0:
                    for move in possible_actions['special_move']: 
                        marker = GameImage("assets/game/Top Down/special_move_marker.png")
                        position = self.board.index_to_position(move['destiny'])
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

                        # peão está na ultima casa
                        
                        if piece.name == "Peão" and (index[0] == 0 or index[0] == 7):
                            #self.board.board_state[index[0]][index[1]] = None
                            self.janela.set_background_color((0,0,0))
                            self.board.draw_board_state()

                            piece = self.promote()

                            self.board.board_state[index[0]][index[1]] = piece

                            self.janela.update()

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

    def ia_turn(self):
        self.janela.delay(200)
        print(self.checkmate)
        valid_moves = self.get_valid_moves() # moves = [[piece_position, {"moves": [], "attack": []}], [piece_position, {"moves": [], "attack": []}]]

        if len(valid_moves) == 0:
            self.checkmate = True
            return False

        pieces_weight = {"Rei": 10, "Rainha": 9, "Torre": 5, "Cavalo": 3, "Bispo": 3, "Peão": 1}

        def my_criteria(elem):
            attacks = elem[1]["attack"]

            best_attack_weight = 0

            for index in attacks:
                attack_weight = pieces_weight[self.board.board_state[index[0]][index[1]].name]

                if attack_weight > best_attack_weight:
                    best_attack_weight = attack_weight
            
            return best_attack_weight

        sorted_attacks = sorted(valid_moves, reverse=True, key=my_criteria)
        if len(sorted_attacks[0][1]["attack"]) > 0:
            piece_index = sorted_attacks[0][0]
        
            attacks = sorted_attacks[0][1]["attack"]
            best_attack_weight = 0
            best_attack = None
            for i in range(len(attacks)):
                attack_weight = pieces_weight[self.board.board_state[attacks[i][0]][attacks[i][1]].name]

                if attack_weight > best_attack_weight:
                    best_attack_weight = attack_weight
                    best_attack = attacks[i]

            piece = self.board.board_state[piece_index[0]][piece_index[1]]

            self.board.board_state[piece_index[0]][piece_index[1]] = None
            
            self.board.board_state[best_attack[0]][best_attack[1]] = piece
            piece.moved = True

            # atualiza posicao do Rei
            if piece.name == "Rei":
                if piece.color == "W": 
                    self.white_king_location = best_attack
                else: 
                    self.black_king_location = best_attack

            print(self.white_king_location)
            print(self.black_king_location)

            if piece.name == "Peão" and (best_attack[0] == 0 or best_attack[0] == 7): # promocao do peao
                if piece.color == "W":
                    piece = Queen(piece.color, "assets/game/Top Down/Pieces/Marble/w_queen.png")
                else:
                    piece = Queen(piece.color, "assets/game/Top Down/Pieces/Marble/b_queen.png")


            self.janela.set_background_color((0,0,0))
            self.board.draw_board_state()
            
            return True

        random_piece = random.choice(valid_moves)
        random_move = random.choice(random_piece[1]["move"])

        piece = self.board.board_state[random_piece[0][0]][random_piece[0][1]]
        
        self.board.board_state[random_piece[0][0]][random_piece[0][1]] = None
        
        self.board.board_state[random_move[0]][random_move[1]] = piece       

        piece.moved = True

        # atualiza posicao do Rei
        if piece.name == "Rei":
            if piece.color == "W": 
                self.white_king_location = random_move
            else: 
                self.black_king_location = random_move

        print(self.white_king_location)
        print(self.black_king_location)

        if piece.name == "Peão" and (random_move[0] == 0 or random_move[0] == 7): # promocao do peao
            if piece.color == "W":
                piece = Queen(piece.color, "assets/game/Top Down/Pieces/Marble/w_queen.png")
            else:
                piece = Queen(piece.color, "assets/game/Top Down/Pieces/Marble/b_queen.png")

        self.janela.set_background_color((0,0,0))
        self.board.draw_board_state()

        return True

    def end_game(self):
        if self.checkmate:
            message = GameImage("assets/game/checkmate.png")
            message.set_position(self.janela.width/2 - message.width/2, self.janela.height/2 - message.height/2)
            message.draw()
            self.janela.update()
            self.janela.delay(2000)
            return True
        elif self.stalemate:
            message = GameImage("assets/game/stalemate.png")
            message.set_position(self.janela.width/2 - message.width/2, self.janela.height/2 - message.height/2)
            message.draw()
            self.janela.update()
            self.janela.delay(2000)
            return True
        
        return False

    def loop(self, game_mode):
        if game_mode == 0:
            self.player_vs_player()
        elif game_mode == 1:
            self.player_vs_ia()
        else:
            self.ia_vs_ia()

    def player_vs_player(self):
        while True:
            if self.end_game():
                return
            
            elif self.player_turn():
                if self.color_on_play == "W": self.color_on_play = "B"
                else: self.color_on_play = "W"
                
                self.get_valid_moves()
            
            self.janela.update()
    
    def player_vs_ia(self):
        player_on_turn = None
        
        if self.player1_color == "W": player_on_turn = True
        else: player_on_turn = False

        while True:
            if self.end_game():
                return
            elif player_on_turn:
                if self.player_turn():
                    if self.color_on_play == "W": self.color_on_play = "B"
                    else: self.color_on_play = "W"

                    player_on_turn = False
                    
                    self.get_valid_moves()
            else:
                if self.ia_turn():
                    if self.color_on_play == "W": self.color_on_play = "B"
                    else: self.color_on_play = "W"
                
                    player_on_turn = True

                    self.get_valid_moves()
            
            self.janela.update()

    def ia_vs_ia(self):
        while True:
            if self.end_game():
                return
            self.ia_turn()
            if self.color_on_play == "W": self.color_on_play = "B"
            else: self.color_on_play = "W"

            self.get_valid_moves()
            
            self.janela.update()