# Used to create different color mask for an frame.
import cv2
import numpy as np


class InvalidChannel(Exception):
    def __init__(self, text):
        self.e = text


def resize(ip_image, dim):

    ip_image = cv2.resize(ip_image, dim, interpolation=cv2.INTER_AREA)
    return ip_image


def nothing(x):
    pass


# dimension = (width, height)
# def cmask(frame, dimension=(600, 400)):
def cmask(frame):
    try:
        if len(frame.shape) != 3:
            raise InvalidChannel(
                "\nInvalidChannelNumber: Invalid number of channels in input image [must be 3 channels] !!")
    except InvalidChannel as e:
        print(e)
    else:
        empty = np.zeros((200, 900, 3), dtype=np.uint8)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(empty,
                    "Controllers to adjust the hsv filter to create mask.",
                    (50, 100), font, 1, (0, 255, 0), 2,  cv2.LINE_AA)
        cv2.putText(empty,
                    "Press [q to get values and exit] or [s to save mask and resultant image to the disk.]", (4, 180), font, 0.5, (0, 255, 0), 1,  cv2.LINE_AA)

        control_window = 'Controllers'
        cv2.namedWindow(control_window)

        # Trackbars to track color changes.
        cv2.createTrackbar('lower_h', control_window, 0, 255, nothing)
        cv2.createTrackbar('lower_s', control_window, 0, 255, nothing)
        cv2.createTrackbar('lower_v', control_window, 0, 255, nothing)

        cv2.createTrackbar('upper_h', control_window, 150, 255, nothing)
        cv2.createTrackbar('upper_s', control_window, 150, 255, nothing)
        cv2.createTrackbar('upper_v', control_window, 150, 255, nothing)

        # frame = resize(frame, dimension)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        while(True):
            lh = cv2.getTrackbarPos('lower_h', control_window)
            ls = cv2.getTrackbarPos('lower_s', control_window)
            lv = cv2.getTrackbarPos('lower_v', control_window)

            hh = cv2.getTrackbarPos('upper_h', control_window)
            hs = cv2.getTrackbarPos('upper_s', control_window)
            hv = cv2.getTrackbarPos('upper_v', control_window)

            # hsv hue sat value
            lower_color = np.array([lh, ls, lv])
            upper_color = np.array([hh, hs, hv])
            hsv_range = [lower_color, upper_color]

            mask = cv2.inRange(hsv, lower_color, upper_color)
            res = cv2.bitwise_and(frame, frame, mask=mask)

            # cv2.imshow('Original frame', frame)
            cv2.imshow('mask', mask)
            cv2.imshow('resultant', res)
            cv2.imshow(control_window, empty)

            k = cv2.waitKey(1) & 0xFF
            # Wait for ESC or 'q' key to exit.
            if((k == 27) | (k == ord('q'))):
                break
            # Wait for 's' key to save and exit.
            elif k == ord('s'):
                cv2.imwrite('./frame_mask.jpg', mask)
                cv2.imwrite('./frame_res.jpg', res)
                break

        cv2.destroyAllWindows()
        return hsv_range, mask, res


if __name__ == "__main__":
    # To test generate_mask function Import your image HERE.
    frame = cv2.imread('../input/watch_image.jpg')
    hsv_range, mask, res = cmask(frame)
