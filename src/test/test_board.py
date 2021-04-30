import unittest
from ..board import *

class MockPiece():
    def __init__(self, name, color, image_file, frames=1):
        self.name = name
        self.color = color
        self.image_file = image_file
        self.en_passant = False
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
    
    def draw(self):
        pass

mock_piece_white = MockPiece('Peão', 'W', 'TBD')
mock_piece_black = MockPiece('Peão', 'B', 'TBD')

class MockBoard():
    board_state = [
        [mock_piece_black,mock_piece_black,mock_piece_black,mock_piece_black,mock_piece_black,mock_piece_black,mock_piece_black,mock_piece_black],
        [mock_piece_black,None,mock_piece_black,mock_piece_black,mock_piece_black,mock_piece_black,None,None],
        [None,None,None,None,None,None,None,None],
        [None,mock_piece_black,None,None,None,None,mock_piece_black,mock_piece_black],
        [None,None,None,mock_piece_white,mock_piece_white,None,None,None],
        [None,None,None,None,None,None,None,None],
        [mock_piece_white,mock_piece_white,mock_piece_white,None,None,mock_piece_white,mock_piece_white,mock_piece_white],
        [mock_piece_white,mock_piece_white,mock_piece_white,None,mock_piece_white,mock_piece_white,mock_piece_white,mock_piece_white]
    ]

mock_position_1 = (372,272)

class TestBoard:

    @unittest.mock.patch('src.board.super')
    @unittest.mock.patch('src.pieces.piece.super')
    @unittest.mock.patch('PPlay.animation.Animation.set_total_duration')
    def test_initial_state(self, mock_board_super, mock_piece_super, mock_piece_total_duration):
        obj = Board('W')
        response = obj.initial_state('W')
        assert [(7, 4), (0, 4)] == response
        obj = Board('B')
        response = obj.initial_state('B')
        assert [(0, 4), (7, 4)] == response

    @unittest.mock.patch('src.board.super')
    def test_get_all_pieces_from_color(self, mock_board_super):
        obj = Board('W')
        obj.board_state = MockBoard.board_state
        response = obj.get_all_pieces_from_color('W')
        expected = [(4, 3), (4, 4), (6, 0), (6, 1), (6, 2), (6, 5), (6, 6), (6, 7), (7, 0), (7, 1), (7, 2), (7, 4), (7, 5), (7, 6), (7, 7)]
        assert expected == response

    @unittest.mock.patch('src.board.super')
    def test_get_all_pieces_from_name_color(self, mock_board_super):
        obj = Board('W')
        obj.board_state = MockBoard.board_state
        response = obj.get_all_pieces_from_name_color('Peão', 'W')
        expected = [(4, 3), (4, 4), (6, 0), (6, 1), (6, 2), (6, 5), (6, 6), (6, 7), (7, 0), (7, 1), (7, 2), (7, 4), (7, 5), (7, 6), (7, 7)]
        assert expected == response

    @unittest.mock.patch('src.board.super')
    def test_clean_all_en_passant(self, mock_board_super):
        obj = Board('W')
        obj.board_state = MockBoard.board_state
        response = obj.clean_all_en_passant('W')
        expected = None
        assert expected == response
    
    @unittest.mock.patch('src.board.super')
    @unittest.mock.patch('PPlay.gameimage.GameImage.draw')
    def test_draw_board_state(self, mock_board_super, mock_game_image_draw):
        obj = Board('W')
        obj.board_state = MockBoard.board_state
        obj.x = 0
        obj.y = 0
        response = obj.draw_board_state()
        expected = None
        assert expected == response
    
    @unittest.mock.patch('src.board.super')
    def test_position_to_index(self, mock_board_super):
        obj = Board('W')
        obj.board_state = MockBoard.board_state
        obj.x = 344
        obj.y = 74
        response = obj.position_to_index(mock_position_1)
        expected = (3,0)
        assert expected == response
