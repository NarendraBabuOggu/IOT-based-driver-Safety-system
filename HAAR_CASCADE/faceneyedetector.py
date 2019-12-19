import numpy as np
import cv2
import time
#import sys
import pyglet
import httplib2, urllib3, os3, glob3, requests
from datetime import datetime
#haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haar-eyes.xml')

wavefile = 'sample.wav'

 

#cap = cv2.VideoCapture('face1.jpg')
cap = cv2.VideoCapture(0)

newTime = time.time()
oldTime = time.time()
command = ""

print (newTime,oldTime)

def playAudio():
    player = pyglet.media.Player()
    music = pyglet.media.load(wavefile)
    player.queue(music)
    player.play()
    time.sleep(4)
    #pyglet.app.run()
    return


def sleepTrack(x,y,Image):
    print (x, y)
    #newTime = time.time()
    dt =  x - y
    print (dt)
    frame = Image.copy()
    #frame = cv2.imread(Image)
    if dt > 7:
        playAudio()
        print ("Driver is Sleeping")
        y = time.time()
        print (x, y)
        playAudio()
        #CaptureImage(Image)
                
    else:
       print ("Driver is Not Sleeping")
       
    return y
    
while True:
    ret, img = cap.read()
    if ret:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
        
            eyes = eye_cascade.detectMultiScale(roi_gray)
            
            newTime = time.time()      
            oldTime = sleepTrack(newTime,oldTime,img)
            
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                newTime = time.time()
                oldTime = newTime

        cv2.imshow('img',img)
        time.sleep(0.1)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
