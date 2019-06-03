import numpy as np
from PIL import ImageFont, ImageDraw, Image
import cv2
import time

#encoding=cp949    


## Make canvas and set the color
img = np.zeros((1000,1000, 3),np.uint8)
b,g,r,a = 0,255,0,0

def bitOperation(hpos, vpos):
    img1 = cv2.imread('../images/back.png')
    img2 = cv2.imread('../images/predicted_test_image.png')

    rows, cols, channels = img2.shape
    roi = img1[vpos:rows+vpos, hpos:cols+hpos]

    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

    ## Use cv2.FONT_HERSHEY_XXX to write English.
    text = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()) 
    cv2.putText(img,  text, (10,530), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (b,g,r), 1, cv2.LINE_AA)
    cv2.putText(img,  "--- by 7708B", (850,150), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (b,g,r), 1, cv2.LINE_AA)
    
    dst = cv2.add(img1_bg, img2_fg)
    img[vpos:rows+vpos, hpos:cols+hpos] = dst

    #cv2.imshow('결과', img)
    cv2.waitKey(0)
    #cv2.destroyAllWindows()

    img3 = img
    ## Use simsum.ttc to write Chinese.
    fontpath = "./BMJUA.ttf"
    font = ImageFont.truetype(fontpath, 32)
    img_pil = Image.fromarray(img3)
    draw = ImageDraw.Draw(img_pil)
    draw.text((10, 550),  "마음속의 사랑은 영원히 간직해서 가져갈 \n수 있으니까 말야", font = font, fill = (b, g, r, a))
    img3 = np.array(img_pil)

    cv2.imshow("result", img3);cv2.waitKey();cv2.destroyAllWindows()

#bitOperation(10, 10)
## Display 

#cv2.imwrite("res.png", img)
