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


class TestStalemate():

    @unittest.mock.patch('src.board.super')
    @unittest.mock.patch('src.pieces.piece.super')
    def test_1(self, mock_board_super, mock_piece_super):
        mock_board = Board("B")
        mock_board.board_state = [
                [King("B", "TBD"),None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,Queen("B", "TBD"),None,None],
                [None,None,None,None,None,None,None,King("W", "TBD")]
            ]

        gameplay = Gameplay("W", mock_janela, None)
        gameplay.board = mock_board

        gameplay.white_king_location = (7,7)
        gameplay.black_king_location = (0,0)
        gameplay.color_on_play = "W"

        gameplay.get_valid_moves()
        
        expected = True

        assert expected == gameplay.stalemate
    
    @unittest.mock.patch('src.board.super')
    @unittest.mock.patch('src.pieces.piece.super')
    def test_2(self, mock_board_super, mock_piece_super):
        mock_board = Board("B")
        mock_board.board_state = [
                [None,None,None,None,None,None,King("B", "TBD"),None],
                [None,None, None,None,None,None,Pawn("W", "TBD", -1),None],
                [None,None,None,None,None,None,King("W", "TBD"),None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None]
            ]

        gameplay = Gameplay("W", mock_janela, None)
        gameplay.board = mock_board

        gameplay.white_king_location = (0,6)
        gameplay.black_king_location = (2,6)
        gameplay.color_on_play = "B"

        gameplay.get_valid_moves()
        
        expected = True

        assert expected == gameplay.stalemate
    
    @unittest.mock.patch('src.board.super')
    @unittest.mock.patch('src.pieces.piece.super')
    def test_3(self, mock_board_super, mock_piece_super):
        mock_board = Board("B")
        mock_board.board_state = [
                [King("B", "TBD"),Bishop("B", "TBD"),None,None,None,None,None,Tower("W", "TBD")],
                [None,None, None,None,None,None,None,None],
                [None,King("W", "TBD"),None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None]
            ]

        gameplay = Gameplay("W", mock_janela, None)
        gameplay.board = mock_board

        gameplay.white_king_location = (2,1)
        gameplay.black_king_location = (0,0)
        gameplay.color_on_play = "B"

        gameplay.get_valid_moves()
        
        expected = True

        assert expected == gameplay.stalemate
    
    @unittest.mock.patch('src.board.super')
    @unittest.mock.patch('src.pieces.piece.super')
    def test_4(self, mock_board_super, mock_piece_super):
        mock_board = Board("B")
        mock_board.board_state = [
                [None,None,None,None,None,None,None,None],
                [None,None, None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,King("W", "TBD"),None,None,None,None,None],
                [None,Tower("W", "TBD"),None,None,None,None,None,None],
                [King("B", "TBD"),None,None,None,None,None,None,None]
            ]

        gameplay = Gameplay("W", mock_janela, None)
        gameplay.board = mock_board

        gameplay.white_king_location = (2,1)
        gameplay.black_king_location = (0,0)
        gameplay.color_on_play = "B"

        gameplay.get_valid_moves()
        
        expected = True

        assert expected == gameplay.stalemate

    @unittest.mock.patch('src.board.super')
    @unittest.mock.patch('src.pieces.piece.super')
    def test_5(self, mock_board_super, mock_piece_super):
        mock_board = Board("B")
        mock_board.board_state = [
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,King("W", "TBD"),Bishop("W", "TBD"),King("B", "TBD")],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [Pawn("B", "TBD", 1),None,None,None,None,None,None,None],
                [Pawn("W", "TBD", -1),None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None]
            ]

        gameplay = Gameplay("W", mock_janela, None)
        gameplay.board = mock_board

        gameplay.white_king_location = (1,5)
        gameplay.black_king_location = (1,7)
        gameplay.color_on_play = "B"

        gameplay.get_valid_moves()
        
        expected = True

        assert expected == gameplay.stalemate
