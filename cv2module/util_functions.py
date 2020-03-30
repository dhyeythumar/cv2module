import cv2
import numpy as np


def rotate(ip_image, angle, loss=1):

    scale = 1.0
    # extracting height and width.
    (h, w) = ip_image.shape[:2]
    (cX, cY) = (w / 2, h / 2)

    M = cv2.getRotationMatrix2D((cX, cY), angle, scale)

    if(loss):
        return cv2.warpAffine(ip_image, M, (h, w))

    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])

    # cal new dimensions for the image
    new_W = int((h * sin) + (w * cos))
    new_H = int((h * cos) + (w * sin))

    M[0, 2] += (new_W / 2) - cX
    M[1, 2] += (new_H / 2) - cY

    return cv2.warpAffine(ip_image, M, (new_W, new_H))


def resize(ip_image, width, height=None):

    if height is not None:
        dim = (width, height)
        return cv2.resize(ip_image, dim, interpolation=cv2.INTER_AREA)

    (h, w) = ip_image.shape[:2]
    # calculate the ratio of the width
    r = width / float(w)
    dim = (width, int(h * r))

    return cv2.resize(ip_image, dim, interpolation=cv2.INTER_AREA)


if __name__ == "__main__":

    image = cv2.imread("../input/watch_image.jpg")

    image = resize(image, 500)
    res = rotate(image, 40, loss=1)

    cv2.imshow("Rotated", res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
