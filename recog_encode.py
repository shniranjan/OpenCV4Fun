import cv2
import os
import c_pk as cpk
import varbles as var

images = []
classNames = []

dpath = var.dpath
fpath = var.fpath
myList = os.listdir(fpath)

print('Encoding loading, Please wait.........')

for cl in myList:
        curImg = cv2.imread(f'{fpath}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])

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
            encode = cpk.compute(imge)
            cpk.save(encode, tem_dpath)
            encodeList.append(encode)
        kk += 1
    return encodeList

encodeListKnown = findEncodings(images)

print('Encoding Complete')
