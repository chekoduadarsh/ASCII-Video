
from flask import Flask, render_template, request, redirect, url_for, abort, jsonify

from libs.videoreader import base64_to_numpy_image, encode_frame
import cv2

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

density_encoder_string = "Ñ@#W$9876543210?!abc;:+=-,._             "
#density_encoder_string = '       .:-i|=+%O#@'
#density_encoder_string = '█▓▒░:.        '
#density_encoder_string= "01 "

image = cv2.imread('lenna.jpeg')

@app.route('/')
def root():
    """Video streaming home page."""
    return render_template('index.html')


@app.route('/calculate_result')
def calculate_result():
  a = str(request.args.get('val1'))
  base64_img = str(request.args.get('val2')).split(",")[1]
  print(base64_to_numpy_image(base64_img))
  return jsonify({"result":encode_frame(base64_to_numpy_image(base64_img),(48,48) ,density_encoder_string)})

if __name__ == '__main__':
    app.run(host='0.0.0.0')