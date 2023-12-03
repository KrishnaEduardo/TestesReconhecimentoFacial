import cv2
from simple_facerec import SimpleFacerec
import datetime
import sqlite3
import requests
con = sqlite3.connect("usuarios.db")

# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

# Load Camera
cap = cv2.VideoCapture(0)
now = datetime.datetime.now()

def banco(usuario):
    query1 = f"select usuario, telefone, apikey from usuarios where id = ?"
    res = con.execute(query1, (usuario,))
    retorno = res.fetchone()

    if retorno:
        query2 = f"select * from registros where created_At < datetime('now', 'localtime', '-600 seconds') and usuario_id = ?"
        res2 = con.execute(query2, (usuario,))
        resultado = res2.fetchone()
        if not resultado:
            return retorno

def requisicao(usuario, telefone, apikey):
    mensagem = f"Ponto Registrado - {now.day}/{now.month}/{now.year} - {now.hour}:{now.minute}"
    url = f"https://api.callmebot.com/whatsapp.php?phone={telefone}&text={mensagem}&apikey={apikey}"
    payload = {}
    headers = {}
    response  = requests.request("GET", url, headers=headers, data=payload)
    print(response)

cache = set()
while True:
    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        dados = banco(face_names[0])
        
        if dados is not None:
            if dados not in cache:
                faces_cache = (dados[0], dados[1], dados[2])
                cache.add(faces_cache)  
                requisicao(dados[0], dados[1], dados[2])
            else:
                cv2.putText(frame, dados[0],(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        else:
            cv2.putText(frame, 'desconhecido',(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)                 
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
            
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break


 

cap.release()
cv2.destroyAllWindows()