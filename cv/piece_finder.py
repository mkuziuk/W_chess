import cv2 as cv
import numpy as np
from .window_capture import WindowCapture
from .vision import Vision


class PieceFinder:
    win_cap = None
    vision_top_left_corner = Vision(r"cv\chess_pieces_png\top_left_corner.png")
    vision_bottom_right_corner = Vision(r"cv\chess_pieces_png\bottom_right_corner.png")

    vision_white_rook = Vision(r"cv\chess_pieces_png\white_r.png")

    def __init__(self, win_cap: WindowCapture):
        self.win_cap = win_cap

    def set_chessboard(self):
        screenshot = self.win_cap.get_screenshot()
        screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
        # cv.imshow("Computer vision", screenshot)
        top_left_corner_position = self.vision_top_left_corner.find_item(
            screenshot,
            threshold=0.8,
            debug_mode="rectangles",
        )
        bottom_right_corner_position = self.vision_bottom_right_corner.find_item(
            screenshot,
            threshold=0.9,
            debug_mode="rectangles",
        )

        top_left_corner_pts, top_left_corner_rects = top_left_corner_position
        (
            bottom_right_corner_pts,
            bottom_right_corner_rects,
        ) = bottom_right_corner_position

        size = 8

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

            bottom_right_x = size
            bottom_right_y = size

        print(f"{top_left_x}, {top_left_y}, {bottom_right_x}, {bottom_right_y}\n")

        h = bottom_right_y - top_left_y
        w = bottom_right_x - top_left_x

        letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8"]

        chessboard_dict = {}

        n = top_left_y
        for i in range(size):
            chessboard_dict[n] = {}
            m = top_left_x
            for j in range(size):
                chessboard_dict[n][m] = f"{letters[i]}{numbers[j]}"
                m += w / size
            n += h / size

        return chessboard_dict
