from board_setup import Setup
from cv.window_capture import WindowCapture
from cv.piece_finder import PieceFinder


class Formatter:
    def __init__(self):
        self.win_cap = WindowCapture(2560, 1440)
        self.finder = PieceFinder(self.win_cap)
        self.setup = Setup(self.win_cap, self.finder)

    def convert_to_fen(pieces_dict: dict) -> str:
        # Mapping of piece codes to FEN symbols
        piece_mapping = {
            "R": "R",
            "N": "N",
            "B": "B",
            "Q": "Q",
            "K": "K",
            "P": "P",
            "r": "r",
            "n": "n",
            "b": "b",
            "q": "q",
            "k": "k",
            "p": "p",
        }

        fen = ""
        empty_squares = 0

        for rank in range(7, -1, -1):  # Loop through ranks in reverse order
            for file in range(8):  # Loop through files
                square = (
                    f"{Setup.letters[file]}{Setup.numbers[rank]}"  # Get square code
                )

                if square in pieces_dict:
                    piece = pieces_dict[square]
                    fen += piece_mapping.get(
                        piece, piece
                    )  # Add FEN symbol if found in mapping
                    empty_squares = 0  # Reset empty square count
                else:
                    empty_squares += 1

                if empty_squares > 0 and (file == 7 or square in pieces_dict):
                    fen += str(empty_squares)  # Add count of consecutive empty squares
                    empty_squares = 0

            if rank > 0:
                fen += "/"

        return fen
