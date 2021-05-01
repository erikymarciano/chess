import unittest
from ..pieces.bishop import *

class MockPiece():
    def __init__(self, name, color, image_file, frames=1):
        self.name = name
        self.color = color
        self.image_file = image_file

mock_piece_white = MockPiece('Peão', 'W', 'TBD')
mock_piece_black = MockPiece('Peão', 'B', 'TBD')


class MockBoard():
    board_state = [
        [mock_piece_black , mock_piece_black , mock_piece_black , mock_piece_black , None             , mock_piece_black , mock_piece_black , mock_piece_black],
        [mock_piece_black , None             , mock_piece_black , mock_piece_black , mock_piece_black , None             , mock_piece_black , mock_piece_black],
        [None             , None             , None             , None             , None             , None             , None             , None            ],
        [None             , mock_piece_black , None             , mock_piece_black , None             , None             , None             , mock_piece_white],
        [None             , None             , None             , None             , mock_piece_white , mock_piece_black , None             , None            ],
        [mock_piece_white , None             , mock_piece_white , None             , None             , None             , None             , mock_piece_white],
        [None             , mock_piece_white , mock_piece_white , mock_piece_white , None             , mock_piece_white , mock_piece_white , mock_piece_white],
        [mock_piece_white , None             , mock_piece_white , None             , mock_piece_white , mock_piece_white , None             , mock_piece_white]
    ]

mock_position_1 = (6, 2)
mock_position_2 = (5, 2)
mock_position_3 = (1, 0)
mock_position_4 = (2, 0)

class TestPawn:

    @unittest.mock.patch('src.pieces.piece.super')
    def test_move(self, mock_super):
        obj = Bishop('W', 'TBD', -1)

        expected = [(7, 3), (5, 1), (4, 0), (7, 1), (5, 3)]
        response = obj.move(mock_position_1, MockBoard)
        assert expected == response



        obj = Bishop('B', 'TBD', 1)

        expected = [(2, 1), (3, 2), (4, 3), (5, 4)]
        response = obj.move(mock_position_3, MockBoard)
        assert expected == response


    @unittest.mock.patch('src.pieces.piece.super')
    def test_attack(self, mock_super):
        mock_position_5 = (2, 3)
        obj = Bishop('W', 'TBD', -1)

        expected = [(4, 5), (1, 2), (1, 4)]
        response = obj.attack(mock_position_5, MockBoard)
        assert expected == response

        obj = Bishop('B', 'TBD', 1)
        mock_position_6 = (3, 3)

        expected = [(4,4)]
        response = obj.attack(mock_position_6, MockBoard)
        assert expected == response