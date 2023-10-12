from stockfish import Stockfish
from board_setup import Setup

stockfish = Stockfish(
    path=r"C:\Users\mkuzyuk\Projects\ProjectsPy\Stockfish\stockfish\stockfish-windows-x86-64-avx2.exe",
    depth=22,
    parameters={"Hash": 4096, "Threads": 8},
)

playing = True


while playing:
    position = input("Enter the fen postion or 'q' to quit: ")

    if position == "q":
        break

    if stockfish.is_fen_valid(position):
        stockfish.set_fen_position(position)
        print(stockfish.get_board_visual())
        print(stockfish.get_top_moves(3))


class Fish:
    stockfish = Stockfish

    def __init__(self, stockfish: Stockfish):
        self.position = position

    def position_to_fen(self):
        position

        return 0
