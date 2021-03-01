from PPlay.window import *
from PPlay.gameimage import *
from PPlay.animation import *
from PPlay.sound import *

# config tela
janela = Window(1200, 700)
janela.set_title("Chess")
mouse = Window.get_mouse()
game = None # estado do jogo

# config imagem menu
fundo_tela = Animation("assets/menu/menu.png", 37)
fundo_tela.set_total_duration(2000)

# config botoes
play_button = GameImage("assets/menu/play_button.png")
play_button.x = janela.width/2 - play_button.width/2
play_button.y = 2 * play_button.height

manual_button = GameImage("assets/menu/manual_button.png")
manual_button.x = janela.width/2 - manual_button.width/2
manual_button.y = 4 * manual_button.height

quit_button = GameImage("assets/menu/quit_button.png")
quit_button.x = janela.width/2 - quit_button.width/2
quit_button.y = 6 * quit_button.height

selector_right = Animation("assets/menu/selector.png", 4) # 4 frames
selector_left = Animation("assets/menu/selector.png", 4) # 4 frames

# soud effects
soundtrack = Sound("assets/sound/Fantascape.ogg")
soundtrack.set_repeat(True)
soundtrack.play()
sound_effect = Sound("assets/sound/Deep-Metal-Clang-SOUND-Effect.ogg")

def animacao_seletor(botao):
    selector_right.set_total_duration(800)
    selector_right.x = botao.x + botao.width
    selector_right.y = botao.y
    selector_right.draw()
    selector_right.update()

    selector_left.set_total_duration(800)
    selector_left.x = botao.x - selector_left.width
    selector_left.y = botao.y
    selector_left.draw()
    selector_left.update()

while True:

    fundo_tela.draw()
    play_button.draw()
    manual_button.draw()
    quit_button.draw()

    if (mouse.is_over_object(play_button)):
        animacao_seletor(play_button)
        if mouse.is_button_pressed(1):
            soundtrack.stop()
            sound_effect.play()
            while fundo_tela.get_curr_frame() < 36:
                fundo_tela.draw()
                fundo_tela.update()
                janela.update()
            # game = gameplay()
            # game.run()

            janela.set_background_color((0,0,0))
            janela.draw_text("Gameplay...", 0, 0, size=30, color=(255,255,255))
            janela.update()
            janela.delay(1500)
            janela.close()

    elif (mouse.is_over_object(manual_button)):
        animacao_seletor(manual_button)
        if mouse.is_button_pressed(1):
            pass
            # game = manual()
            
    elif (mouse.is_over_object(quit_button)):
        animacao_seletor(quit_button)
        if mouse.is_button_pressed(1):
            janela.close()

    janela.update()