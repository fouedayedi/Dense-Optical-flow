# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 12:30:16 2020

@author: Emna
"""
########################Read an image file ###########################
# importing OpenCV(cv2) module 
import cv2 
  


######################### Read a video ##############################""


#cap = cv2.VideoCapture("akiyo_qcif.y4m")
#cap = cv2.VideoCapture("bowing_qcif.y4m")
#cap = cv2.VideoCapture("bus_qcif_15fps.y4m")
#cap = cv2.VideoCapture("carphone_qcif.y4m")
#cap = cv2.VideoCapture("salesman_qcif.y4m")
#cap = cv2.VideoCapture("claire_qcif.y4m")
#cap = cv2.VideoCapture("coastguard_qcif.y4m")
#cap = cv2.VideoCapture("crew_qcif_15fps.y4m")
def readseq(filepath):
    cap = cv2.VideoCapture(filepath)


        #Grabs, decodes and returns the next video frame.
    while cap.isOpened():
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        cv2.imshow('frame', frame)
        if cv2.waitKey(50) == ord('q'):
            break
    cap.release()                  # Closes video file
    cv2.destroyAllWindows()         # Closes all generated cv2 windows 

filepath = "akiyo_qcif.y4m"
readseq(filepath)