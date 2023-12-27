# pip freeze > requirements.txt
import face_recognition
import cv2
import numpy as np

# Load a sample picture and learn how to recognize it.
known_image = face_recognition.load_image_file("images/ryan_reynolds_img.jpeg")  # known image
known_face_encoding = face_recognition.face_encodings(known_image)[0]

# Load an unknown image to recognize faces in.
unknown_image = face_recognition.load_image_file("images/ryan_gosling_img.png")  # unknown image
unknown_face_encodings = face_recognition.face_encodings(unknown_image)

# There might be more than one person in the unknown image, so we need to loop over each face we found
for unknown_face_encoding in unknown_face_encodings:
    # Compare the faces
    results = face_recognition.compare_faces([known_face_encoding], unknown_face_encoding)

    if results[0]:
        print("Found a match!")
    else:
        print("No match found.")
