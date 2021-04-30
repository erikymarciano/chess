import unittest
from ..pieces.knight import *

class MockPiece():
    def __init__(self, name, color, image_file, frames=1):
        self.name = name
        self.color = color
        self.image_file = image_file

mock_piece_white = MockPiece('Peão', 'W', 'TBD')
mock_piece_black = MockPiece('Peão', 'B', 'TBD')


class MockBoard():
    board_state = [
        [mock_piece_black,mock_piece_black,mock_piece_black,mock_piece_black,None,mock_piece_black,mock_piece_black,mock_piece_black],
        [mock_piece_black,None,mock_piece_black,mock_piece_black,mock_piece_black,None,mock_piece_black,mock_piece_black],
        [None,None,None,None,None,None,None,None],
        [None,mock_piece_black,None,mock_piece_black,None,None,None,mock_piece_white],
        [None,None,None,None,mock_piece_white,mock_piece_black,None,None],
        [mock_piece_white,None,mock_piece_white,None,None,None,None,mock_piece_white],
        [None,mock_piece_white,mock_piece_white,mock_piece_white,None,mock_piece_white,mock_piece_white,mock_piece_white],
        [mock_piece_white,None,mock_piece_white,None,mock_piece_white,mock_piece_white,None,mock_piece_white]
    ]

mock_position_1 = (5,2)
mock_position_2 = (5,7)
mock_position_3 = (0,1)
mock_position_4 = (0,6)


class TestKnight:

    @unittest.mock.patch('src.pieces.piece.super')
    def test_move(self, mock_super):
        obj = Knight('W', 'TBD')

        expected = [(7, 1), (7, 3), (6, 4), (4, 0), (6, 0)]
        response = obj.move(mock_position_1, MockBoard)
        assert expected == response
        expected = [(7, 6), (3, 6)]
        response = obj.move(mock_position_2, MockBoard)
        assert expected == response

        obj = Knight('B', 'TBD')

        expected = [(2, 0), (2, 2)]
        response = obj.move(mock_position_3, MockBoard)
        assert expected == response
        expected = [(2, 5), (2, 7)]
        response = obj.move(mock_position_4, MockBoard)
        assert expected == response

    @unittest.mock.patch('src.pieces.piece.super')
    def test_attack(self, mock_super):
        obj = Knight('W', 'TBD')

        expected = [(3, 1), (3, 3)]
        response = obj.attack(mock_position_1, MockBoard)
        assert expected == response
        expected = [(4, 5)]
        response = obj.attack(mock_position_2, MockBoard)
        assert expected == response

        obj = Knight('B', 'TBD')

        expected = []
        response = obj.attack(mock_position_3, MockBoard)
        assert expected == response
        expected = []
        response = obj.attack(mock_position_4, MockBoard)
        assert expected == response