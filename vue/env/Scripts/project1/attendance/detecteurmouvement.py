import os
import sys
import time
import numpy as np
import cv2
from .face_recognitions import Facedetection
import face_recognition as fr
class VideoCamera(object):
        def __init__(self):
            self.cap=cv2.VideoCapture(0) # Mettre votre video ou webcam!
           
            self.type=0
            self.kernel_blur=3
            self.seuil=15
            self.surface=6000
            ret, self.originale=self.cap.read()
            if ret is False:
                 quit()
            self.originale=cv2.cvtColor(self.originale, cv2.COLOR_BGR2GRAY)
            self.originale=cv2.GaussianBlur(self.originale, (self.kernel_blur, self.kernel_blur), 0)
            self.kernel_dilate=np.ones((5, 5), np.uint8)
            self.alarme=0
            self.intrus=0
        def get_frame(self,id):
            path=os.getcwd().replace("\\","/")
            ret, frame=self.cap.read()
            cv2.resize(frame,(1280,720),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
            if ret is False:
                quit()
            gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray_blur=cv2.GaussianBlur(gray, (self.kernel_blur, self.kernel_blur), 0)
            mask=cv2.absdiff(self.originale, gray_blur)
            mask=cv2.threshold(mask, self.seuil, 255, cv2.THRESH_BINARY)[1]
            mask=cv2.dilate(mask, self.kernel_dilate, iterations=3)
            contours, nada=cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            frame_contour=frame.copy()
           
            
            for c in contours:
                 if cv2.contourArea(c)<self.surface:
                     continue
                 cv2.drawContours(frame_contour, [c], 0, (0, 255, 0), 2)
                 x, y, w, h=cv2.boundingRect(c)
                 self.alarme=1
                 self.intrus=1
                 cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                 if self.intrus:
                     cv2.putText(frame, "Detected", (x, y-20), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)
            self.originale=gray_blur
            resp=""

            if fr.face_locations(frame):
                print(id)
                imfpath=path+"/static/assets/images/frame0.jpg"
                foderpath=path+"/static/assets/data/db.data"
                cv2.imwrite(imfpath,frame)
                detect=Facedetection()
                if id!=1:
                    if not detect.identification(foderpath,imfpath):
                      resp=detect.face_saving(imfpath,foderpath,id)
                    else:
                        resp=2   
                else:
                    resp=detect.identification(foderpath,imfpath)
                   
            ret, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes(),resp 
            
               
        
    
