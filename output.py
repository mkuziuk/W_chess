from stockfish import Stockfish

stockfish = Stockfish(
    path=r"C:\Users\mkuzyuk\Projects\ProjectsPy\Stockfish\stockfish\stockfish-windows-x86-64-avx2.exe",
    depth=18,
    parameters={"Hash": 2048, "Threads": 6},
)

playing = True


while playing:
    position = input("Enter the fen postion or 'q' to quit: ")

    if position == "q":
        break

    if stockfish.is_fen_valid(position):
        stockfish.set_fen_position(position)
        print(stockfish.get_board_visual())
        print(stockfish.get_top_moves(3))
