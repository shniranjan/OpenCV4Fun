import cv2
import numpy as np
import face_recognition
import os
import requests
import c_pk as cpk
import varbles as var

myList = os.listdir(var.fpath)
dpath = var.dpath
fpath = var.fpath
mlr = var.mlr
url=var.url
images = []
classNames = []


def findEncodings(myList):
    eList = []
    kk=0
    for im in myList:
        print(kk,   im)
        fpkl = im.replace('.jpg', '.pkl')
        classNames.append(os.path.splitext(im)[0])
        tem_dpath=f'{dpath}/{fpkl}'
        if os.path.isfile(tem_dpath):
            print(f'Encode loading from {tem_dpath}.....')
            encode=cpk.load(tem_dpath)
            eList.append(encode)
        else:
            print(f'{im} file is not encoded.')
        kk += 1
    return eList

#load encoded data
encodeListKnown = findEncodings(myList)


#cap = cv2.VideoCapture()

while True:

    #if webCamFeed:success, img = cap.read()
    #else:img = cv2.imread(pathImage)
    #else:
    
    imgg = requests.get(url)

    #img_arr = np.array(bytearray(imgg.content), dtype=np.uint8)
    #img = cv2.imdecode(img_arr, -1)
    img = cv2.imdecode(np.array(bytearray(imgg.content), dtype=np.uint8), -1)   

    imgS = cv2.resize(img, (0,0), None, 1/mlr, 1/mlr) # RESIZE IMAGE to 1/mlr
    imgS =cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    
    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)
    
    for encodeFace,faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
        #print(faceDis) #need to connect webCamFeed
        matchIndex = np.argmin(faceDis)
                
        if matches[matchIndex]:
            name = classNames[matchIndex]
            
            y1,x2,y2,x1 = faceLoc
            y1,x2,y2,x1 = y1*mlr,x2*mlr,y2*mlr,x1*mlr
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),1)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255.0),1) #cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255.0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1)
    
    
    
    cv2.imshow('Webcam', img)
    
    #waits and exits if pressed escape key
    if cv2.waitKey(300)== 27:
        exit()
