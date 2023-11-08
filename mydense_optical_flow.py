# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 13:50:02 2020

@author: Amel BENAZZA
"""
import cv2
import numpy as np
import itertools
from itertools import product 
from math import log10, sqrt 

def PSNR(mydfd): 
    mse = np.mean(mydfd ** 2) 
    if(mse == 0):  # MSE is zero means no noise is present in the signal . 
                  # Therefore PSNR have no importance.
        print('mse=0!, arbitrary PSNR=100')          
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse)) 
    return psnr

def draw_flow(im,flow,step=4):
       h,w = im.shape[:2]
       #y,x = np.mgrid[step/2:h:step,step/2:w:step].reshape(2,-1)
       y, x = np.mgrid[step/2:h:step, step/2:w:step].reshape(2,-1).astype(int) 
       fx,fy = flow[y,x].T

       # create line endpoints
       lines = np.vstack([x,y,x+fx,y+fy]).T.reshape(-1,2,2)
       lines = np.int32(lines)

       # create image and draw
       vis = cv2.cvtColor(im,cv2.COLOR_GRAY2BGR)
       for (x1,y1),(x2,y2) in lines:
           cv2.line(vis,(x1,y1),(x2,y2),(0,255,0),1)
           cv2.circle(vis,(x1,y1),1,(0,255,0), -1)
       return vis

def dfd(previous,current,flow):
    height, width = previous.shape[:2]

    # allocate "reconstruct" only once
    
   #reconstructed = np.empty(previous.shape)
    reconstructed = np.zeros_like(previous)
    
    for x, y in itertools.product(range(width), range(height)):
        dy, dx = flow[y, x]
        rx = int(max(0, min(x + dx, width - 1)))
        ry = int(max(0, min(y + dy, height - 1)))
        reconstructed[y, x] = current[ry, rx]
    return np.abs(previous-reconstructed)

def flow_to_color(flow, frame2):
    hsv = np.zeros_like(frame2)
    hsv[..., 1] = 255
    mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
    hsv[..., 0] = ang * 180 / np.pi / 2
    hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
    rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return rgb, mag, ang

cap = cv2.VideoCapture("akiyo_qcif.y4m")
ret, frame1 = cap.read()

if not ret:
    print("Error: Unable to read video file")
    cap.release()
    exit(1)

prvs = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
hsv[...,1] = 255
num_frame = 1
length_seq = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print('Seq length', length_seq)

try:
    while num_frame < length_seq:
        ret, frame2 = cap.read()
        if not ret:
            break
        
        next = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

        FD = np.abs(prvs - next)
        cv2.imwrite(f'akiDF_{num_frame:04d}.jpg', FD)
        print(f"PSNR DF {num_frame}: {PSNR(FD)}")
        
        flow = cv2.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
      
      
        step = 8 
        h, w = prvs.shape[:2]
        flow_img = cv2.cvtColor(prvs, cv2.COLOR_GRAY2BGR) if len(prvs.shape) == 2 else prvs.copy()

        for y in range(0, h, step):
            for x in range(0, w, step):
                fx, fy = flow[y, x]
                end_point = (int(x + fx), int(y + fy))  
                cv2.arrowedLine(flow_img, (x, y), end_point, color=(0, 255, 0), thickness=1, tipLength=0.3)

    
        cv2.imwrite(f'Flowwitharrows_{num_frame:04d}.png', flow_img)
        


        rgb, mag, ang = flow_to_color(flow, frame2)
        cv2.imwrite(f'akiOF_hsv_{num_frame:04d}.png', rgb)
        cv2.imwrite(f'akiOF_{num_frame:04d}.jpg', draw_flow(prvs, flow))
        
        myDFD = dfd(prvs, next, flow)
        print(f'PSNR DFD {num_frame}: {PSNR(myDFD)}')
        cv2.imwrite(f'akiDFD_{num_frame:04d}.jpg', myDFD)

        prvs = next
        num_frame += 1

except KeyboardInterrupt:
    print("Interrupted")

finally:
    cap.release()
    cv2.destroyAllWindows()
