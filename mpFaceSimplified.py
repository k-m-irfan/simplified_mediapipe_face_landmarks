# python version 3.9.7
# opncv-python version = 4.5.4.60
# mediapipe version = 0.8.9.1

# ACTUAL MEDIAPIPE FACE LANDMARKS
# Left Eyebrow = [70,63,105,66,107,55,65,52,53,46]
# Right Eyebrow = [300,293,334,296,336,285,295,282,283,276]
# Left Eye = [33,246,161,160,159,158,157,173,133,155,154,153,145,144,163,7]
# Right Eye = [263,466,388,387,386,385,384,398,362,382,381,380,374,373,390,249]
# Inner Lip = [78,191,80,81,82,13,312,311,310,415,308,324,318,402,317,14,87,178,88,95]
# Outer Lip = [61,185,40,39,37,0,267,269,270,409,291,375,321,405,314,17,84,181,91,146]
# Face Boundary = [10,338,297,332,284,251,389,356,454,323,361,288,397,365,379,378,400,377,152,148,176,149,150,136,172,58,132,93,234,127,162,21,54,103,67,109]
# Left iris = [468,469,470,471,472]
# Right iris = [473,474,475,476,477]

# SIMPLIFIED FACE LANDMARKS AFTER SEQUENCING
# Left Eyebrow (0->9)
# right Eyebrow (10->19)
# Left Eye (20->35)
# Right Eye (36->51)
# iner Lip (52->71)
# outer Lip (72->91)
# face boundary (92->127)
# Left iris (128->132)
# Right iris (133->137)


class mpFace:
    import mediapipe as mp
    import cv2
    def __init__(self,width=640,height=480):
        self.findFace = self.mp.solutions.face_detection.FaceDetection()
        self.faceMesh = self.mp.solutions.face_mesh.FaceMesh(False,3,True,0.5,0.5)#(staticFrame,number of faces,True for extra iris landmarks,trackingParameter,findingParameter)
        self.width = width
        self.height = height
    def faceBox(self,frame):#face bounding box
        frameRGB = self.cv2.cvtColor(frame,self.cv2.COLOR_BGR2RGB)
        results = self.findFace.process(frameRGB)
        myFaces = []
        if results.detections != None:
            for face in results.detections:
                bBox = face.location_data.relative_bounding_box
                topLeft = (int(bBox.xmin*self.width),int(bBox.ymin*self.height))
                bottomRight = (int((bBox.xmin+bBox.width)*self.width),int((bBox.ymin+bBox.height)*self.height))
                myFaces.append((topLeft,bottomRight))
        return myFaces
    def faceLandmarks(self,frame):#Full Face Landmarks
        frameRGB = self.cv2.cvtColor(frame,self.cv2.COLOR_BGR2RGB)
        results = self.faceMesh.process(frameRGB)
        myFacesLandmarks=[]
        myFaceLandmarks=[]
    
        if results.multi_face_landmarks != None:
            for faceLandmarks in results.multi_face_landmarks:
                for lm in faceLandmarks.landmark:
                    myFaceLandmarks.append((int(lm.x*self.width),int(lm.y*self.height)))

                myFacesLandmarks.append(myFaceLandmarks)            
        return myFacesLandmarks

    def faceLandmarksSimplified(self,frame):#essential face landmarks(left eyebrow,righteyebrow,left eye,right eye,inner lips,outer lips,face outline,left iris and right iris)
        frameRGB = self.cv2.cvtColor(frame,self.cv2.COLOR_BGR2RGB)
        results = self.faceMesh.process(frameRGB)
        #sequenced indexes of required landmarks from original landmarks
        points = [70,63,105,66,107,55,65,52,53,46,300,293,334,296,336,285,295,282,283,276,33,246,161,160,159,158,157,173,133,155,154,153,145,144,163,7,263,466,388,387,386,385,384,398,362,382,381,380,374,373,390,249,78,191,80,81,82,13,312,311,310,415,308,324,318,402,317,14,87,178,88,95,61,185,40,39,37,0,267,269,270,409,291,375,321,405,314,17,84,181,91,146,10,338,297,332,284,251,389,356,454,323,361,288,397,365,379,378,400,377,152,148,176,149,150,136,172,58,132,93,234,127,162,21,54,103,67,109,468,469,470,471,472,473,474,475,476,477]
        myFaceLandmarksSimplified=[]
        myFacesLandmarksSimplified=[]
        myFaceLandmarksRearranged = [0]*len(points)
        myIndex=[]
    
        if results.multi_face_landmarks != None:
            for faceLandmarks in results.multi_face_landmarks:
                for lm,indx in zip(faceLandmarks.landmark,range(len(faceLandmarks.landmark))):
                    if indx in points:#only collect required landmarks
                        myFaceLandmarksSimplified.append((int(lm.x*self.width),int(lm.y*self.height)))
                        myIndex.append(points.index(indx))#for rearranging the points, collect sequenced index
                    for i,indx in zip(range(len(points)),myIndex):
                        myFaceLandmarksRearranged[indx] = myFaceLandmarksSimplified[i]#rearranging according to sequenced index

                myFacesLandmarksSimplified.append(myFaceLandmarksRearranged)          
        return myFacesLandmarksSimplified