import unittest
from ..board import *
from ..pieces.king import *
from ..pieces.queen import *
from ..pieces.tower import *
from ..pieces.bishop import *
from ..pieces.knight import *
from ..pieces.pawn import *
from ..gameplay import *

class MockJanela():

    def set_background_color(self, rgb):
        pass

mock_janela = MockJanela()

class TestCheckmate:

    @unittest.mock.patch('src.board.super')
    @unittest.mock.patch('src.pieces.piece.super')
    def test_king_and_queen(self, mock_board_super, mock_piece_super):
        mock_board = Board("B")
        mock_board.board_state = [
                [None,None,None,None,None,None,None,None],
                [King("B", 'TBD'), Queen("W", "TBD"), King("W", "TBD"), None, None, None, None, None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None]
            ]

        gameplay = Gameplay("W", mock_janela, None)
        gameplay.board = mock_board

        gameplay.white_king_location = (1,2)
        gameplay.black_king_location = (1,0)
        gameplay.color_on_play = "B"

        gameplay.get_valid_moves()
        
        expected = True

        assert expected == gameplay.checkmate

    @unittest.mock.patch('src.board.super')
    @unittest.mock.patch('src.pieces.piece.super')
    def test_king_and_tower(self, mock_board_super, mock_piece_super):
        mock_board = Board("B")
        mock_board.board_state = [
                [None,Tower("W", "TBD"),None,None,None,None,King("B", "TBD"),None],
                [None,None, None, None, None, None, None, None],
                [None,None,None,None,None,None,King("W", "TBD"),None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None]
            ]

        gameplay = Gameplay("W", mock_janela, None)

        gameplay.white_king_location = (2,6)
        gameplay.black_king_location = (0,6)
        gameplay.board = mock_board
        gameplay.color_on_play = "B"

        gameplay.get_valid_moves()
        
        expected = True

        assert expected == gameplay.checkmate

        
    @unittest.mock.patch('src.board.super')
    @unittest.mock.patch('src.pieces.piece.super')
    def test_king_and_two_bishops(self, mock_board_super, mock_piece_super):
        mock_board = Board("B")
        mock_board.board_state = [
                [None,None,None,None,None,None,None,None],
                [None,None, None, None, None, None, None, None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,Bishop("W", "TBD"),None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,Bishop("W", "TBD"),None,King("W", "TBD"),None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,King("B", "TBD")]
            ]

        gameplay = Gameplay("W", mock_janela, None)

        gameplay.white_king_location = (5,6)
        gameplay.black_king_location = (7,7)
        gameplay.board = mock_board
        gameplay.color_on_play = "B"

        gameplay.get_valid_moves()
        
        expected = True

        assert expected == gameplay.checkmate

    @unittest.mock.patch('src.board.super')
    @unittest.mock.patch('src.pieces.piece.super')
    def test_king_bishop_and_knight(self, mock_board_super, mock_piece_super):
        mock_board = Board("B")
        mock_board.board_state = [
                [King("B", "TBD"),None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None, None],
                [Knight("W", "TBD"),King("W", "TBD"),None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,Bishop("W", "TBD"),None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None]
            ]

        gameplay = Gameplay("W", mock_janela, None)

        gameplay.white_king_location = (2,1)
        gameplay.black_king_location = (0,0)
        gameplay.board = mock_board
        gameplay.color_on_play = "B"

        gameplay.get_valid_moves()
        
        expected = True

        assert expected == gameplay.checkmate

    @unittest.mock.patch('src.board.super')
    @unittest.mock.patch('src.pieces.piece.super')
    def test_arabian_mate(self, mock_board_super, mock_piece_super):
        mock_board = Board("B")
        mock_board.board_state = [
                [None,None,None,None,None,None,Tower("W", "TBD"),King("B", "TBD")],
                [None,None,None,None,None,None,None, None],
                [None,None,None,None,None,Knight("W", "TBD"),None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,King("W", "TBD")]
            ]

        gameplay = Gameplay("W", mock_janela, None)

        gameplay.white_king_location = (7,7)
        gameplay.black_king_location = (0,7)
        gameplay.board = mock_board
        gameplay.color_on_play = "B"

        gameplay.get_valid_moves()
        
        expected = True

        assert expected == gameplay.checkmate

    @unittest.mock.patch('src.board.super')
    @unittest.mock.patch('src.pieces.piece.super')
    def test_fools_mate(self, mock_board_super, mock_piece_super):
        mock_board = Board("B")
        mock_board.board_state = [
                [Tower("B", "TBD"),Knight("B", "TBD"),Bishop("B", "TBD"),None,King("B", "TBD"),Bishop("B", "TBD"),Knight("B", "TBD"),Tower("B", "TBD")],
                [Pawn("B", "TBD", 1),Pawn("B", "TBD", 1),Pawn("B", "TBD", 1),None,Pawn("B", "TBD", 1),Pawn("B", "TBD", 1),Pawn("B", "TBD", 1), Pawn("B", "TBD", 1)],
                [None,None,None,Pawn("B", "TBD", 1),None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,Pawn("W", "TBD", -1),Queen("B", "TBD")],
                [None,None,None,None,None,Pawn("W", "TBD", -1),None,None],
                [Pawn("W", "TBD", -1),Pawn("W", "TBD", -1),Pawn("W", "TBD", -1),Pawn("W", "TBD", -1),Pawn("W", "TBD", -1),None,None,Pawn("W", "TBD", -1)],
                [Tower("W", "TBD"),Knight("W", "TBD"),Bishop("W", "TBD"),Queen("W", "TBD"),King("W", "TBD"),Bishop("W", "TBD"),Knight("W", "TBD"),Tower("W", "TBD")]
            ]

        gameplay = Gameplay("W", mock_janela, None)

        gameplay.white_king_location = (7,4)
        gameplay.black_king_location = (0,4)
        gameplay.board = mock_board
        gameplay.color_on_play = "W"

        gameplay.get_valid_moves()
        
        expected = True

        assert expected == gameplay.checkmate

    @unittest.mock.patch('src.board.super')
    @unittest.mock.patch('src.pieces.piece.super')
    def test_scholars_mate(self, mock_board_super, mock_piece_super):
        mock_board = Board("B")
        mock_board.board_state = [
            [Tower("B", "TBD"),Knight("B", "TBD"),Bishop("B", "TBD"),Queen("B", "TBD"),King("B", "TBD"),None,None,Tower("B", "TBD")],
            [Pawn("B", "TBD", 1),Pawn("B", "TBD", 1),Pawn("B", "TBD", 1),Pawn("B", "TBD", 1),None,Queen("W", "TBD"),Pawn("B", "TBD", 1), Pawn("B", "TBD", 1)],
            [None,None,None,None,None,Knight("B", "TBD"),None,None],
            [None,None,Bishop("B", "TBD"),None,Pawn("B", "TBD", 1),None,None,None],
            [None,None,Bishop("W", "TBD"),None,Pawn("W", "TBD", -1),None,None,None],
            [None,None,None,None,None,None,None,None],
            [Pawn("W", "TBD", -1),Pawn("W", "TBD", -1),Pawn("W", "TBD", -1),Pawn("W", "TBD", -1),None,Pawn("W", "TBD", -1),Pawn("W", "TBD", -1),Pawn("W", "TBD", -1)],
            [Tower("W", "TBD"),Knight("W", "TBD"),Bishop("W", "TBD"),None,King("W", "TBD"),None,Knight("W", "TBD"),Tower("W", "TBD")]
        ]

        gameplay = Gameplay("W", mock_janela, None)

        gameplay.white_king_location = (7,4)
        gameplay.black_king_location = (0,4)
        gameplay.board = mock_board
        gameplay.color_on_play = "B"

        gameplay.get_valid_moves()
        
        expected = True

        assert expected == gameplay.checkmate

    @unittest.mock.patch('src.board.super')
    @unittest.mock.patch('src.pieces.piece.super')
    def test_legals_mate(self, mock_board_super, mock_piece_super):
        mock_board = Board("B")
        mock_board.board_state = [
                [Tower("B", "TBD"),None,None,Queen("B", "TBD"),None,Bishop("B", "TBD"),Knight("B", "TBD"),Tower("B", "TBD")],
                [Pawn("B", "TBD", 1),Pawn("B", "TBD", 1),Pawn("B", "TBD", 1),None,King("B", "TBD"),Bishop("W", "TBD"),Pawn("B", "TBD", 1), Pawn("B", "TBD", 1)],
                [None,None,Knight("B", "TBD"),Pawn("B", "TBD", 1),None,None,None,None],
                [None,None,None,Knight("W", "TBD"),Knight("W", "TBD"),None,None,None],
                [None,None,None,None,Pawn("W", "TBD", -1),None,None,None],
                [None,None,None,None,None,None,None,None],
                [Pawn("W", "TBD", -1),Pawn("W", "TBD", -1),Pawn("W", "TBD", -1),Pawn("W", "TBD", -1),None,Pawn("W", "TBD", -1),Pawn("W", "TBD", -1),Pawn("W", "TBD", -1)],
                [Tower("W", "TBD"),None,Bishop("W", "TBD"),Bishop("B", "TBD"),King("W", "TBD"),None,None,Tower("W", "TBD")]
            ]

        gameplay = Gameplay("W", mock_janela, None)

        gameplay.white_king_location = (7,4)
        gameplay.black_king_location = (1,4)
        gameplay.board = mock_board
        gameplay.color_on_play = "B"

        gameplay.get_valid_moves()
        
        expected = True

        assert expected == gameplay.checkmate

    @unittest.mock.patch('src.board.super')
    @unittest.mock.patch('src.pieces.piece.super')
    def test_back_rank_mate(self, mock_board_super, mock_piece_super):
        mock_board = Board("B")
        mock_board.board_state = [
                [None,None,None,None,None,Tower("W", "TBD"),None,King("B", "TBD")],
                [None,None,None,None,None,Pawn("B", "TBD", 1),Pawn("B", "TBD", 1), Pawn("B", "TBD", 1)],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,Pawn("W", "TBD", -1),Pawn("W", "TBD", -1),Pawn("W", "TBD", -1)],
                [None,None,None,None,None,None,King("W", "TBD"),None]
            ]

        gameplay = Gameplay("W", mock_janela, None)

        gameplay.white_king_location = (7,6)
        gameplay.black_king_location = (0,7)
        gameplay.board = mock_board
        gameplay.color_on_play = "B"

        gameplay.get_valid_moves()
        
        expected = True

        assert expected == gameplay.checkmate
    
    @unittest.mock.patch('src.board.super')
    @unittest.mock.patch('src.pieces.piece.super')
    def test_smothered_mate(self, mock_board_super, mock_piece_super):
        mock_board = Board("B")
        mock_board.board_state = [
                [Tower("W", "TBD"),None,None,None,None,None,Tower("W", "TBD"),King("B", "TBD")],
                [None,None,None,None,None,Knight("W", "TBD"),Pawn("B", "TBD", 1), Pawn("B", "TBD", 1)],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,Pawn("W", "TBD", -1)],
                [None,None,None,None,None,Pawn("W", "TBD", -1),Pawn("W", "TBD", -1),None],
                [None,None,None,None,None,None,King("W", "TBD"),None]
            ]

        gameplay = Gameplay("W", mock_janela, None)

        gameplay.white_king_location = (7,6)
        gameplay.black_king_location = (0,7)
        gameplay.board = mock_board
        gameplay.color_on_play = "B"

        gameplay.get_valid_moves()
        
        expected = True

        assert expected == gameplay.checkmate

    @unittest.mock.patch('src.board.super')
    @unittest.mock.patch('src.pieces.piece.super')
    def test_anastatias_mate(self, mock_board_super, mock_piece_super):
        mock_board = Board("B")
        mock_board.board_state = [
                [None,None,Queen("B", "TBD"),None,None,Tower("W", "TBD"),None,None],
                [None,None,None,None,Knight("W", "TBD"),Pawn("B", "TBD", 1),Pawn("B", "TBD", 1), King("B", "TBD")],
                [None,None,None,None,None,None,None,None],
                [None,None,Knight("B", "TBD"),None,None,None,None,None],
                [None,None,None,None,None,None,None,Tower("W", "TBD")],
                [None,None,None,None,None,None,None,Pawn("W", "TBD", -1)],
                [None,None,None,None,None,Pawn("W", "TBD", -1),Pawn("W", "TBD", -1),None],
                [None,None,None,None,None,None,King("W", "TBD"),None]
            ]

        gameplay = Gameplay("W", mock_janela, None)

        gameplay.white_king_location = (7,6)
        gameplay.black_king_location = (1,7)
        gameplay.board = mock_board
        gameplay.color_on_play = "B"

        gameplay.get_valid_moves()
        
        expected = True

        assert expected == gameplay.checkmate