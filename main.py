import face_recognition
import cv2
import numpy as np

def draw_landmarks(image, face_landmarks_list, radius=4):
    for face_landmarks in face_landmarks_list:
        for feature in face_landmarks:
            for point in face_landmarks[feature]:
                cv2.circle(image, point, radius, (0, 255, 0), -1)
    return image

# Load a sample picture and learn how to recognize it.
known_image = face_recognition.load_image_file("images/ryan_reynolds_img.jpeg")
known_face_encoding = face_recognition.face_encodings(known_image)[0]
known_face_landmarks = face_recognition.face_landmarks(known_image)

# Convert the known image to BGR color (which OpenCV uses)
known_image_cv = cv2.cvtColor(known_image, cv2.COLOR_RGB2BGR)
# Draw larger landmarks on the known image
known_image_cv = draw_landmarks(known_image_cv, known_face_landmarks, radius=4)

# Load an unknown image to recognize faces in.
unknown_image = face_recognition.load_image_file("images/ryan_gosling_img.png")
unknown_face_encodings = face_recognition.face_encodings(unknown_image)
unknown_face_landmarks = face_recognition.face_landmarks(unknown_image)

# Convert the unknown image to BGR color (which OpenCV uses)
unknown_image_cv = cv2.cvtColor(unknown_image, cv2.COLOR_RGB2BGR)

for unknown_face_encoding in unknown_face_encodings:
    # Compare the faces
    results = face_recognition.compare_faces([known_face_encoding], unknown_face_encoding)

    if results[0]:
        print("Found a match!")
    else:
        print("No match found.")

# Draw smaller landmarks on the unknown image
unknown_image_cv = draw_landmarks(unknown_image_cv, unknown_face_landmarks, radius=2)

# Display both images with facial landmarks
cv2.imshow('Known Face', known_image_cv)
cv2.imshow('Unknown Face', unknown_image_cv)
cv2.waitKey(0)
cv2.destroyAllWindows()
