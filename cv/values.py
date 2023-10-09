from .vision import Vision


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
    vision_black_king = Vision(r"cv\chess_pieces_png\black_k2.png")

    vision_white_pawn = Vision(r"cv\chess_pieces_png\white_p3.png")
    vision_white_pawn2 = Vision(r"cv\chess_pieces_png\white_p4.png")
    vision_black_pawn = Vision(r"cv\chess_pieces_png\black_p2.png")


class OtherValues:
    letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    numbers = ["8", "7", "6", "5", "4", "3", "2", "1"]
    size = 8
