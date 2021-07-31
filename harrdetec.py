import cv2

cv2_carclass = cv2.CascadeClassifier("haarcar.xml")
cap = cv2.VideoCapture("video.mp4")

count_line_pos = 430
offset = 6

couter = 2

def center_find(x, y, w, h):
    
    x1 = int(w/2)
    y1 = int(h/2)
    cx = x + x1
    cy = y + y1
    return cx , cy

detect = []

while True:

    _, frame = cap.read()
    frame2 = frame 
    #roi = frame[400:,100:850]
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    roi = gray_frame[:,100:850]
    cars = cv2_carclass.detectMultiScale(roi, 1.2, 2)

    cv2.line(frame2, (80, count_line_pos), (1000, count_line_pos), (0, 0, 255), 3)

    for (x, y ,w ,h) in cars:

        x = x + 100
        cv2.rectangle(frame2, (x, y), (x+w, y+h), (0, 255, 255), 2)
        #cv2.imshow('Cars', frame)

        center = center_find(x, y, w, h)
        detect.append(center)
        cv2.circle(frame2, center, 4, (0, 0, 255), -1)

        for (x, y) in detect:

            if y < (count_line_pos + offset) and y > (count_line_pos - offset):

                couter += 1

                cv2.line(frame2, (80, count_line_pos), (1000, count_line_pos), (0, 255, 0), 3)
                detect.remove((x, y))
                print("VAHICLE COUNT" + str(couter))

    cv2.putText(frame2, "VEHICLE COUNT : " + str(couter), (450, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)

    cv2.imshow("cars", frame2)

    if cv2.waitKey(1) == 13: #13 is the Enter Key
        break

cap.release()
cv2.destroyAllWindows()