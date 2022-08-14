# import the necessary packages
import numpy as np
import cv2

# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cv2.startWindowThread()

# open webcam video stream
cap = cv2.VideoCapture('./input/clips/0bfacc_0.mp4')
#cap = cv2.VideoCapture(0)

out = cv2.VideoWriter(
    'output.mp4',
    cv2.VideoWriter_fourcc(*'mp4v'),
    20.,
    (1920, 1080))

while 1:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    frame = cv2.resize(frame, (3840, 2160))
    # using a greyscale picture, also for faster detection
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # detect people in the image
    # returns the bounding boxes for the detected objects
    boxes, weights = hog.detectMultiScale(
        gray, winStride=(2, 2), scale=1.01)

    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

    for i, (xA, yA, xB, yB) in enumerate(boxes):
        if weights[i] < 0.5:
            continue
        # display the detected boxes in the colour picture
        cv2.rectangle(frame, (xA, yA), (xB, yB),
                      (0, 255, 0), 2)
        cv2.putText(frame, f'{weights[i]}', (xA, yA),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)

    #cv2.imshow('frame', frame)
    frame = cv2.resize(frame, (1920, 1080))
    out.write(frame.astype('uint8'))
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    if key == ord('s'):
        cv2.imwrite('last.jpg', frame)

# When everything done, release the capture
cap.release()
out.release()
# finally, close the window
cv2.destroyAllWindows()
cv2.waitKey(1)
