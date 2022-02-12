import cv2
import os
from c_pk import compute, save
from varbles import dpath, fpath

images = []
classNames = []

if not os.path.exists(dpath):
    os.makedirs(dpath)

if os.path.exists(fpath):    
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
            encode = compute(imge)
            save(encode, tem_dpath)
            encodeList.append(encode)
        kk += 1
    return encodeList

encodeListKnown = findEncodings(images)

print('Encoding Complete')
