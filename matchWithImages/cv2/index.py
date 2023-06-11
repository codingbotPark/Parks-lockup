import cv2
import numpy as np

# 얼굴 인식을 위한 Haar Cascade 파일 경로
cascade_path = "./haarcascade_frontalface_default.xml"

# 얼굴 인식을 위한 CascadeClassifier 객체 생성
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + cascade_path)

# Webcam 캡처를 위한 VideoCapture 객체 생성
cap = cv2.VideoCapture(0)

# 주인의 얼굴 이미지 경로
owner_face_path = "./my_image.jpg"

# 주인의 얼굴 이미지를 로드하여 특징 벡터 생성
owner_face = cv2.imread(owner_face_path, cv2.IMREAD_GRAYSCALE)
owner_face = cv2.resize(owner_face, (150, 150))
owner_face_vector = np.array(owner_face, dtype=np.uint8)

# 주인의 얼굴 특징 벡터 생성을 위한 LBPHFaceRecognizer 객체 생성
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

face_recognizer.train([owner_face_vector], np.array([1]))

while True:
    # Webcam에서 프레임 읽기
    ret, frame = cap.read()

    # 회색조로 변환
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 얼굴 인식 수행
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # 인식된 얼굴 영역 잘라내기
        face = gray[y:y+h, x:x+w]
        face = cv2.resize(face, (150, 150))

        # 얼굴 인식 결과 예측
        label, confidence = face_recognizer.predict(face)

        # 얼굴이 주인인 경우
        if label == 1:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
            cv2.putText(frame, "Owner", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        else:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)
            cv2.putText(frame, "Unknown", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    # 화면에 프레임 출력
    cv2.imshow('Face Recognition', frame)

    # 'q'를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 객체와 윈도우 해제
cap.release()
cv2.destroyAllWindows()