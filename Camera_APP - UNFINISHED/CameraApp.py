# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 10:51:00 2022

@author: marin
"""

""" Library """
import cv2
import numpy as np

""" Init Phase """

global VideFeedModuleSel
global ImageShowModeSel

VideFeedModuleSel = 1
ImageShowModeSel = 1

""" Functions """


""" Interrupt """

KeyInterruptSTS = False
def KeyInterrupt ():
    global VideFeedModuleSel
    global ImageShowModeSel
    global run
    if key == 49: #1
        VideFeedModuleSel = 1
    if key ==50: #2
        VideFeedModuleSel = 0
    if key == 52: #4
        ImageShowModeSel = 1   
    if key == 53: #5
        ImageShowModeSel = 2 
    if key == 54: #6
        ImageShowModeSel = 3   
    if key == 55: #7
        ImageShowModeSel = 4 
    if key == 56: #8
        ImageShowModeSel = 5 
    if key == 113: #q
        ImageShowModeSel = 99
        VideoFeed.release()
        cv2.destroyAllWindows()
        run = False
    






""" Main Loop """
VideoFeed = cv2.VideoCapture(VideFeedModuleSel)       
run = True
while(run):
    if cv2.waitKey(1):
        key = cv2.waitKey(100)
        if key > 0:
            KeyInterrupt()
            VideoFeed = cv2.VideoCapture(VideFeedModuleSel)
    ret,frame = VideoFeed.read()
    #print(key,VideFeedModuleSel )
    if ret == True:  
        pass
    else:
        print("No Vide Feed, plase check camera feed - cv2.VideoCapture(1)")
        run = False
        break
    if ImageShowModeSel == 1 :
        cv2.imshow('frame',frame)
    elif ImageShowModeSel == 2 :
        grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
        cv2.imshow('frame',grayscale)
    elif ImageShowModeSel == 3 :
        grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(grayscale,75,125)
        cv2.imshow('frame',edges)
    elif ImageShowModeSel == 4:
        bilateral=cv2.bilateralFilter(frame,9,75,75)
        cv2.imshow('frame',bilateral)
    elif ImageShowModeSel == 5:
        min_area = 0.0005
        max_area = 0.95
        dilate_iter = 10
        erode_iter = 10
        mask_color = (0.0,0.0,0.0)
        grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(grayscale,75,125)
        edges = cv2.dilate(edges, None)
        edges = cv2.erode(edges, None)     
        # get the contours and their areas
        
        c = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        contour_info = (c, cv2.contourArea(c))
        
        """
        for c in cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)[1]]
        
        # Get the area of the image as a comparison
        image_area = frame.shape[0] * frame.shape[1]  
      
        # calculate max and min areas in terms of pixels
        max_area = max_area * image_area
        min_area = min_area * image_area
        # Set up mask with a matrix of 0's
        mask = np.zeros(edges.shape, dtype = np.uint8)
        # Go through and find relevant contours and apply to mask
        for contour in contour_info:
            # Instead of worrying about all the smaller contours, if the area is smaller than the min, the loop will break
            if contour[1] > min_area and contour[1] < max_area:
                # Add contour to mask
                mask = cv2.fillConvexPoly(mask, contour[0], (255))        
        # use dilate, erode, and blur to smooth out the mask
        mask = cv2.bilateralFilter(mask,9,75,75)
        # Ensures data types match up
        mask_stack = mask.astype('float32') / 255.0           
        frame = frame.astype('float32') / 255.0
        # Blend the image and the mask
        masked = (mask_stack * frame) + ((1-mask_stack) * mask_color)
        masked = (masked * 255).astype('uint8')

        cv2.imshow("Foreground", masked)
        """
    else :
        print("wrong settings")
        VideoFeed.release()
        cv2.destroyAllWindows()
        run = False