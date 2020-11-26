import face_recognition as fr
import os
import cv2
import face_recognition
import numpy as np
from time import sleep
import time
import manageFiles as mf

def get_encoded_faces():
    """
    looks through the faces folder and encodes all
    the faces

    :return: dict of (name, image encoded)
    """
    encoded = {}

    for dirpath, dnames, fnames in os.walk("./faces"):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png"):
                encoded[f.split(".")[0]] = get_face_encoding(f)

    return encoded
#assuming we are using faces folder
def get_face_encoding(f):
    face = fr.load_image_file("faces/" + f)
    return fr.face_encodings(face)[0]

#function to return encoding for image given its path
def get_face_encoding_from_path(path, errorList, index):
    face = fr.load_image_file(path)
    try:
        encoding = fr.face_encodings(face)[0]
    except:
        errorList.append(index)
        # Assume the whole image is the location of the face
        height, width, _ = face.shape
        # location is in css order - top, right, bottom, left
        encoding = fr.face_encodings(face, known_face_locations=[(0, width, height, 0)])
    return encoding


def unknown_image_encoded(img):
    """
    encode a face given the file name
    """
    face = fr.load_image_file("faces/" + img)
    encoding = fr.face_encodings(face)[0]

    return encoding


def classify_face(im, data):
    """
    will find all of the faces in a given image and label
    them if it knows what they are

    :param im: str of file path
    :return: list of face names
    """
    #encoded = data['imageNameToEncoding']#get_encoded_faces()
    faces_encoded = data['encodingList'] #list(faces.values())
    known_face_names = data['imageNameList']#list(faces.keys())
    ind = known_face_names.index(im.split('.')[0])#we don't want our test image to be here
    #testImgName = known_face_names.pop(ind)
    testImgEncoding = [faces_encoded.pop(ind)]

    #img = cv2.imread(im, 1)
    #img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
    #img = img[:,:,::-1]

    #face_locations = face_recognition.face_locations(img)
    unknown_face_encodings = testImgEncoding#encoded[im.split('.')[0]]#split to get part before '.'
    #print(type(testImgEncoding))
    #was = face_recognition.face_encodings(img, face_locations)
    #test_name = im.split('.')[0]
    #start_time = time.time_ns()
    face_names = []
    for face_encoding in unknown_face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(faces_encoded, face_encoding)
        name = "Unknown"

        # use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(faces_encoded, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        face_names.append(name)
    return face_names
    #time_to_classify = time.time_ns() - start_time
    #print(time_to_classify)
"""
data = mf.readPickle('encodings')#only have to read in encodings once
start = time.time_ns()
print(classify_face("test.jpg", data))#timed at 0 ns
print("Took "+str(time.time_ns()-start)+" ns")
"""
#original w/o showing image is 4504921400 ns
