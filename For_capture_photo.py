import cv2
cap = cv2.VideoCapture(0)

ret, photo = cap.read()

cv2.imshow("my photo" , photo)

if cv2.waitKey() ==13:
    cv2.destroyAllWindows()
