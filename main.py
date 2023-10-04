import cv2 as cv
import numpy as np
from cv.window_capture import WindowCapture
from cv.piece_finder import PieceFinder

win_cap = WindowCapture(2560, 1440)
finder = PieceFinder(win_cap)

while True:
    chessboard_dict = finder.set_chessboard()
    print(chessboard_dict)

    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()
        break


print("Done.")
