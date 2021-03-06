import cv2
clicked = False


def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True

#videoCapture = cv2.VideoCapture('MyOutputVid.avi')
videoCapture = cv2.VideoCapture('IMG_0464.MOV')
print videoCapture.grab() 

#fps = videoCapture.get(cv2.CAP_PROP_FPS)
fps = 25
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

cv2.namedWindow('MyWindow')
cv2.setMouseCallback('MyWindow', onMouse)

print 'Showing camera feed. Click window or press any key to stop.'
success, frame = videoCapture.read()
while success and not clicked:
    cv2.imshow('MyWindow', frame)
    cv2.waitKey(25)
    success, frame = videoCapture.read()

    

cv2.destroyWindow('MyWindow')
videoCapture.release()
