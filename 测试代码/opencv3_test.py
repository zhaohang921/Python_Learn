# -*- coding:utf-8 -*-
import cv2

imgpath='D:/data/zhan.jpg'
img=cv2.imread(imgpath,cv2.IMREAD_COLOR)
cv2.namedWindow('zhan',cv2.WINDOW_AUTOSIZE)
cv2.imshow("zhan",img)
k=cv2.waitKey(0)

if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite('D:/data/zhan_1.jpg',img)
    cv2.destroyAllWindows()

