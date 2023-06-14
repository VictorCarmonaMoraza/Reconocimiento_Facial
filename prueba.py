import cv2
import face_recognition

#Imagen a comparar
image = cv2.imread("images/victor.jpg")
face_loc = face_recognition.face_locations(image)[0]
#print("face_loc:", face_loc)
#Codificamos el rsotro a 128
face_image_encodings= face_recognition.face_encodings(image,known_face_locations =[face_loc])[0]


#print("face_image_encodings:", face_image_encodings)
#imagen2 =face_recognition.load_image_file("images/victor.jpg")
#face_loc = face_recognition.face_locations(imagen2)[0]
#Encuentre y manipule rasgos faciales en imágenes
#face_landmarks_list = face_recognition.face_landmarks(imagen2)[0]

#face_image_encodings= face_recognition.face_encodings(imagen2,known_face_locations =[face_landmarks_list])[0]
#print("Rasgos faciales:", face_image_encodings)

#Detccion facial del rostro
cv2.rectangle(image,(face_loc[3],face_loc[0]),(face_loc[1],face_loc[2]),(0,255,0))
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Leemos el video
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    if ret == False: break
    frame = cv2.flip(frame,1)

    face_locations = face_recognition.face_locations(frame)
    if face_locations !=[]:
        for face_location in face_locations:
            face_frame_encodings = face_recognition.face_encodings(frame,known_face_locations =[face_location])[0]
            #Compara la imagen guardada con las nuevas imagenes
            result = face_recognition.compare_faces([face_frame_encodings], face_image_encodings)
            print("Result:", result)

            if result[0] == True:
                text = "Victor"
                color = (62,151,208)
            else:
                text ="Desconocido"
                color = (50,50,255)

            cv2.rectangle(frame, (face_location[3], face_location[2]), (face_location[1], face_location[2] +30), color, -1)
            cv2.rectangle(frame, (face_location[3], face_location[0]), (face_location[1], face_location[2]),color,2)
            cv2.putText(frame, text, (face_location[3], face_location[2] + 20), 2,0.7,(255,255,255),1)

    cv2.imshow("Frame", frame)
    k = cv2.waitKey(1)
    if k == 27 & 0xFF:
        break

cap.release()
cv2.destroyAllWindows()
