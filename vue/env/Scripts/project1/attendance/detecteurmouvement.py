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
           
            # self.type=0
            # self.kernel_blur=3
            # self.seuil=15
            # self.surface=6000
            # ret, self.originale=self.cap.read()
            # if ret is False:
            #     quit()
            # self.originale=cv2.cvtColor(self.originale, cv2.COLOR_BGR2GRAY)
            # self.originale=cv2.GaussianBlur(self.originale, (self.kernel_blur, self.kernel_blur), 0)
            # self.kernel_dilate=np.ones((5, 5), np.uint8)
            # self.alarme=0
            # self.intrus=0
        def get_frame(self,id):
            path=os.getcwd().replace("\\","/")
            ret, frame=self.cap.read()
            if ret is False:
                quit()
            # gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # gray_blur=cv2.GaussianBlur(gray, (self.kernel_blur, self.kernel_blur), 0)
            # mask=cv2.absdiff(self.originale, gray_blur)
            # mask=cv2.threshold(mask, self.seuil, 255, cv2.THRESH_BINARY)[1]
            # mask=cv2.dilate(mask, self.kernel_dilate, iterations=3)
            # contours, nada=cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            frame_contour=frame.copy()
            # cv2.imwrite(path+"/static/assets/images/frame0.jpg",frame_contour)
            # img=fr.load_image_file(path+"/static/assets/images/frame0.jpg")
            
            # for c in contours:
            #     if cv2.contourArea(c)<self.surface:
            #         continue
            #     cv2.drawContours(frame_contour, [c], 0, (0, 255, 0), 2)
            #     x, y, w, h=cv2.boundingRect(c)
            #     self.alarme=1
            #     self.intrus=1
            #     cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            #     if self.intrus:
            #         cv2.putText(frame, "Detected", (x, y-20), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)
            # self.originale=gray_blur
            
            resp=""
            if fr.face_locations(frame_contour):
                
                imfpath=path+"/static/assets/images/frame0.jpg"
                foderpath=path+"/static/assets/data/db.data"
                cv2.imwrite(imfpath,frame)
                detect=Facedetection()
                if id!=1:
                    
                    if not detect.identification(foderpath,imfpath):
                      detect.face_saving(imfpath,foderpath,id)
                      resp=1
                else:
                    resp=detect.identification(foderpath,imfpath)
            
            frame_flip = cv2.flip(frame_contour,1)
            ret, jpeg = cv2.imencode('.jpg', frame_flip)
            return jpeg.tobytes(),resp
            
               
        
    
