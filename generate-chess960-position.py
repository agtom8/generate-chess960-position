# 09/08/2019 ATOM
# https://chess960.net/start-positions/
import random
import sys

class ChessPiece:
    """Chess piece class"""
    def __init__(self, piece_name, valid_squares):
        """Chess piece constructor method"""
        self.piece_name = piece_name
        self.start_square = random.choice(valid_squares)
#
def main():
    """Entry point of the program"""
    # Squares initialization
    position = dict()                                                           # position to be set randomly on the first rank
    cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']                             # board columns
    rows = 1               # only the first row matters as pawns get set as in regular game, and black pieces get mirror position across the median on the 8th row
    avail_squares = [char+str(rows) for char in cols]                           # available squares - a1, b1, etc.
    dark_squares = [cols[i]+str(rows) for i in range(len(cols)) if i % 2 != 0]  # dark squares are odd count columns on the first rank
    light_squares = [cols[i]+str(rows) for i in range(len(cols)) if i % 2 == 0] # light squares are even count columns

    # king piece to be placed first; it must be between rooks to preserve castling possibility in either direction
    king = ChessPiece('K',avail_squares[1:7])
    position[king.start_square] = king.piece_name

    # rooks must be on either side of king
    left_hand_rook = ChessPiece('R',avail_squares[0:avail_squares.index(king.start_square)])
    avail_squares.remove(left_hand_rook.start_square)
    position[left_hand_rook.start_square] = left_hand_rook.piece_name
    #
    right_hand_rook = ChessPiece('R',avail_squares[avail_squares.index(king.start_square)+1:len(cols)])
    avail_squares.remove(right_hand_rook.start_square)
    position[right_hand_rook.start_square] = right_hand_rook.piece_name

    # now we can remove the king's square from avail_squares as no other piece's position depends on it
    avail_squares.remove(king.start_square)

    # set positions for dark and light square bishops
    avail_dark_squares = [cols[i]+str(rows) for i in range(len(cols)) if cols[i]+str(rows) in dark_squares and cols[i]+str(rows) in avail_squares]
    dark_square_bishop = ChessPiece('B',avail_dark_squares)
    avail_squares.remove(dark_square_bishop.start_square)
    position[dark_square_bishop.start_square] = dark_square_bishop.piece_name
    #
    avail_light_squares = [cols[i]+str(rows) for i in range(len(cols)) if cols[i]+str(rows) in light_squares and cols[i]+str(rows) in avail_squares]
    light_square_bishop = ChessPiece('B',avail_light_squares)
    avail_squares.remove(light_square_bishop.start_square)
    position[light_square_bishop.start_square] = light_square_bishop.piece_name

    # the knights and queen get what's left
    knight_1 = ChessPiece('N',avail_squares)
    avail_squares.remove(knight_1.start_square)
    position[knight_1.start_square] = knight_1.piece_name
    #
    knight_2 = ChessPiece('N',avail_squares)
    avail_squares.remove(knight_2.start_square)
    position[knight_2.start_square] = knight_2.piece_name

    # no disrespect, but queen gets the last available square in the same manner
    queen = ChessPiece('Q',avail_squares)
    avail_squares.remove(queen.start_square)
    position[queen.start_square] = queen.piece_name

    # print the position
    for char in cols:
        sys.stdout.write(position[char+str(rows)]+char+str(rows)+' ')
    sys.stdout.write('\n')

if __name__ == '__main__':
    main()
