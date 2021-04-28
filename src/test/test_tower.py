import unittest
from ..pieces.tower import *

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
        [mock_piece_black,None,mock_piece_black,mock_piece_black,mock_piece_black,mock_piece_black,mock_piece_black,mock_piece_black],
        [None,None,None,None,None,None,None,None],
        [None,mock_piece_white,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None],
        [None,mock_piece_white,mock_piece_white,mock_piece_white,mock_piece_white,mock_piece_white,mock_piece_white,mock_piece_white],
        [mock_piece_white,mock_piece_white,mock_piece_white,mock_piece_white,mock_piece_white,mock_piece_white,mock_piece_white,mock_piece_white]
    ]

mockPosition = (7,0)

class TestTower:

    @unittest.mock.patch('src.pieces.piece.super')
    def test_move(self, mock_super):
        obj = Tower('W', 'TBD')
        expected = [(6,0), (5,0), (4,0), (3,0), (2,0)]
        response = obj.move(mockPosition, MockBoard)
        assert expected == response

    @unittest.mock.patch('src.pieces.piece.super')
    def test_attack(self, mock_super):
        obj = Tower('W', 'TBD')
        expected = [(1,0)]
        response = obj.attack(mockPosition, MockBoard)
        assert expected == response
