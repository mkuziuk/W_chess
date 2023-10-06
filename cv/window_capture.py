import numpy as np
import win32gui, win32ui, win32con


class WindowCapture:
    w = 0
    h = 0
    hwnd = None

    def __init__(self, w: int, h: int):
        self.w = w
        self.h = h

    def get_screenshot(self):
        # hwnd = win32gui.FindWindow(None, windowname)

        # get the window image date
        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0), (self.w, self.h), dcObj, (0, 0), win32con.SRCCOPY)

        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype="uint8")
        img.shape = (self.h, self.w, 4)

        # Free Ressources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        # drop alpha channel
        img = img[..., :3]

        # make image contiguous
        img = np.ascontiguousarray(img)

        return img
