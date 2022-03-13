import cv2
import numpy as np
import math
from PIL import Image
from io import BytesIO
import base64

def translate(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    valueScaled = float(value - leftMin) / float(leftSpan)

    return rightMin + (valueScaled * rightSpan)



def encode_frame(frame, size, density_encoder_string =""):
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_image = cv2.resize(gray_image, size, interpolation= cv2.INTER_LINEAR)
    height = gray_image.shape[0] # keep original height
    dim = (size, height)
    frame = cv2.resize(frame, dim, interpolation= cv2.INTER_LINEAR)

    encode_str = ""
    h = gray_image.shape[0]
    w = gray_image.shape[1] 
    for y in range(0, h):
        for x in range(0, w):
            if gray_image[y, x] > 255:
                gray_image[y, x] = 255
            if gray_image[y, x] < 0:
                gray_image[y, x] = 0
            encode_str += "<p style='display:inline;color:#"+rgb_to_hex((int(frame[y, x][0]), int(frame[y, x][1]), int(frame[y, x][2])))+"'>"+density_encoder_string[math.floor(translate(gray_image[y, x], 0, 255, len(density_encoder_string)-1, 0))].replace(" ", "&nbsp;")+"</p>"
        encode_str += "</br>"
    
    print(encode_str)
    return encode_str
        

def base64_to_numpy_image(base64_img):
    return np.array(Image.open(BytesIO(base64.b64decode(base64_img))))


def pil_image_to_base64(pil_image):
    buf = BytesIO()
    pil_image.save(buf, format="JPEG")
    return base64.b64encode(buf.getvalue())

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb