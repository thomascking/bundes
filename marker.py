import cv2
import json
import sys


clip_id = sys.argv[1]


# colors for teams
TEAM_ONE_COLOR = (255, 0, 0)
TEAM_ONE_GOALIE_COLOR = (255, 255, 0)
TEAM_TWO_COLOR = (0, 0, 255)
TEAM_TWO_GOALIE_COLOR = (0, 255, 255)
BALL_COLOR = (0, 255, 0)

TEAM_ONE = 'Team 1'
TEAM_ONE_GOALIE = 'Goalie 1'
TEAM_TWO = 'Team 2'
TEAM_TWO_GOALIE = 'Goalie 2'
BALL = 'Ball'


COLOR_MAP = {
    TEAM_ONE: TEAM_ONE_COLOR,
    TEAM_ONE_GOALIE: TEAM_ONE_GOALIE_COLOR,
    TEAM_TWO: TEAM_TWO_COLOR,
    TEAM_TWO_GOALIE: TEAM_TWO_GOALIE_COLOR,
    BALL: BALL_COLOR,
}

current_mode = TEAM_ONE

markings = [
    [],
]

# handle mouse input to mark objects


def mark_object(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        markings[frame_count].append({
            'x': x,
            'y': y,
            'type': current_mode,
        })


# intitalize window to display frames
cv2.namedWindow('frame')
# add mouse callback to handle mouse events
cv2.setMouseCallback('frame', mark_object)

# load the video
# TODO: load different videos with command line args
cap = cv2.VideoCapture(f'./input/clips/{clip_id}.mp4')

# track the latest key press and current frame
key = 0
frame_count = 0

# read the first frame
ret, frame = cap.read()


# loop until the video ends or the `ESC` key is pressed
while key != 27 and ret:
    # clear previous text
    current_frame = frame.copy()
    # show the current frame number
    cv2.putText(current_frame, f'Frame: {frame_count}', (5, 20),
                cv2.FONT_HERSHEY_SIMPLEX, .7, (255, 255, 255), 1)
    # show current marking type
    cv2.putText(current_frame, f'Marking: {current_mode}', (5, 40),
                cv2.FONT_HERSHEY_SIMPLEX, .7, (255, 255, 255), 1)

    # show current markings
    for marking in markings[frame_count]:
        cv2.circle(current_frame,
                   (marking['x'], marking['y']), 6, COLOR_MAP[marking['type']], 3)

    # render the frame
    cv2.imshow('frame', current_frame)

    # wait for key input
    key = cv2.waitKey(1)

    # if spacebar is pressed
    if key == ord('.'):
        # move to the next frame
        ret, frame = cap.read()
        frame_count += 1
        if len(markings) <= frame_count:
            markings.append([])
    elif key == ord(','):
        frame_count -= 1
        if frame_count < 0:
            frame_count = 0
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_count + 1)
        ret, frame = cap.retrieve()
    elif key == ord('1'):
        current_mode = TEAM_ONE
    elif key == ord('2'):
        current_mode = TEAM_TWO
    elif key == ord('g'):
        current_mode = TEAM_ONE_GOALIE
    elif key == ord('h'):
        current_mode = TEAM_TWO_GOALIE
    elif key == ord('b'):
        current_mode = BALL

# write the markings
json_data = json.dumps(markings, indent=2)
with open(f'./output/markings/{clip_id}.json', 'w') as outfile:
    outfile.write(json_data)

# clean up
cap.release()
cv2.destroyAllWindows()
