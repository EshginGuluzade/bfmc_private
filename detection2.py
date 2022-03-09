import cv2
import time

# Stop Sign Cascade Classifier xml
stop_sign = cv2.CascadeClassifier('cascade_classifiers/cascade_stop_sign.xml')
# No entry Sign Cascade Classifier xml
no_entry_sign = cv2.CascadeClassifier('cascade_classifiers/cascade_no_entry_sign.xml')
# Stop Sign Cascade Classifier xml
yield_sign = cv2.CascadeClassifier('cascade_classifiers/cascade_yield_sign_v2.xml')
# One way Sign Cascade Classifier xml
one_way_sign = cv2.CascadeClassifier('cascade_classifiers/cascade_one_way_sign.xml')
# Parking Sign Cascade Classifier xml
parking_sign = cv2.CascadeClassifier('cascade_classifiers/cascade_park2.xml')
# Crosswalk Sign Cascade Classifier xml
crosswalk_sign = cv2.CascadeClassifier('cascade_classifiers/cascade_crosswalk_sign_v2.xml')
# Roundabout Sign Cascade Classifier xml
roundabout_sign = cv2.CascadeClassifier('cascade_classifiers/cascade_v1.xml')

cap = cv2.VideoCapture(0)
#cap.set(4, 480)
#cap.set(3, 360)term
#time.sleep(5)

while cap.isOpened():
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    stop_sign_scaled = stop_sign.detectMultiScale(gray, 1.3, 5)
    no_entry_sign_scaled = no_entry_sign.detectMultiScale(gray, 1.2, 5)
    yield_sign_scaled = yield_sign.detectMultiScale(gray, 1.2, 5)
    one_way_sign_scaled = one_way_sign.detectMultiScale(gray, 1.3, 5)
    parking_sign_scaled = parking_sign.detectMultiScale(gray, 1.3, 5)
    crosswalk_sign_scaled = crosswalk_sign.detectMultiScale(gray, 1.2, 5)
    round_sign_scaled = roundabout_sign.detectMultiScale(gray, 1.3, 5)

    # # Detect the stop sign, x,y = origin points, w = width, h = height (w, h = bottom right corner)
    # for (x,y,w,h) in stop_sign_scaled:
    #     # Draw rectangle around the stop sign
    #     stop_sign_rectangle = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
    #     # Write "Stop Sign" on bottom of rectangle
    #     stop_sign_text = cv2.putText(img=stop_sign_rectangle, text="Stop Sign", org=(x, y+h+30),
    #                                  fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
    #                                  color=(0,0,255), thickness=2, lineType=cv2.LINE_4)

    # # Detect the no entry sign, x,y = origin points, w = width, h = height (w, h = bottom right corner)
    # for (x,y,w,h) in no_entry_sign_scaled:
    #     # Draw rectangle around the no entry sign
    #     no_entry_sign_rectangle = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
    #     # Write "No entry Sign" on bottom of rectangle
    #     no_entry_sign_text = cv2.putText(img=no_entry_sign_rectangle, text="No entry Sign", org=(x, y+h+30),
    #                                  fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
    #                                  color=(0,0,255), thickness=2, lineType=cv2.LINE_4)
    #
    # Detect the yield sign, x,y = origin points, w = width, h = height (w, h = bottom right corner)
    # for (x,y,w,h) in yield_sign_scaled:
    #     # Draw rectangle around the yield sign
    #     yield_sign_rectangle = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
    #     # Write "Yield Sign" on bottom of rectangle
    #     yield_sign_text = cv2.putText(img=yield_sign_rectangle, text="Yield Sign", org=(x, y+h+30),
    #                                  fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
    #                                  color=(0,0,255), thickness=2, lineType=cv2.LINE_4)
    #
    # # Detect the one_way sign, x,y = origin points, w = width, h = height (w, h = bottom right corner)
    # for (x,y,w,h) in one_way_sign_scaled:
    #     # Draw rectangle around the one way sign
    #     one_way_sign_rectangle = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
    #     # Write "Onw waySign" on bottom of rectangle
    #     one_way_sign_text = cv2.putText(img=one_way_sign_rectangle, text="One way Sign", org=(x, y+h+30),
    #                                  fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
    #                                  color=(0,0,255), thickness=2, lineType=cv2.LINE_4)
    #
    # # Detect the parking sign, x,y = origin points, w = width, h = height (w, h = bottom right corner)
    # for (x,y,w,h) in parking_sign_scaled:
    #     # Draw rectangle around the parking sign
    #     parking_sign_rectangle = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
    #     # Write "Parking" on bottom of rectangle
    #     parking_sign_text = cv2.putText(img=parking_sign_rectangle, text="Parking Sign", org=(x, y+h+30),
    #                                  fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
    #                                  color=(0,0,255), thickness=2, lineType=cv2.LINE_4)
    #
    #
    # # Detect the crosswalk sign, x,y = origin points, w = width, h = height (w, h = bottom right corner)
    # for (x,y,w,h) in crosswalk_sign_scaled:
    #     # Draw rectangle around the crosswalk sign
    #     crosswalk_sign_rectangle = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
    #     # Write "Crosswalk" on bottom of rectangle
    #     crosswalk_sign_text = cv2.putText(img=crosswalk_sign_rectangle, text="Crosswalk Sign", org=(x, y+h+30),
    #                                  fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
    #                                  color=(0,0,255), thickness=2, lineType=cv2.LINE_4)
    #
    # Detect the crosswalk sign, x,y = origin points, w = width, h = height (w, h = bottom right corner)
    for (x,y,w,h) in round_sign_scaled:
        # Draw rectangle around the crosswalk sign
        round_sign_rectangle = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
        # Write "Crosswalk" on bottom of rectangle
        round_sign_text = cv2.putText(img=round_sign_rectangle, text="Roundabout Sign", org=(x, y+h+30),
                                     fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                                     color=(0,0,255), thickness=2, lineType=cv2.LINE_4)

    cv2.imshow("img", img)

    key = cv2.waitKey(30)
    if key == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break