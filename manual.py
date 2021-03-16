from PPlay.window import *
from PPlay.gameimage import *

class Manual():
    def __init__(self, janela, mouse):
        self.janela = janela
        self.fundo = GameImage("assets/menu/chess_rules_01.jpg")
        self.mouse = mouse
        self.keyboard = Window.get_keyboard()
        self.state = 1

    def loop(self):
        while True:
            self.fundo.draw()
            if self.keyboard.key_pressed("ENTER"):
                if self.state == 1:
                    self.fundo = GameImage("assets/menu/chess_rules_02.jpg")
                    self.state += 1
                else:
                    self.fundo = GameImage("assets/menu/chess_rules_01.jpg")
                    self.state = 1
                self.janela.delay(500)
            elif self.keyboard.key_pressed("ESC"):
                return
            self.janela.update()