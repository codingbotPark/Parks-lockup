
import os
import face_recognition
from PIL import Image


image_to_be_matched = face_recognition.load_image_file('my_image.jpg')
image_to_be_matched_encoded = face_recognition.face_encodings(image_to_be_matched)[0]

ext=['jpg','png','gif','jpeg']
for filename in os.listdir('images '):
    if filename.split(".")[-1] in ext:
        Image.open(f'{"images"}/{filename}').save(f'{"realImages"}/{filename}', 'png')

realImages = os.listdir("realImages")

# iterate over each image
for image in realImages:
    # load the image
    current_image = face_recognition.load_image_file("images/" + image)
    # encode the loaded image into a feature vector
    
    print(image)

    if (len(face_recognition.face_encodings(current_image)) > 0):
        current_image_encoded = face_recognition.face_encodings(current_image)[0]
        # match your image with the image and check if it matches
        result = face_recognition.compare_faces([image_to_be_matched_encoded], current_image_encoded)
        # check if it was a match
        if result[0] == True:
            print("Matched: " + image)
        else:
            print("Not matched: " + image)
    else:
        print("cannot find face")


         


    


