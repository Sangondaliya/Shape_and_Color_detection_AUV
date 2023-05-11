import cv2 
import numpy as np


class FilledShape:
    def __init__(self, img):
        self.img = img

    def detect(self, contour,frame):
        shape = "undefined"
        epsilon = 0.03 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        x, y, w, h = cv2.boundingRect(contour)
        #cv2.rectangle(self.img, (x, y), (x + w, y + h), (0, 255, 255), 1)
        #cv2.rectangle(self.img, (x, y-10), (x + w, y + 10), (0, 255, 255), -1)
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        number = ""
        area=cv2.contourArea(contour)
        if area>10000 and area<50000:
            if len(approx) == 3:
                shape = "triangle"
            elif len(approx) == 4:
                # print(w, h, w / h)
                if 0.95 < w / h < 1.05:
                    shape = "Square"
                else:
                    shape = "Rectangle"
            elif len(approx) == 5:
                shape = "Pentagon"
            else:
                shape = "Circle"
            cv2.putText(self.img, number + shape, (x, y), font, 0.4, (0,0,0), 1, cv2.LINE_AA) 
            
          

    def preprocessing_image(self,frame):
        hsv=cv2.cvtColor(self.img,cv2.COLOR_RGB2HSV)
        i_h=cv2.getTrackbarPos('ih','frame')
        i_s=cv2.getTrackbarPos('is','frame')
        i_v=cv2.getTrackbarPos('iv','frame')
        h_h=cv2.getTrackbarPos('hh','frame')
        h_s=cv2.getTrackbarPos('hs','frame')
        h_v=cv2.getTrackbarPos('hv','frame')
        lower=[i_h,i_s,i_v]
        upper=[h_h,h_s,h_v]
        kernel = np.ones((2,2),np.uint8)
        mask = cv2.inRange(hsv, np.array(lower), np.array(upper))
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.dilate(mask, kernel, iterations=3)
        cont,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        return mask,cont

    def Findingcont(self):
        pass

def callback(x):
    pass
def capture(frame):
    img_object = FilledShape(frame)
    mask,contours = img_object.preprocessing_image(frame)
    #print(contours)
    for contour in contours:
        print("going to detect")
        img_object.detect(contour,frame)
        
        print("detected")
    cv2.imshow('frame', frame)
    cv2.imshow('mask',mask)


    
