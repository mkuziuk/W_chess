import cv2 as cv
from cv.window_capture import WindowCapture
from cv.piece_finder import PieceFinder
from board_setup import SetupBoard
from fen_formatter import Formatter
from fish import Fish
from cv.values import OtherValues as values

win_cap = WindowCapture(2560, 1440)

finder = PieceFinder(win_cap)

setup = SetupBoard(win_cap, finder)


players_color = input("Enter your color ('w' for white, 'b' for black): ")
formatter = Formatter(players_color)


stockfish = values.stockfish
fish = Fish(stockfish)

counters = []
fen_list = []

while True:
    screenshot = win_cap.get_screenshot()
    screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)

    pieces_on_board = setup.get_pieces_on_board(screenshot)
    setup.save_snapshot(pieces_on_board)

    # print(pieces_on_board)
    # print(formatter.snapshots)
    # print(len(formatter.snapshots))

    fen = formatter.convert_to_fen(pieces_on_board, setup)
    print(fen)

    # if fen_list:
    #     if fen != fen_list[-1]:
    #         fen_list.append(fen)
    #         best_moves = fish.get_best_moves(fen)
    # else:
    #     fen_list.append(fen)
    #     best_moves = fish.get_best_moves(fen)

    best_moves = fish.get_best_moves(fen)
    print(best_moves)

    board = fish.get_board(fen)
    print(board)

    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()
        break


print("Done.")
