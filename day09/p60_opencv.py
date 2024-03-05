# file: p60_opencv.py
# desc: OpenCV 이미지 처리 계속

import cv2

image = cv2.imread('./day09/dinga.jpg',cv2.IMREAD_UNCHANGED)
dst = cv2.flip(image, 1)    # 0 위아래 반전, 1 좌우반전

height, width, channel = image.shape
maxrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 4)    # 세번째 옵션, scale -1 = CW(시계방향), 1 = CCW(반시계방향), 2이상(배율)
thrd = cv2.warpAffine(image, maxrix, (width, height))

reverse = cv2.bitwise_not(image)    # 역상, 반전색
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # 그레이스케일
ret, bny = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY) # 이진화(0 또는 1)

cv2.imshow('dinga dinga ding~', image)
cv2.imshow('Flip', dst)
# cv2.imshow('Rotation', thrd)
cv2.imshow('ding ding', reverse)
cv2.imshow('Gray', gray)
cv2.imshow('Binary', bny)

cv2.waitKey(0)
cv2.destroyAllWindows()