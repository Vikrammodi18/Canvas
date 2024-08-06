import numpy as np
import cv2
draw = False
mode = True
prex,prey = -1,-1
def onChange(x):
    pass
def change(value):
    print(value)
    global mode
    if value == 1:
       mode = True
    else:
       mode = False
def draw_shape(events,x,y,key,param):
    
    B = cv2.getTrackbarPos("B","track")
    G = cv2.getTrackbarPos("G","track")
    R = cv2.getTrackbarPos("R","track")
    radius = cv2.getTrackbarPos("radius","track")
    thickness = cv2.getTrackbarPos(thick,"track")
    global draw,mode,prex,prey
    if (events == cv2.EVENT_LBUTTONDOWN):
        prex = x
        prey = y
        draw = True
        
    elif events == cv2.EVENT_MOUSEMOVE:
        if draw == True:
            if mode == True:
                cv2.rectangle(img,(prex,prey),(x,y),(B,G,R),-1)
            else:
                cv2.circle(img,(x,y),radius,(B,G,R),-1)
            # print(x,y)
    elif (events == cv2.EVENT_LBUTTONUP):
        draw = False
        if mode == True:
            cv2.rectangle(img,(prex,prey),(x,y),(B,G,R),-1)
        else:
            cv2.circle(img,(x,y),radius,(B,G,R),-1)
thick = "thick"
shape = "0(off)\n1(on)"
cv2.namedWindow("image")
img = np.zeros((550,750,3),np.uint8)
cv2.namedWindow("track")
cv2.resizeWindow("track",400,250)
cv2.createTrackbar("radius","track",1,200,onChange)
cv2.createTrackbar("B","track",0,255,onChange)
cv2.createTrackbar("R","track",0,255,onChange)
cv2.createTrackbar("G","track",0,255,onChange)
cv2.createTrackbar(thick,"track",0,6,onChange)
cv2.createTrackbar(shape,"image",0,1,change)
cv2.setMouseCallback("image",draw_shape)
while(True):
    cv2.imshow("image",img)
    # cv2.imwrite("new.jpg",img)
    if cv2.waitKey(20) == ord('q'):
        break
cv2.destroyAllWindows()