import cv2
import os
import shutil

path=os.getcwd().replace("\\","/")
repertoire=path+"/images"
if not os.path.exists(repertoire):
 os.makedirs(repertoire)
# Opens the inbuilt camera of laptop to capture video.
cap = cv2.VideoCapture(0)

success, image = cap.read()
frame_count = 0
while frame_count<5:
	cv2.imwrite(repertoire+f"/frame_{frame_count}.jpg", image)
	success, image = cap.read()
	frame_count += 1

cap.release()
# if os.path.exists(repertoire):
#   shutil.rmtree(repertoire)