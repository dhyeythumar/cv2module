import cv2
import numpy as np
from color_filter import generate_mask as gen_mask


def resize(ip_image, h, w):

    dim = (w, h)
    ip_image = cv2.resize(ip_image, dim, interpolation=cv2.INTER_AREA)
    return ip_image


if __name__ == "__main__":
    # Import your image HERE & it should have 3 channels.
    img = cv2.imread("../input/watch_image.jpg", cv2.IMREAD_COLOR)

    img = resize(img, 200, 300)

    hsv_range, mask, res = gen_mask(img)

    cv2.imshow('Original frame', img)
    cv2.imshow('mask', mask)
    cv2.imshow('resultant', res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite('../output/resultant_image.jpg', res)
