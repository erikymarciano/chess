from board import *

class Gameplay():
    def __init__(self, choosen_color, janela, mouse):
        self.janela = janela
        self.janela.set_background_color((0,0,0))
        self.mouse = mouse
        self.player1_color = choosen_color

        self.board = Board("assets/game/Top Down/Boards/Full Boards/Wood and Marble 512x552.png")
        self.board.initial_state(self.player1_color)
        self.board.set_position(self.janela.width/2 - self.board.width/2, self.janela.height/2 - self.board.height/2)
        self.board.draw_board_state()

        self.color_on_play = "W" # as brancas comecam
    
    def player_turn(self):
        # verifica se o mouse esta dentro do tabuleiro
        piece_index = self.board.position_to_index(self.mouse.get_position())
        if piece_index == None: return False

        # verifica se o mouse esta sobre uma peca
        piece = self.board.board_state[piece_index[0]][piece_index[1]]
        if piece == None: return False

        # verifica se a peca clicada eh da cor do jogador da vez
        if self.mouse.is_button_pressed(1) and self.color_on_play == piece.color:
            possible_actions = piece.on_choose(piece_index, self.board)
            print(possible_actions)
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
                        self.janela.set_background_color((0,0,0))
                        self.board.draw_board_state()
                        return True # o jogador realizou uma jogada
                    else:
                        self.board.draw_board_state()
                        return False # o jogador clicou em um local invalido
                

    def loop(self):
        while True:
            if self.player_turn():
                if self.color_on_play == "W": self.color_on_play = "B"
                else: self.color_on_play = "W"
            self.janela.update()