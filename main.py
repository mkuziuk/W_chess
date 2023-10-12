import cv2 as cv
from cv.window_capture import WindowCapture
from cv.piece_finder import PieceFinder
from board_setup import Setup
from formater import Formater

win_cap = WindowCapture(2560, 1440)

finder = PieceFinder(win_cap)

formatter = Setup(win_cap, finder)

formater = Formater()

while True:
    screenshot = win_cap.get_screenshot()
    screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)

    pieces_on_board = formatter.get_pieces_on_board(screenshot)
    formatter.save_snapshot(pieces_on_board)

    # print(pieces_on_board)
    # print(formatter.snapshots)
    # print(len(formatter.snapshots))

    fen = formatter.convert_to_fen(pieces_on_board)

    print(fen)

    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()
        break


print("Done.")
