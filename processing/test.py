from stockfish import Stockfish

stockfish = Stockfish(
    path=r"C:\Users\mkuzyuk\Projects\ProjectsPy\Stockfish\stockfish\stockfish-windows-x86-64-avx2.exe",
    depth=18,
    parameters={"Hash": 2048, "Threads": 6},
)

position = []
playing = True


while playing:
    move = input("Enter move: ")

    if move == "q":
        break

    position.append(move)

    stockfish.set_position(position)
    print(stockfish.get_top_moves(3))
