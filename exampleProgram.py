#python version 3.9.7
#opncv-python version = 4.5.4.60
#mediapipe version = 0.8.9.1

import cv2
from mpFaceSimplified import mpFace
import math

cam = cv2.VideoCapture(0)
# cam = cv2.VideoCapture("http://192.168.1.3:4747/video")# connecting to ip cam
width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
#print(width,height)

cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

radius = 2
red = (0,0,255)
green = (0,255,0)
blue = (255,0,0)
yellow = (0,255,255)

faceLm = mpFace()

#For connecting range of dots
def connectPoints(indx1,indx2):
    for i in range(indx1,indx2):
        if i==(indx2-1):
            cv2.line(frame,(face[i][0],face[i][1]),(face[indx1][0],face[indx1][1]),green,1)
            break
        cv2.line(frame,(face[i][0],face[i][1]),(face[i+1][0],face[i+1][1]),green,1)
#Finding length between two points
def findRadius(pt1,pt2):
    x1,y1 = (pt1[0],pt1[1])
    x2,y2 = (pt2[0],pt2[1])
    radius = math.sqrt(((y2-y1)*(y2-y1))+((x2-x1)*(x2-x1)))
    return radius

while True:
    a, frame = cam.read()

    faces = faceLm.faceLandmarksSimplified(frame)
    # for face in faces:
    #     for lm in face:
    #         cv2.circle(frame,lm,radius,green,-1)
    for face in faces:
        #print(len(face))
        for indx in range(0,len(face)):# Total Landmarks = 141
            cv2.circle(frame,(face[indx][0],face[indx][1]),radius,red,-1)
            # print(face[indx])        
        connectPoints(0,10)#Left Eyebrow (0->9)
        connectPoints(10,20)#right Eyebrow (10->19)
        connectPoints(20,36)#Left Eye (20->35)
        connectPoints(36,52)#Right Eye (36->51)
        connectPoints(52,72)#iner Lip (52->71)
        connectPoints(72,92)#outer Lip (72->91)
        connectPoints(92,128)#face boundary (92->127)

        cv2.circle(frame,(face[128][0],face[128][1]),3,yellow,-1)#left pupil (centre->128,adjacent->129)
        rl=findRadius(face[128],face[129])#left iris radius
        cv2.circle(frame,(face[128][0],face[128][1]),int(rl),blue,1)

        cv2.circle(frame,(face[133][0],face[133][1]),3,yellow,-1)#right pupil (centre->133,adjacent->134)
        rr=findRadius(face[133],face[134])#right iris radius
        cv2.circle(frame,(face[133][0],face[133][1]),int(rr),blue,1)

    cv2.imshow('Webcam', frame)
    if cv2.waitKey(1) & 0xff == ord('q'): # to quit the camera press 'q'
        print('end')
        break
cam.release()
cv2.destroyAllWindows()
