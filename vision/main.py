import cv2 as cv
import numpy as np

chessboard_img = cv.imread(
    r"vision\chess_pieces_png\chessboard_rook_dif.png", cv.IMREAD_UNCHANGED
)

white_rook_img = cv.imread(
    r"vision\chess_pieces_png\white_rook2_no_back.png", cv.IMREAD_UNCHANGED
)
# width and hight of the image
white_rook_w = white_rook_img.shape[1]
white_rook_h = white_rook_img.shape[0]

result = cv.matchTemplate(chessboard_img, white_rook_img, cv.TM_CCOEFF_NORMED)
print(str(result) + "\n")

threshold = 0.6
locations = np.where(result >= threshold)

print(str(locations) + "\n")

locations = list(zip(*locations[::-1]))
print(locations)

rectangles = []
for loc in locations:
    rect = [int(loc[0]), int(loc[1]), white_rook_w, white_rook_h]
    rectangles.append(rect)

rectangles, weights = cv.groupRectangles(rectangles, 1, 0.5)

if len(rectangles):
    print("White rook found")

    white_rook_w = white_rook_img.shape[1]
    white_rook_h = white_rook_img.shape[0]
    line_color = (0, 0, 255)
    line_type = cv.LINE_4
    line_thickness = 1

    for x, y, w, h in rectangles:
        top_left = x, y
        bottom_right = x + w, y + h

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
