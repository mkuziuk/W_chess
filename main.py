import cv2 as cv
from cv.window_capture import WindowCapture
from cv.piece_finder import PieceFinder
from formater import Formater

win_cap = WindowCapture(2560, 1440)

finder = PieceFinder(win_cap)

formater = Formater(win_cap, finder)

while True:
    screenshot = win_cap.get_screenshot()
    screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)

    chessboard_dict = formater.get_chessboard_dict(screenshot)
    pieces_on_board = formater.get_pieces_on_board(screenshot, chessboard_dict)

    print(chessboard_dict)

    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()
        break


print("Done.")
