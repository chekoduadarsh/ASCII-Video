
from flask import Flask, render_template, request, redirect, url_for, abort, jsonify
import binascii
from libs.videoreader import base64_to_numpy_image, encode_frame, pil_image_to_base64
import cv2

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'


@app.route('/')
def root():
    """Video streaming home page."""
    return render_template('index.html')


@app.route('/calculate_result')
def calculate_result():
  density_encoder_string = str(request.args.get('val1'))
  base64_img = str(request.args.get('val2')).split(",")[1]
  image_size = int(request.args.get('val3'))
  ecoded_img, img =encode_frame(base64_to_numpy_image(base64_img),size=(image_size,image_size) ,density_encoder_string=density_encoder_string)
  #base_64_img = "data:image/jpeg;base64,"+str((pil_image_to_base64(img)).decode("utf-8"))
  return jsonify({"result":ecoded_img})

if __name__ == '__main__':
    app.run()