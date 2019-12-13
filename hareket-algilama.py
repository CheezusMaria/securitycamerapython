import cv2
from datetime import datetime


def farkImaj(t0,t1,t2): #comparing 3 different time
    fark1=cv2.absdiff(t2,t1) #difference between 2 photo
    fark2 = cv2.absdiff(t1, t0)
    return cv2.bitwise_and(fark1,fark2) #compare bits
esik_deger=200 #sensitivity
kamera=cv2.VideoCapture(0) #getting images from webcam

pencereIsmi="Movement Detection" #name for window
cv2.namedWindow(pencereIsmi)

t_eksi=cv2.cvtColor(kamera.read()[1],cv2.COLOR_BGR2GRAY)#image from past in gray
t=cv2.cvtColor(kamera.read()[1],cv2.COLOR_BGR2GRAY) #image from present in gray
t_arti=cv2.cvtColor(kamera.read()[1],cv2.COLOR_BGR2GRAY) #last image for understand the movement in gray

zamanKontrol=datetime.now().strftime('%Ss') #for every second max. take 1 photo

while True:
    cv2.imshow(pencereIsmi,kamera.read()[1])
    if cv2.countNonZero(farkImaj(t_eksi,t,t_arti))>esik_deger and zamanKontrol !=datetime.now().strftime('%Ss'):
        fark_resim=kamera.read()[1]
        cv2.imwrite(datetime.now().strftime('%Y%m%d_%Hh%Mm%Ss%f')+'.jpg',fark_resim)

    zamanKontrol = datetime.now().strftime('%Ss')
    t_eksi=t
    t=t_arti
    t_arti=cv2.cvtColor(kamera.read()[1],cv2.COLOR_BGR2GRAY)
    key=cv2.waitKey(10)
    if key==27:
        cv2.destroyWindow(pencereIsmi)
        break
