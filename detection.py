import cv2
import numpy as np

stop_sign = cv2.CascadeClassifier('stop_sign_classifier_2.xml')

cap = cv2.VideoCapture('video_test.mp4')
cap.set(4, 480)
cap.set(3, 360)

count = 0
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Screen", img)
    ss = stop_sign.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in ss:
        print("Stop_sign_detected", count)
        count+=1
        print(x,y,w,h)
        cv2.rectangle(img, (x, y), (x+w, y+h), (200, 0, 50), 3)

    key = cv2.waitKey(30)
    if key == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break

