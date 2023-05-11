import cv2 
import numpy as np

img=cv2.imread(r'C:\AUV\turkey\codes\images\circle .jpg')
cap=cv2.VideoCapture(0)
print(img.shape)
img=cv2.resize(img,(448,313))
gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
frame=cv2.imread(r'C:\AUV\turkey\codes\images\images (2).jpg')
s=0
while True:
    #san,frame=cap.read()
    rows1=gray.shape[0]
    circles1=cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,rows1/3,param1=50,param2=20,minRadius=20,maxRadius=50)
    
    print('before np circles',circles1)
    if circles1 is not None:
        circles1 = np.uint16(np.around(circles1))
        print('after np circles',circles1)
        for i in circles1[0, :]:
            center1 = (i[0], i[1])
            # circle center
            cv2.circle(img, center1, 1, (0, 100, 100), 3)
            # circle outline
            radius1 = i[2]
            cv2.circle(img, center1, radius1, (255, 0, 255), 3)
    frame2=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    rows2=frame2.shape[0]
    circles2=cv2.HoughCircles(frame2,cv2.HOUGH_GRADIENT,1,100,param1=256,param2=10,minRadius=1,maxRadius=30)
    if circles2 is not None:
        circles2 = np.uint16(np.around(circles2))
        #circles = np.round(circles[0, :]).astype("int")
        print('after np circles',circles2)
        for i in circles2[0, :]:
            center2 = (i[0], i[1])
            # circle center
            cv2.circle(frame, center2, 1, (0, 100, 100), 3)
            # circle outline
            radius2 = i[2]
            cv2.circle(frame, center2, radius2, (255, 0, 255), 3)
    cv2.imshow('image',img)
    cv2.imshow('live',frame)
    k=cv2.waitKey(1)
    if k==27:
        break
    s+=1
    if s>100:
        frame=cv2.imread(r'C:\AUV\turkey\codes\images\circle .jpg')
        img=cv2.imread(r'C:\AUV\turkey\codes\images\images (2).jpg')
        img=cv2.resize(img,(448,313))
        frame=cv2.resize(frame,(448,313))
    if s>150:
        frame=cv2.imread(r'C:\AUV\turkey\codes\images\c1.png')
        img=cv2.imread(r'C:\AUV\turkey\codes\images\c1.png') 
        img=cv2.resize(img,(448,313))
        frame=cv2.resize(frame,(448,313))
    if s>200:
        frame=cv2.imread(r'C:\AUV\turkey\codes\images\c2.png')
        img=cv2.imread(r'C:\AUV\turkey\codes\images\c2.png')
        img=cv2.resize(img,(448,313))
        frame=cv2.resize(frame,(448,313))
    if s>250:
        frame=cv2.imread(r'C:\AUV\turkey\codes\images\c3.jpg')
        img=cv2.imread(r'C:\AUV\turkey\codes\images\c3.jpg')
        img=cv2.resize(img,(448,313))
        frame=cv2.resize(frame,(448,313))
    if s>300:
        frame=cv2.imread(r'C:\AUV\turkey\codes\images\cr4.png')
        img=cv2.imread(r'C:\AUV\turkey\codes\images\cr4.png')
        img=cv2.resize(img,(448,313))
        frame=cv2.resize(frame,(448,313))
    if s>350:
        frame=cv2.imread(r'C:\AUV\turkey\codes\images\mc.png')
        img=cv2.imread(r'C:\AUV\turkey\codes\images\mc.png')
        img=cv2.resize(img,(448,313))
        frame=cv2.resize(frame,(448,313))

cap.release()
cv2.destroyAllWindows()    