import cv2


# handle mouse input to mark objects
def mark_object():
    pass


# intitalize window to display frames
cv2.namedWindow('frame')
# add mouse callback to handle mouse events
cv2.setMouseCallback('frame', mark_object)

# load the video
# TODO: load different videos with command line args
cap = cv2.VideoCapture('./input/clips/0bfacc_0.mp4')

# track the latest key press and current frame
key = 0
frame_count = 0

# read the first frame
ret, frame = cap.read()


# loop until the video ends or the `ESC` key is pressed
while key != 27 and ret:
    # show the current frame number
    cv2.putText(frame, f'Frame: {frame_count}', (5, 20),
                cv2.FONT_HERSHEY_SIMPLEX, .7, (255, 255, 255), 1)
    # show current selector type
    # render the frame
    cv2.imshow('frame', frame)

    # wait for key input indefinitely
    key = cv2.waitKey(0)

    # if spacebar is pressed
    if key == 32:
        # move to the next frame
        ret, frame = cap.read()
        frame_count += 1


# clean up
cap.release()
cv2.destroyAllWindows()
