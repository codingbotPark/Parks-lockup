import cv2
import face_recognition

image_to_be_matched = face_recognition.load_image_file('my_image.jpg')
image_to_be_matched_encoded = face_recognition.face_encodings(image_to_be_matched)[0]

name = "byoungkwan"

webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("Could not open webcam")
    exit()



while webcam.isOpened():
    status, frame = webcam.read()

    if not status:
        print("Could not read frame")
        exit()
    
    try:
        face_encoded = face_recognition.face_encodings(frame)[0]
        result = face_recognition.compare_faces([image_to_be_matched_encoded], face_encoded)
        print(result)
        print(result[0])
    except:
        print("Could not find face")
        pass
    # face_locations = face_recognition.face_locations(frame, number_of_times_to_upsample=0) # CNN 기반 얼굴 검출기
 
    # for face_location in face_locations:
    #     top, right, bottom, left = face_location
    #     face_image = frame[top:bottom, left:right]
 
    #     try:
    #         face_encoded = face_recognition.face_encodings(face_image)[0]
    #         result = face_recognition.compare_faces([image_to_be_matched_encoded], face_encoded)
    #         # result = face_recognition.compare_faces([image_to_be_matched_encoded], face_encoded, 0.5)
 
    #         if result[0] == True:
    #             # cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
    #             Y = top - 10 if top - 10 > 10 else top + 10
    #             text = name
    #             # cv2.putText(frame, text, (left, Y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    #     except:
    #         pass
 
    # # display output
    # cv2.imshow("detect me", frame) 
 
    # press "Q" to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
