# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 13:50:02 2020

@author: Amel BENAZZA
"""
import cv2
import numpy as np

def info(filepath):
    cap = cv2.VideoCapture(filepath)

    ret, frame1 = cap.read()

    #taille=frame1.shape #(hauteur,largeur,nbre composantes couleur)


    largeur = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

    hauteur =  cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    longueur_seq = cap.get(cv2.CAP_PROP_FRAME_COUNT)

    fps = cap.get(cv2.CAP_PROP_FPS)


    print("Largeur : {0}".format(largeur))

    print("hauteur : {0}".format(hauteur))

    print("Longueur sequence : {0}".format(longueur_seq))

    print("Debit fps: {0}".format(fps))
    


    cap.release()
    cv2.destroyAllWindows()
    
    return largeur,hauteur,longueur_seq,fps

filepath = "akiyo_qcif.y4m"
info(filepath)