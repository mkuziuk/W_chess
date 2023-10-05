import cv2 as cv
from cv.window_capture import WindowCapture
from cv.piece_finder import PieceFinder

win_cap = WindowCapture(2560, 1440)

finder = PieceFinder(win_cap)

while True:
    screenshot = win_cap.get_screenshot()
    screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
    chessboard_dict = finder.set_chessboard(screenshot)
    # print(chessboard_dict)

    w_r_points = finder.find_white_rook(screenshot)
    b_r_points = finder.find_black_rook(screenshot)

    w_n_points = finder.find_white_knight(screenshot)
    b_n_points = finder.find_black_knight(screenshot)

    w_b_points = finder.find_white_bishop(screenshot)
    b_b_points = finder.find_black_bishop(screenshot)

    w_q_points = finder.find_white_queen(screenshot)
    b_q_points = finder.find_black_queen(screenshot)

    w_k_points = finder.find_white_king(screenshot)
    b_k_points = finder.find_black_king(screenshot)

    w_p_points = finder.find_white_pawn(screenshot)
    b_p_points = finder.find_black_pawn(screenshot)

    print(b_p_points)

    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()
        break


print("Done.")
