import cv2
import matplotlib.pyplot as plt
import pyautogui as robot 

eye_model = cv2.CascadeClassifier("haarcascade_eye.xml")
face_model = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

loop = True
cam = cv2.VideoCapture(0)
while loop:
    _, img = cam.read()
    img = cv2.flip(img,1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = face_model.detectMultiScale(gray)
    imgout = img.copy()
    if len(face) > 0:
        x = face[0][0]
        y = face[0][1]
        x2 = x + face[0][2]
        y2 = y + face[0][3]
        gray_face = gray[y:y2, x:x2]
        print(f"X:{x},Y:{y}")
        eye = eye_model.detectMultiScale(gray_face, minSize=(30, 30), scaleFactor=1.1, minNeighbors=5)
        
        out = cv2.rectangle(imgout, (x, y), (x2, y2), (0, 250, 0), 2)
        white = (250,250,250)
        red = (0,0,250)
        range = white
        
        mouse_x = robot.position().x
        mouse_y = robot.position().y

        if y<80:
            range = red
            mouse_y = mouse_y - abs(y-80)
            robot.moveTo(mouse_x,mouse_y,0)

        if y2>350:
            range = red
            mouse_y = mouse_y + abs(y2-350)
            robot.moveTo(mouse_x,mouse_y,0)

        if x<200:
            range = red
            mouse_x = mouse_x - abs(x-200)
            robot.moveTo(mouse_x,mouse_y,0)

        if x2>450:
            range = red
            mouse_x = mouse_x + abs(x2-450)
            robot.moveTo(mouse_x,mouse_y,0)

        out = cv2.rectangle(imgout,(200,80),(450,350),range,2)
        
        ic = 0
        for (xe, ye, w, h) in eye:
            ic += 1
            cv2.rectangle(imgout, (xe + x, ye + y), (xe + w + x, ye + h + y), (0, 0, 250), 2)
            if ic == 2:
                break
    else:
        out = imgout
    cv2.imshow("Alireza", out)
    if cv2.waitKey(1) == ord("q"):
        loop = False
        cam.release()
        cv2.destroyAllWindows()
