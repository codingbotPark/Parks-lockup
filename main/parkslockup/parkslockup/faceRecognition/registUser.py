import face_recognition
from openpyxl import Workbook
import os
import numpy as np

# 로드할 파일의 파일확장자
fileExtension = [
    '.jpg',
    '.png',
    '.jpeg',
]
imgDirPath = "./imgs"
# registImgs 는 __init__.py 에 의해 호출된다, 이에따른 경로를 설정
def loadFile(file,dir):
    # .jpg, .png, .jpeg 파일만 로드
    if '.' + file.split('.')[-1] in fileExtension:
        return os.path.join(dir,file)
    
registerList = list(filter(None,map(lambda file:loadFile(file,imgDirPath),os.listdir(imgDirPath))))
print(registerList)

# --------

def registImgs():
    print(registerList)
    encodedImgs = list(map(encodingImg,registerList))
    # 배열에서 얼굴을 못 찾은, 즉 none값을 없애준다
    encodedImgs = list(filter(lambda x: isinstance(x,np.ndarray),encodedImgs))
    makeExel(encodedImgs,registerList)
    

def encodingImg(path):
    loadedImg = face_recognition.load_image_file(path)
    EncodedImg = face_recognition.face_encodings(loadedImg)

    if (len(EncodedImg)):
        return EncodedImg[0]
    else:
        print("Cannot find face")
        return None



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
    