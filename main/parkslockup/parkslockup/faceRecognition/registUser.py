import face_recognition
from openpyxl import Workbook


registerList = [
    './imgs/ParkByoungkwan.jpg',
]

def registImgs():
    encodedImgs = list(map(encodingImg,registerList))
    makeExel(encodedImgs)
    

def encodingImg(path):
    loadedImg = face_recognition.load_image_file(path)
    EncodedImg = face_recognition.face_encodings(loadedImg)

    if (len(EncodedImg)):
        return EncodedImg[0]
    else:
        print("Cannot find face")
        return False



def makeExel(imgArray):
    workbook = Workbook()
    # 기본 시트 선택
    ws = workbook.active
    # 인덱스와 값으로 사용한다
    for row_idx, row in enumerate(imgArray, start=1):
        for col_idx, value in enumerate(row, start=1):
            ws.cell(row=row_idx, column=col_idx, value=value)
        print(registerList[row_idx-1],"등록")
    workbook.save('user.xlsx')
    