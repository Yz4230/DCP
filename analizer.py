import cv2
import numpy as np

def bin2hex(dbin):
    """
    2進数を16進数に変換します。
    """
    #print(dbin)
    dhex = hex(int(dbin, 2))
    return dhex

def hex2str(dhex):
    """
    16進数をasciiコードとして文字に変換します。
    """
    doct = int(dhex[2:], 16)
    dascii = chr(doct)
    return dascii

def list2str(lst):
    string = ''.join(lst)
    return string

TRG_IMG = cv2.imread('c.png')

HEIGHT, WIDTH = TRG_IMG.shape[:2]

BEFORE = TRG_IMG[0:int(HEIGHT/2), 0:int(WIDTH)]
AFTER = TRG_IMG[int(HEIGHT/2):int(HEIGHT), 0:int(WIDTH)]

BEFORE = np.array(BEFORE, 'int8').flatten()
AFTER = np.array(AFTER, 'int8').flatten()

BIN_CODE = AFTER - BEFORE
INDEX = np.where((BIN_CODE == 3) | (BIN_CODE == -3))
print(f'index => {INDEX[0][0]}')
print(f'count => {BIN_CODE.shape[0]}')

BIN_CODE = BIN_CODE[:INDEX[0][0]]
BIN_CODE_INDEX = np.where((BIN_CODE == 2) | (BIN_CODE == -2))[0].tolist()

REAL_BINCODE = []
for index, val in enumerate(BIN_CODE_INDEX):
    try:
        value = BIN_CODE[val:BIN_CODE_INDEX[index+1]].tolist()
        value = [1 if i == -1 else i for i in value]
        value = [str(i) for i in value]
        REAL_BINCODE.append(value[1:])
        # print(f'{value}:st{val}:en{BIN_CODE_INDEX[index+1]}:shape{value.shape[0]}')
    except IndexError:
        value = BIN_CODE[val:].tolist()
        value = [-i if i < 0 else i for i in value]
        value = [str(i) for i in value]
        REAL_BINCODE.append(value[1:])
        # print(f'{value}:st{val}:en{BIN_CODE.shape[0]}:shape{value.shape[0]}')


for index, val in enumerate(REAL_BINCODE):
    REAL_BINCODE[index] = list2str(val)

REAL_HEXCODE = []
for i in REAL_BINCODE:
    REAL_HEXCODE.append(bin2hex(i))

SECRET_TEXT = ''
for i in REAL_HEXCODE:
    SECRET_TEXT += hex2str(i)

TEXT = open('text.txt', 'w')
TEXT.write(SECRET_TEXT)

# BIN_CODE = BIN_CODE.tolist()
# BIN_CODE = [str(-i) if i < 0 else str(i) for i in BIN_CODE]
# BIN_CODE_INDEX = BIN_CODE.index('2', 1)
# BIN_CODE = np.array(BIN_CODE, 'uint8')
# BIN_CODE = hex(BIN_CODE)
# print(f'{BIN_CODE_INDEX}:{BIN_CODE_INDEX.}')
