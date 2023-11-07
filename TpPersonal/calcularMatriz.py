from flask import Flask, request, json, jsonify
import cv2
import face_recognition
import numpy as np
import base64
import json
from flask_cors import CORS
import re
import time
import subprocess

app = Flask(__name__)
CORS(app, methods=['GET', 'POST', 'PUT', 'DELETE'], allow_headers=['Content-Type', 'Authorization'])

@app.post('/calcular-matriz')
def calcular():
    try:
        data = request.json
        image = data["imagen64"]
        image = str(image).replace(" ", "")
        image = base64.b64decode(image) #Decodifica en datos binarios       
        image = np.frombuffer(image, np.uint8) #Lo convierte en un array de numpy
        image = cv2.imdecode(image, cv2.IMREAD_COLOR) #Decodifica la imagen en un formato que opencv pueda leer
        faces_loc=face_recognition.face_locations(image) #Encuentra las caras en la imagen
        faces = []
        for fl in faces_loc:
            model=face_recognition.face_encodings(image, known_face_locations=[fl]) #Calcula la matriz del rostro identificado a partir de dlib
            face_array = np.array(model) #Convierte la matriz en un array de numpy
            flattened_array = face_array.flatten().tolist() #Convierte el array en una lista
            formatted = str(flattened_array).replace("'", "").replace("[", "").replace("]", "").replace(",", "")
            faces.append(formatted)     
        response = jsonify(matriz=faces)
        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response
    except Exception as e:
        print(e)
        response = jsonify(error=e)
        response.status_code = 500
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response
    
@app.post('/detectar-rostro')
def detectar():
    try:
        data = request.json
        matriz = data["matriz"]
        with open("perfil.txt", "w") as file:
            file.write(matriz)
        output = subprocess.check_output(["python", "IdentificaRostro.py"])
        output = output.decode("utf-8")
        response = jsonify(msg=output)
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        if(output[0] == "1"):
            response.status_code = 200
        else:
            response.status_code = 403
        return response
    except Exception as e:
        print(e)
    response.status_code = 404
    return response
   

if __name__ == '__main__':
    app.run(debug=True, host='192.168.192.6', port=8100)