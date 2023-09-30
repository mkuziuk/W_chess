import cv2 as cv
import numpy as np

chessboard_img = cv.imread(
    r"vision\chess_pieces_png\chessboard_rook_dif.png", cv.IMREAD_UNCHANGED
)

white_rook_img = cv.imread(
    r"vision\chess_pieces_png\black_rook2.png", cv.IMREAD_UNCHANGED
)

result = cv.matchTemplate(chessboard_img, white_rook_img, cv.TM_CCOEFF_NORMED)
print(str(result) + "\n")

threshold = 0.8
locations = np.where(result >= threshold)

print(str(locations) + "\n")

locations = list(zip(*locations[::-1]))
print(locations)

if locations:
    print("White rook found")

    white_rook_w = white_rook_img.shape[1]
    white_rook_h = white_rook_img.shape[0]
    line_color = (0, 0, 255)
    line_type = cv.LINE_4
    line_thickness = 1

    for loc in locations:
        top_left = loc
        bottom_right = (top_left[0] + white_rook_w, top_left[1] + white_rook_h)

        cv.rectangle(
            chessboard_img,
            top_left,
            bottom_right,
            line_color,
            line_thickness,
            line_type,
        )

    cv.imshow("Chessboard", chessboard_img)
    cv.waitKey()

else:
    print("White rook not found")
