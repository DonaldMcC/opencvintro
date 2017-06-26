import numpy as np
import cv2

clicked = False
def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True

cameraCapture = cv2.VideoCapture(0)
fps = 30 # an assumption
size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
cv2.namedWindow('MyWindow', cv2.WINDOW_NORMAL)
cv2.setMouseCallback('MyWindow', onMouse)

print 'Showing camera feed. Click window or press any key to stop.'

while not clicked:
    success, frame = cameraCapture.read()
    #gray = cv2.cvtColor(frame, cv2)
    cv2.imshow('MyWindow', frame)
    cv2.waitKey(25)

cameraCapture.release()
cv2.destroyAllWindows()
