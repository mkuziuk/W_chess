from dataclasses import dataclass
from stockfish import Stockfish

from .vision import Vision


@dataclass
class VisionPaths:
    vision_top_left_corner = Vision(r"cv\chess_pieces_png\top_left_corner.png")
    vision_bottom_right_corner = Vision(r"cv\chess_pieces_png\bottom_right_corner.png")

    vision_white_rook = Vision(r"cv\chess_pieces_png\white_r.png")
    vision_white_rook2 = Vision(r"cv\chess_pieces_png\white_r2.png")
    vision_black_rook = Vision(r"cv\chess_pieces_png\black_r2.png")

    vision_white_knight = Vision(r"cv\chess_pieces_png\white_n.png")
    vision_white_knight2 = Vision(r"cv\chess_pieces_png\white_n2.png")
    vision_black_knight = Vision(r"cv\chess_pieces_png\black_n2.png")

    vision_white_bishop = Vision(r"cv\chess_pieces_png\white_b.png")
    vision_white_bishop2 = Vision(r"cv\chess_pieces_png\white_b2.png")
    vision_black_bishop = Vision(r"cv\chess_pieces_png\black_b2.png")

    vision_white_queen = Vision(r"cv\chess_pieces_png\white_q2.png")
    vision_black_queen = Vision(r"cv\chess_pieces_png\black_q2.png")

    vision_white_king = Vision(r"cv\chess_pieces_png\white_k2.png")
    vision_white_king2 = Vision(r"cv\chess_pieces_png\white_k3.png")
    vision_black_king = Vision(r"cv\chess_pieces_png\black_k2.png")

    vision_white_pawn = Vision(r"cv\chess_pieces_png\white_p3.png")
    vision_white_pawn2 = Vision(r"cv\chess_pieces_png\white_p4.png")
    vision_black_pawn = Vision(r"cv\chess_pieces_png\black_p2.png")


@dataclass
class OtherValues:
    letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    numbers = ["8", "7", "6", "5", "4", "3", "2", "1"]
    size = 8

    stockfish = Stockfish(
        path=r"C:\Users\mkuzyuk\Projects\ProjectsPy\Stockfish\stockfish\stockfish-windows-x86-64-avx2.exe",
        depth=16,
        parameters={"Hash": 8192, "Threads": 8},
    )

    halfmove_number = 2

    initial_board = {
        "a8": "r",
        "b8": "n",
        "c8": "b",
        "d8": "q",
        "e8": "k",
        "f8": "b",
        "g8": "n",
        "h8": "r",
        "a7": "p",
        "b7": "p",
        "c7": "p",
        "d7": "p",
        "e7": "p",
        "f7": "p",
        "g7": "p",
        "h7": "p",
        "a6": "0",
        "b6": "0",
        "c6": "0",
        "d6": "0",
        "e6": "0",
        "f6": "0",
        "g6": "0",
        "h6": "0",
        "a5": "0",
        "b5": "0",
        "c5": "0",
        "d5": "0",
        "e5": "0",
        "f5": "0",
        "g5": "0",
        "h5": "0",
        "a4": "0",
        "b4": "0",
        "c4": "0",
        "d4": "0",
        "e4": "0",
        "f4": "0",
        "g4": "0",
        "h4": "0",
        "a3": "0",
        "b3": "0",
        "c3": "0",
        "d3": "0",
        "e3": "0",
        "f3": "0",
        "g3": "0",
        "h3": "0",
        "a2": "P",
        "b2": "P",
        "c2": "P",
        "d2": "P",
        "e2": "P",
        "f2": "P",
        "g2": "P",
        "h2": "P",
        "a1": "R",
        "b1": "N",
        "c1": "B",
        "d1": "Q",
        "e1": "K",
        "f1": "B",
        "g1": "N",
        "h1": "R",
    }
