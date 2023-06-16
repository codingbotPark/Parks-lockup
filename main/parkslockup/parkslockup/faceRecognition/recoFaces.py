import cv2
import face_recognition
import registUser

def useWithWebCam():

    video_capture = cv2.VideoCapture(0)
    # while True: