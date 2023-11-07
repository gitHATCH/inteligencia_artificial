import cv2
import face_recognition
import numpy as np
import base64
import json
import re
import time
import sys

matriz = np.loadtxt("./perfil.txt") #Carga matriz numpy del rostro
cap=cv2.VideoCapture(0) #Inicia la captura de video
global start_time
start_time = time.time()
while True:
    ret, frame=cap.read() #Lee el frame
    if ret == False: 
        break
    frame=cv2.flip(frame,1) #Voltea horizontalmente el frame (espejo)
    faces_loc=face_recognition.face_locations(frame) #Encuentra las caras en el frame
    for fl in faces_loc:
        model=face_recognition.face_encodings(frame, known_face_locations=[fl]) #Calcula la matriz del rostro identificado a partir de dlib
        result=False #Variable para saber si el rostro es el mismo
        for f in model:
            result = result or True in face_recognition.compare_faces([matriz],f) #Compara la matriz del rostro identificado con la matriz del rostro guardado
        quien="Desconocid@"
        if result: #Si el rostro es el mismo
            cap.release() 
            cv2.destroyAllWindows()
            print(1)
        cv2.rectangle(frame, (fl[3], fl[2]), (fl[1], fl[2]+30), (50,50,255), -1 ) #Dibuja un rectangulo en el frame
        cv2.rectangle(frame, (fl[3], fl[0]), (fl[1], fl[2]), (50,50,255), 2 ) 
        cv2.putText(frame, quien , (fl[3], fl[2]+20),2,0.7,(255,255,255), 1) 
    cv2.imshow('video', frame)
    key=cv2.waitKey(1)
    if key == ord('q') or key==27:
        break  
    if time.time() - start_time > 10:
        print("Se termino el tiempo")
        break
cap.release()
cv2.destroyAllWindows()
sys.exit(0)