import cv2 as cv
import numpy as np
from cv.window_capture import WindowCapture
from cv.piece_finder import PieceFinder
from cv.values import OtherValues as values


class Formater:
    win_cap = None
    finder = None

    letters = values.letters
    numbers = values.numbers
    size = values.size

    def __init__(self, win_cap: WindowCapture, finder: PieceFinder) -> None:
        self.win_cap = win_cap
        self.finder = finder

    def format_to_fen(self, screenshot: np.ndarray) -> str:
        pieces_on_board = self.get_pieces_on_board(screenshot)

        return pieces_on_board

    def get_pieces_on_board(self, screenshot: np.ndarray, chessboard_dict: dict) -> dict:
        pieces_on_board = {}

        for number in self.numbers:
            for letter in self.letters:
                pieces_on_board[number + letter] = None

        # screenshot = self.win_cap.get_screenshot()
        # screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)

        all_points_dict = self.__get_all_points(screenshot)
        # chessboard_dict = self.get_chessboard_dict(screenshot)

        result_dict = {}
        square_w, square_h = self.finder.square_size

        for key, position in chessboard_dict.items():
            board_x, board_y = position[0]
            for piece, coords in all_points_dict.items():
                for x, y in coords:
                    if x > board_x and y > board_y and x < board_x + square_w and y < board_y + square_h:
                        result_dict[piece] = key

        return result_dict

    def __get_all_points(self, screenshot: np.ndarray) -> dict:
        w_r_points = self.finder.find_white_rook(screenshot)
        b_r_points = self.finder.find_black_rook(screenshot)

        w_n_points = self.finder.find_white_knight(screenshot)
        b_n_points = self.finder.find_black_knight(screenshot)

        w_b_points = self.finder.find_white_bishop(screenshot)
        b_b_points = self.finder.find_black_bishop(screenshot)

        w_q_points = self.finder.find_white_queen(screenshot)
        b_q_points = self.finder.find_black_queen(screenshot)

        w_k_points = self.finder.find_white_king(screenshot)
        b_k_points = self.finder.find_black_king(screenshot)

        w_p_points = self.finder.find_white_pawn(screenshot)
        b_p_points = self.finder.find_black_pawn(screenshot)

        return {
            "R": w_r_points,
            "r": b_r_points,
            "N": w_n_points,
            "n": b_n_points,
            "B": w_b_points,
            "b": b_b_points,
            "Q": w_q_points,
            "q": b_q_points,
            "K": w_k_points,
            "k": b_k_points,
            "P": w_p_points,
            "p": b_p_points,
        }

    def get_chessboard_dict(self, screenshot: np.ndarray) -> dict:
        chessboard_dict = self.finder.set_chessboard(screenshot)

        inverted_dict = {}

        for key, nested_dict in chessboard_dict.items():
            for nested_key, value in nested_dict.items():
                if value not in inverted_dict:
                    inverted_dict[value] = []
                inverted_dict[value].append((nested_key, key))

        return inverted_dict
