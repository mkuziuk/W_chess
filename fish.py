from stockfish import Stockfish


class Fish:
    def __init__(self, stockfish: Stockfish):
        self.stockfish = stockfish

    def get_best_moves(self, position: str, number_of_moves: int = 3) -> list:
        stockfish = self.stockfish
        if stockfish.is_fen_valid(position):
            stockfish.set_fen_position(position)

            return stockfish.get_top_moves(number_of_moves)
        else:
            return None

    def get_board(self, fen: str):
        stockfish = self.stockfish
        return stockfish.get_board_visual()
