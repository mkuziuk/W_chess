import cv2 as cv
import numpy as np


class Vision:
    item_img = None
    item_w = 0
    item_h = 0
    method = None

    def __init__(self, item_img_path: str, method=cv.TM_CCOEFF_NORMED):
        self.item_img = cv.imread(item_img_path, cv.IMREAD_UNCHANGED)
        self.item_img = cv.cvtColor(self.item_img, cv.COLOR_BGR2GRAY)

        # Save the dimensions of the item image
        self.item_w = self.item_img.shape[1]
        self.item_h = self.item_img.shape[0]

        # TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED
        self.method = method

    # r"vision\chess_pieces_png\white_rook2_no_back.png"
    def find_item(self, screenshot: np.ndarray, threshold: float = 0.5, debug_mode: str = None) -> list:
        result = cv.matchTemplate(screenshot, self.item_img, self.method)

        # Get the all the positions from the match result that exceed our threshold
        locations = np.where(result >= threshold)
        locations = list(zip(*locations[::-1]))
        # print(locations)

        # list of [x, y, w, h] rectangles
        rectangles = []
        for loc in locations:
            rect = [int(loc[0]), int(loc[1]), self.item_w, self.item_h]
            # Add every box to the list twice in order to retain single (non-overlapping) boxes
            rectangles.append(rect)
            rectangles.append(rect)

        # Apply group rectangles.
        rectangles, weights = cv.groupRectangles(rectangles, groupThreshold=1, eps=0.5)
        # print(rectangles)

        points = []
        if len(rectangles):
            line_color = (0, 255, 0)
            line_type = cv.LINE_4
            marker_color = (0, 255, 0)
            marker_type = cv.MARKER_CROSS

            for x, y, w, h in rectangles:
                # Determine the center position
                center_x = x + int(w / 2)
                center_y = y + int(h / 2)
                # Save the points
                points.append((center_x, center_y))

                if debug_mode == "rectangles":
                    # Determine the box position
                    top_left = (x, y)
                    bottom_right = (x + w, y + h)
                    # Draw the box
                    cv.rectangle(
                        screenshot,
                        top_left,
                        bottom_right,
                        color=line_color,
                        lineType=line_type,
                        thickness=2,
                    )
                elif debug_mode == "points":
                    # Draw the center point
                    cv.drawMarker(
                        screenshot,
                        (center_x, center_y),
                        color=marker_color,
                        markerType=marker_type,
                        markerSize=40,
                        thickness=2,
                    )

        if debug_mode:
            cv.imshow("Matches", screenshot)

        return points, rectangles
