import cv2
import os

if not os.path.exists('frames/CamOneD09M02Y23-H14M12S13-Amsterdam-1.mp4'):
    os.makedirs('frames/CamOneD09M02Y23-H14M12S13-Amsterdam-1.mp4')

cap = cv2.VideoCapture('CamOneD09M02Y23-H14M12S13-Amsterdam-1.mp4')

frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
for i in range(frame_count):
    cap.set(cv2.CAP_PROP_POS_FRAMES, i)
    ret, frame = cap.read()

    # Process the frame here
    
    cv2.imwrite('frames/CamOneD09M02Y23-H14M12S13-Amsterdam-1.mp4/CamOneD09M02Y23-H14M12S13-Amsterdam-1.mp4_%d.jpg' % i, frame)

cap.release()
