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

 
    # press "Q" to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
