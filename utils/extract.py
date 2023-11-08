import cv2
import numpy as np
import itertools
from math import log10, sqrt

class OpticalFlowAnalyzer:
    def __init__(self, winsize=15):
        self.winsize = winsize

    @staticmethod
    def psnr(dfd): 
        mse = np.mean(dfd ** 2)
        if mse == 0:  # MSE is zero means no noise is present in the signal.
            print('mse=0!, arbitrary PSNR=100')          
            return 100
        max_pixel = 255.0
        psnr = 20 * log10(max_pixel / sqrt(mse))
        return psnr

    @staticmethod
    def draw_flow(im, flow, step=16):
        h, w = im.shape[:2]
        y, x = np.mgrid[step/2:h:step, step/2:w:step].reshape(2,-1).astype(int)
        fx, fy = flow[y, x].T
        lines = np.vstack([x, y, x+fx, y+fy]).T.reshape(-1, 2, 2)
        lines = np.int32(lines)
        vis = cv2.cvtColor(im, cv2.COLOR_GRAY2BGR)
        for (x1, y1), (x2, y2) in lines:
            cv2.line(vis, (x1, y1), (x2, y2), (0, 255, 0), 1)
            cv2.circle(vis, (x1, y1), 1, (0, 255, 0), -1)
        return vis

    @staticmethod
    def dfd(previous, current, flow):
        h, w = previous.shape[:2]
        reconstructed = np.zeros_like(previous)
        for x, y in itertools.product(range(w), range(h)):
            dy, dx = flow[y, x]
            rx = int(max(0, min(x + dx, w - 1)))
            ry = int(max(0, min(y + dy, h - 1)))
            reconstructed[y, x] = current[ry, rx]
        return np.abs(previous - reconstructed)

    def calculate_flow(self, frame1, frame2):
        prvs = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        next = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        flow = cv2.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, self.winsize, 3, 5, 1.2, 0)
        return flow

    def compute_metrics(self, frame1, frame2):
        flow = self.calculate_flow(frame1, frame2)
        fd = self.dfd(cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY), cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY), flow)
        return {
            'flow': flow,
            'psnr': self.psnr(fd)
        }
