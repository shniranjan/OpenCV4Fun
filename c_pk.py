import pickle
import gzip
import cv2
import face_recognition

#filename= 'c_object.obj'
# filename='newDump.pkl'

def compute(imge):
    img = cv2.cvtColor(imge, cv2.COLOR_BGR2RGB)
    encode = face_recognition.face_encodings(img)[0]
    return encode


def save(object, filename, protocol = 0):
    """Saves a compressed object to disk
    """
    file = gzip.GzipFile(filename, 'wb')
    file.write(pickle.dumps(object, protocol))
    file.close()


def load(filename):
    """Loads a compressed object from disk
    """
    file = gzip.GzipFile(filename, 'rb')
    data = file.read()    
    object = pickle.loads(data)
    file.close()
    return object
