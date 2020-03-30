import cv2
import numpy as np
from cv2module import cmask

hsv_range = []
redo = 1

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
actual_video = cv2.VideoWriter('../output/actual_video.avi', fourcc, 20.0, (640, 480))
result_video = cv2.VideoWriter('../output/result_video.avi', fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()
    if ret == "False":
        break

    # Writing the actual frames to the video.
    actual_video.write(frame)

    if((len(hsv_range) == 0) & (redo == 1)):
        # The mask and res returned by the function are static in nature[only for first frame].
        # So create the new mask for each frame with hsv_range.
        # Redo is used to again create a mask and get the hsv_range for new frame.
        redo = 0
        hsv_range, static_mask, static_res = cmask(frame)
    else:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # hsv => hue sat value
        lower_red = hsv_range[0]
        upper_red = hsv_range[1]

        mask = cv2.inRange(hsv, lower_red, upper_red)
        res = cv2.bitwise_and(frame, frame, mask=mask)

        # Write the resultant frames (after applying the mask) to the video.
        result_video.write(res)

        cv2.imshow('frame', frame)
        cv2.imshow('mask', mask)
        cv2.imshow('res', res)

    k = cv2.waitKey(1) & 0xFF
    # Wait for ESC or 'q' key to exit.
    if((k == 27) | (k == ord('q'))):
        break
    # Wait for 'r' key to recalculate hsv_range.
    elif(k == ord('r')):
        hsv_range = []
        redo = 1
        cv2.destroyAllWindows()
        continue

cap.release()
result_video.release()
actual_video.release()
cv2.destroyAllWindows()
