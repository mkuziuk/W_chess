import numpy as np
from .window_capture import WindowCapture
from .values import VisionPaths as vp
from .values import OtherValues as values


class PieceFinder:
    win_cap = None
    letters = values.letters
    numbers = values.numbers
    size = values.size
    square_size = ()

    def __init__(self, win_cap: WindowCapture):
        self.win_cap = win_cap

    def find_white_rook(self, screenshot: np.ndarray) -> list:
        w_r_pos = vp.vision_white_rook.find_item(
            screenshot,
            threshold=0.6,
            debug_mode="rectangles",
        )
        w_r_pos2 = vp.vision_white_rook2.find_item(
            screenshot,
            threshold=0.7,
            debug_mode="rectangles",
        )

        w_r_pts, w_r_rects = w_r_pos
        w_r_pts2, w_r_rects2 = w_r_pos2

        return w_r_pts + w_r_pts2

    def find_black_rook(self, screenshot: np.ndarray) -> list:
        b_r_pos = vp.vision_black_rook.find_item(
            screenshot,
            threshold=0.7,
            debug_mode="rectangles",
        )

        b_r_pts, b_r_rects = b_r_pos

        return b_r_pts

    def find_white_knight(self, screenshot: np.ndarray) -> list:
        w_n_pos = vp.vision_white_knight.find_item(
            screenshot,
            threshold=0.7,
            debug_mode="rectangles",
        )
        w_n_pos2 = vp.vision_white_knight2.find_item(
            screenshot,
            threshold=0.7,
            debug_mode="rectangles",
        )

        w_n_pts, w_n_rects = w_n_pos
        w_n_pts2, w_n_rects2 = w_n_pos2

        return w_n_pts + w_n_pts2

    def find_black_knight(self, screenshot: np.ndarray) -> list:
        b_n_pos = vp.vision_black_knight.find_item(
            screenshot,
            threshold=0.9,
            debug_mode="rectangles",
        )

        b_n_pts, b_n_rects = b_n_pos

        return b_n_pts

    def find_white_bishop(self, screenshot: np.ndarray) -> list:
        w_b_pos = vp.vision_white_bishop.find_item(
            screenshot,
            threshold=0.7,
            debug_mode="rectangles",
        )
        w_b_pos2 = vp.vision_white_bishop2.find_item(
            screenshot,
            threshold=0.7,
            debug_mode="rectangles",
        )

        w_b_pts, w_b_rects = w_b_pos
        w_b_pts2, w_b_rects2 = w_b_pos2

        return w_b_pts + w_b_pts2

    def find_black_bishop(self, screenshot: np.ndarray) -> list:
        b_b_pos = vp.vision_black_bishop.find_item(
            screenshot,
            threshold=0.9,
            debug_mode="rectangles",
        )

        b_b_pts, b_b_rects = b_b_pos

        return b_b_pts

    def find_white_queen(self, screenshot: np.ndarray) -> list:
        w_q_pos = vp.vision_white_queen.find_item(
            screenshot,
            threshold=0.9,
            debug_mode="rectangles",
        )

        w_q_pts, w_q_rects = w_q_pos

        return w_q_pts

    def find_black_queen(self, screenshot: np.ndarray) -> list:
        b_q_pos = vp.vision_black_queen.find_item(
            screenshot,
            threshold=0.9,
            debug_mode="rectangles",
        )

        b_q_pts, b_q_rects = b_q_pos

        return b_q_pts

    def find_white_king(self, screenshot: np.ndarray) -> list:
        w_k_pos = vp.vision_white_king.find_item(
            screenshot,
            threshold=0.9,
            debug_mode="rectangles",
        )

        w_k_pts, w_k_rects = w_k_pos

        return w_k_pts

    def find_black_king(self, screenshot: np.ndarray) -> list:
        b_k_pos = vp.vision_black_king.find_item(
            screenshot,
            threshold=0.9,
            debug_mode="rectangles",
        )

        b_k_pts, b_k_rects = b_k_pos

        return b_k_pts

    def find_white_pawn(self, screenshot: np.ndarray) -> list:
        w_p_pos = vp.vision_white_pawn.find_item(
            screenshot,
            threshold=0.9,
            debug_mode="rectangles",
        )
        w_p_pos2 = vp.vision_white_pawn2.find_item(
            screenshot,
            threshold=0.9,
            debug_mode="rectangles",
        )

        w_p_pts, w_p_rects = w_p_pos
        w_p_pts2, w_p_rects2 = w_p_pos2

        return w_p_pts + w_p_pts2

    def find_black_pawn(self, screenshot: np.ndarray) -> list:
        b_p_pos = vp.vision_black_pawn.find_item(
            screenshot,
            threshold=0.9,
            debug_mode="rectangles",
        )

        b_p_pts, b_p_rects = b_p_pos

        return b_p_pts

    def set_chessboard(self, screenshot: np.ndarray) -> dict:
        # screenshot = self.win_cap.get_screenshot()
        # screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
        # cv.imshow("Computer vision", screenshot)
        top_left_corner_pos = vp.vision_top_left_corner.find_item(
            screenshot,
            threshold=0.95,
            debug_mode="rectangles",
        )
        bottom_right_corner_pos = vp.vision_bottom_right_corner.find_item(
            screenshot,
            threshold=0.95,
            debug_mode="rectangles",
        )

        top_left_corner_pts, top_left_corner_rects = top_left_corner_pos

        bottom_right_corner_pts, bottom_right_corner_rects = bottom_right_corner_pos

        try:
            top_left_x = top_left_corner_rects[0][0]
            top_left_y = top_left_corner_rects[0][1]

            bottom_right_x = (
                bottom_right_corner_rects[0][0] + bottom_right_corner_rects[0][2]
            )
            bottom_right_y = (
                bottom_right_corner_rects[0][1] + bottom_right_corner_rects[0][3]
            )

        except:
            top_left_x = 0
            top_left_y = 0

            bottom_right_x = self.size
            bottom_right_y = self.size

        h = bottom_right_y - top_left_y
        w = bottom_right_x - top_left_x

        self.square_size = (w / self.size, h / self.size)

        chessboard_dict = {}

        n = top_left_y
        for i in range(self.size):
            chessboard_dict[n] = {}
            m = top_left_x
            for j in range(self.size):
                chessboard_dict[n][m] = f"{self.letters[j]}{self.numbers[i]}"
                m += w / self.size
            n += h / self.size

        return chessboard_dict
