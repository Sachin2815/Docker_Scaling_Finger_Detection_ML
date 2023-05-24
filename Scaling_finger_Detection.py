import cv2
import  urllib.request
from cvzone.HandTrackingModule import HandDetector
detector = HandDetector(maxHands=1 , detectionCon=0.8 )

cap = cv2.VideoCapture(0)

while True:
    ret,  photo = cap.read()
    hand = detector.findHands(photo , draw=False )
    
    if hand:
        detectHand = hand[0]
        if detectHand:
            fingerup = detector.fingersUp(detectHand) 
            if detectHand['type'] == 'Right':
                if fingerup == [0, 1, 1, 0, 0]:
                    print("initial 2 finger : inititaed creating 2 docker containers")
                    # AI Model
                    for i in range(2):
                        request_url = urllib.request.urlopen("https://oh9jhr9pw3.execute-api.ap-south-1.amazonaws.com/test/docker")
                        print ( request_url.read() )
         
                
                elif   fingerup == [0, 1, 1, 1, 0]:
                    print("middle 3 finger up : inititaed creating 3 docker containers")
                     # AI Model
                    for i in range(3):
                        request_url = urllib.request.urlopen("https://oh9jhr9pw3.execute-api.ap-south-1.amazonaws.com/test/docker")
                        print ( request_url.read() )
                
                elif   fingerup == [0, 1, 1, 1, 1]:
                    print("middle 4 finger up : inititaed creating 4 docker containers")
                     # AI Model
                    for i in range(4):
                        request_url = urllib.request.urlopen("https://oh9jhr9pw3.execute-api.ap-south-1.amazonaws.com/test/docker")
                        print ( request_url.read() )
                
                elif   fingerup == [1, 1, 1, 1, 1]:
                    print("all finger up : inititaed creating 5 docker containers")
                    for i in range(5):
                        request_url = urllib.request.urlopen("https://oh9jhr9pw3.execute-api.ap-south-1.amazonaws.com/test/docker")
                        print ( request_url.read() )
                
            
            else:
                
                if fingerup == [0, 1, 1, 0, 0]:
                    print("initial 2 finger : intiated removing 2 docker containers")
                    # AI Model
                    for i in range(2):
                        request_url = urllib.request.urlopen("https://oh9jhr9pw3.execute-api.ap-south-1.amazonaws.com/test/rmvcont")
                        print ( request_url.read() )
                
                    # AI Model
                
                elif   fingerup == [0, 1, 1, 1, 0]:
                    print("middle 3 finger up : intiated removing 3 docker containers")
                    for i in range(3):
                        request_url = urllib.request.urlopen("https://oh9jhr9pw3.execute-api.ap-south-1.amazonaws.com/test/rmvcont")
                        print ( request_url.read() )
                
                elif   fingerup == [0, 1, 1, 1, 1]:
                    print("middle 4 finger up : intiated removing 4 docker containers")
                    for i in range(4):
                        request_url = urllib.request.urlopen("https://oh9jhr9pw3.execute-api.ap-south-1.amazonaws.com/test/rmvcont")
                        print ( request_url.read() )
                
                elif   fingerup == [1, 1, 1, 1, 1]:
                    print("all finger up : intiated removing 5 docker containers")
                    for i in range(5):
                        request_url = urllib.request.urlopen("https://oh9jhr9pw3.execute-api.ap-south-1.amazonaws.com/test/rmvcont")
                        print ( request_url.read() )
                 
                
            
    cv2.imshow("my photo", photo)
    if cv2.waitKey(10) == 13:
        break
        
        
cv2.destroyAllWindows()
cap.release()
