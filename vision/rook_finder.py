import cv2 as cv
from time import time
from window_capture import WindowCapture


loop_time = time()
while True:
    screenshot = window_capture()

    cv.imshow("Computer vision", screenshot)

    print(f"FPS {1 / (time() - loop_time)}")
    loop_time = time()

    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()
        break


print("Done.")
