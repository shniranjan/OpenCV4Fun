import cv2
import face_recognition
import os
from c_pk import *
from varbles import *

#dpath = './data'
#fpath = './gID'
#images = []
#classNames = []
myList = os.listdir(fpath)

print('Encoding loading, Please wait.........')

for cl in myList:
        curImg = cv2.imread(f'{fpath}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])

'''
def compute(imge):
    img = cv2.cvtColor(imge, cv2.COLOR_BGR2RGB)
    encode = face_recognition.face_encodings(img)[0]
    return encode
'''
def findEncodings(imges):
    encodeList = []
    kk=0
    for imge in imges:
        print(kk,   myList[kk])
        fpkl = myList[kk].replace('.jpg', '.pkl')
        tem_dpath=f'{dpath}/{fpkl}'
        if os.path.isfile(tem_dpath):
            print("File already encoded")
        else:
            print(f'incoding image #{kk} {myList[kk]}')
            encode = compute(imge)
            save(encode, tem_dpath)
            encodeList.append(encode)
        kk += 1
    return encodeList

#encodeListKnown = findEncodings(images)
#save(encodeListKnown)

print('Encoding Complete')
