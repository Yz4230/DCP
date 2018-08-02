import cv2
import numpy as np

def cnbin(filename):
    base_img = cv2.imread(filename)
    ps_img = cv2.imread(f'{filename[:-4]}_e.{filename[-4:]}')
    img_height, img_width, img_cnl = base_img.shape
    f_img_height = img_height * 2

    cnb_img = np.zeros((f_img_height, img_width, img_cnl), 'uint8')
    cnb_img[0:img_height, 0:img_width] = base_img
    cnb_img[img_height:f_img_height, 0:img_width] = ps_img
    cv2.imwrite('c.png', cnb_img)


cnbin('0.png')
