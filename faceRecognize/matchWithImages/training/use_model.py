#카메라열기
cap = cv2.VideoCapture(0)

while True:
    #카메라에서 사진 한장 읽기

    ret, frame = cap.read()

    #얼굴 검출해내기
    image,unknownface = face_detector(frame)

    try:
        #검출된 사진을 흑백으로 변환
        unknownface = cv2.cvtColor(unknownface, cv2.COLOR_BGR2GRAY)
        #predict_img = predict(unknownface)

        #print("Prediction complete")

        result = model.predict(unknownface)

        if result[1] < 500:
            confidence = int(100*(1-(result[1])/300))
            display_string = str(confidence)+'% Confidence it is user'
        cv2.putText(image,display_string,(100,120), cv2.FONT_HERSHEY_COMPLEX,1,(250,120,255),2)


        if confidence > 75:
            cv2.putText(image, "Hi Deeperent Member!", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('Face Cropper', image)

        else:
            cv2.putText(image, "OutSider!", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow('Face Cropper', image)

        

    except:
        cv2.putText(image, "Face Not Found", (400,500), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0),2)
        print("Face Not Found!")
        #cv2.imshow('Fail Face Cropper',image)
        pass

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()