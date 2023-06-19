import face_recognition
from openpyxl import Workbook

import os


# 로드할 파일의 파일확장자
fileExtension = [
    '.jpg',
    '.png',
    '.jpeg'
]

def loadFile(file,dir):
    # .jpg, .png, .jpeg 파일만 로드
    if '.' + file.split('.')[-1] in fileExtension:
        return os.path.join(dir,file)
    

def registImgs():
    # registImgs 는 __init__.py 에 의해 호출되기 때문에, 이에따른 경로를 설정
    registerList = list(map(lambda file:loadFile(file,'./imgs'),os.listdir('./imgs')))
    print(registerList)
    encodedImgs = list(map(encodingImg,registerList))
    makeExel(encodedImgs,registerList)
    

def encodingImg(path):
    loadedImg = face_recognition.load_image_file(path)
    EncodedImg = face_recognition.face_encodings(loadedImg)

    if (len(EncodedImg)):
        return EncodedImg[0]
    else:
        print("Cannot find face")
        return False



def makeExel(imgArray,registerList):
    workbook = Workbook()
    # 기본 시트 선택
    ws = workbook.active
    # 인덱스와 값으로 사용한다
    for row_idx, row in enumerate(imgArray, start=1):
        for col_idx, value in enumerate(row, start=1):
            ws.cell(row=row_idx, column=col_idx, value=value)
        print(registerList[row_idx-1],"등록")
    workbook.save('user.xlsx')
    