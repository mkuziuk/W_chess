from board_setup import SetupBoard
from cv.window_capture import WindowCapture
from cv.piece_finder import PieceFinder
from cv.values import OtherValues as values


class Formatter:
    # active_color = "b"
    blank = "-"

    letters = values.letters
    numbers = values.numbers
    size = values.size

    def __init__(self, players_color: str):
        self.players_color = players_color
        # self.win_cap = WindowCapture(2560, 1440)
        # self.finder = PieceFinder(self.win_cap)
        # self.setup = Setup(self.win_cap, self.finder)
        ...

    def convert_to_fen(self, pieces_dict: dict, setup: SetupBoard) -> str:
        fen = ""

        for rank in range(7, -1, -1):  # Loop through ranks in reverse order
            empty_squares = 0

            for file in range(8):  # Loop through files
                square = f"{self.letters[file]}{self.numbers[rank]}"  # Get square code

                if square in pieces_dict:
                    piece = pieces_dict[square]
                    if empty_squares > 0:
                        fen += str(empty_squares)
                        empty_squares = 0
                    fen += piece
                else:
                    empty_squares += 1

            if empty_squares > 0:
                fen += str(empty_squares)

            if rank > 0:
                fen += "/"

        # print(fen)

        # Replace consecutive "0" with there sum
        count = 0
        fen_list = list(fen)
        for i in range(len(fen_list)):
            if fen_list[i] == "0":
                count += 1
                if i == len(fen_list) - 1:
                    fen_list[i] = str(count)
            else:
                if count > 0:
                    fen_list[i - 1] = str(count)
                count = 0

        fen = "".join(fen_list)
        fen = fen.replace("0", "")

        fen_reversed_list = fen.split("/")[::-1]
        fen_result = ""
        for i in range(len(fen_reversed_list)):
            if i == len(fen_reversed_list) - 1:
                fen_result += fen_reversed_list[i]
                continue
            fen_result += fen_reversed_list[i] + "/"

        # setup = SetupBoard(self.win_cap, self.finder)
        castle_str = setup.check_castling()

        halfmove_number = values.halfmove_number

        full_move_number = setup.get_fullmove_number()

        fen_result += (
            " "
            + self.players_color
            + " "
            + castle_str
            + " "
            + self.blank
            + " "
            + str(halfmove_number)
            + " "
            + str(full_move_number)
        )

        return fen_result
