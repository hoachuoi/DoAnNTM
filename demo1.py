import face_recognition
import os
import pickle
import numpy as np

MatDaBiet = 'train'
#mang chua ma hoa cua cua mat da huan luyen
encoded_faces = {}

for name in os.listdir(MatDaBiet):
    for file_name in os.listdir(f'{MatDaBiet}/{name}'):
        #tai anh
        image = face_recognition.load_image_file(f'{MatDaBiet}/{name}/{file_name}')
        #xac dinh mat
        
        faceloc = face_recognition.face_locations(image, model= 'hog')
        
        if(len(faceloc) > 0):
            #ma hoa cac mat da duoc xac dinh
            encoded_faces[name+ "_" + file_name] = face_recognition.face_encodings(image, faceloc)
with open('train.dat', 'wb') as f:
                # ma hoa vao tep
                pickle.dump(encoded_faces, f)
print("Mat duoc ma hoa")            
