import cv2

ddept=cv2.CV_16S
scale=1
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ref, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    x = cv2.Sobel(gray, ddept, 1,0, ksize=3, scale=1)
    y = cv2.Sobel(gray, ddept, 0,1, ksize=3, scale=1)
    absx= cv2.convertScaleAbs(x)
    absy = cv2.convertScaleAbs(y)
    grad = cv2.addWeighted(absx, 0.5, absy, 0.5,0)
    cv2.imshow('edge', grad)
    cv2.imshow('main', frame)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
cap.release()
