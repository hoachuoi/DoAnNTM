import face_recognition
import os
import pickle
import numpy as np

#MatChuaBiet = 'test'
#mo tep
a = 'test.jpg'
with open('train.dat', 'rb') as f:
    encoded_faces = pickle.load(f)
#ten cua mat ma hoa
face_name = list(encoded_faces.keys())
# gia tri cua ma
face_encodings = np.array(list(encoded_faces.values()), dtype= object)
img = face_recognition.load_image_file('test.jpg')
face_loc = face_recognition.face_locations(img, model='hog')
test_encode = face_recognition.face_encodings(img, face_loc)

for i in range(0, len(face_encodings)):
    result = face_recognition.compare_faces(face_encodings[i], test_encode)
    if result == True:
        print("anh test du bao" )
        break