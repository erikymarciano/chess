import unittest
from ..pieces.queen import *

class MockPiece():
    def __init__(self, name, color, image_file, frames=1):
        self.name = name
        self.color = color
        self.image_file = image_file

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

mock_position_1 = (6,4)
mock_position_2 = (3,7)
mock_position_3 = (3,1)


class TestQueen:

    @unittest.mock.patch('src.pieces.piece.super')
    def test_move(self, mock_super):
        obj = Queen('W', 'TBD')

        expected = [(5, 4), (6, 3), (5, 3), (4, 2), (7, 3), (5, 5), (4, 6)]
        response = obj.move(mock_position_1, MockBoard)
        assert expected == response
        expected = [(4, 7), (5, 7), (2, 7), (1, 7), (2, 6), (4, 6), (5, 5), (6, 4), (7, 3)]
        response = obj.move(mock_position_2, MockBoard)
        assert expected == response
        expected = [(4, 1), (5, 1), (3, 2), (3, 3), (3, 4), (3, 5), (4, 2), (5, 3), (6, 4), (2, 1), (1, 1), (3, 0), (2, 0), (4, 0), (2, 2)]
        response = obj.move(mock_position_3, MockBoard)
        assert expected == response

    @unittest.mock.patch('src.pieces.piece.super')
    def test_attack(self, mock_super):
        obj = Queen('W', 'TBD')

        expected = [(3, 1), (3, 7)]
        response = obj.attack(mock_position_1, MockBoard)
        assert expected == response
        expected = [(0, 7), (3, 6), (1, 5)]
        response = obj.attack(mock_position_2, MockBoard)
        assert expected == response
        expected = [(3, 6), (0, 1), (1, 3)]
        response = obj.attack(mock_position_3, MockBoard)
        assert expected == response