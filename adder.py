import cv2
import numpy as np

def read_text(filename):
    file = open(filename, 'r')
    string = file.read()
    return string

def cnglist(ar1, ar2):
    """二つのリストを比較する。
    ar1:一つ目のリスト
    ar2:二つ目のリスト
    ar1[x]==254, 255 の時に、
    ar2[x]=256-arr[x] とする。
    """
    count = len(ar2)
    for index in range(count):
        if ar1[index] in (254, 255):
            ar2[index] = 256 - ar2[index]
    #LOG.write(str(ar1))
    #LOG.write('\n')
    ar1 = np.array(ar1)

    return ar1, ar2

def val2bin(val):
    re_list = []
    for i, fig in enumerate(val):
        re_list.insert(i, ord(fig))

    re_val = ''
    for j in re_list:
        re_val += str(bin(j)).replace('0b', 'b')

    re_val += '3'

    # print(f'\'{val}\' has changed into \'{re_val}\'.')
    # print(f'The range is {len(re_val)}.')

    return re_val

def bin2img(adding_text, photo_name):
    adding_img = cv2.imread(photo_name)
    heiht, width, channel = adding_img.shape

    tg_bin = val2bin(adding_text).replace('b', '2')
    tg_bin_list = list(tg_bin)
    tg_bin_list = [int(i) for i in tg_bin_list]

    adding_img, tg_bin_list = cnglist(adding_img.flatten().tolist(), tg_bin_list)

    adding_img_fn = np.array(adding_img, dtype='uint8')
    tg_bin_ar = np.array(tg_bin_list, dtype='uint8')
    print(f'{len(tg_bin)}文字を差し込みます')

    print(f'{adding_img_fn}=>{adding_img_fn.shape[0]}: type=>{adding_img_fn.dtype}')
    print(f'{tg_bin_ar}=>{tg_bin_ar.shape[0]}: type=>{tg_bin_ar.dtype}')

    len_tba = tg_bin_ar.shape[0]
    sl_aif = adding_img_fn[:len_tba]

    sl_aif += tg_bin_ar

    print(f'{sl_aif}=>{sl_aif.shape[0]}要素')
    print(f'{adding_img_fn}=>{adding_img_fn.shape[0]}要素')

    adding_img = np.array(np.reshape(adding_img_fn, (heiht, width, channel)), dtype='uint8')

    # print(f'adding_img => {adding_img}')

    return adding_img

ADDING_TEXT = read_text('data.txt')
FILENAME = '0.png'

BASE_IMG = cv2.imread(FILENAME)
PS_IMG = bin2img(ADDING_TEXT, FILENAME)

cv2.imwrite(f'{FILENAME[:-4]}_e.{FILENAME[-4:]}', PS_IMG)
