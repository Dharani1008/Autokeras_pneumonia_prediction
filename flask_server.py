import flask
import os
import numpy as np
import random
import uuid
import tensorflow as tf
from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
from PIL import Image
from tensorflow.keras.models import load_model
from keras.preprocessing import image
import autokeras as ak
import io
import json

app = flask.Flask(__name__)

PATH = './model_autokeras_chest_xray.h5'
model = load_model(PATH)
model

def prepare_image(image, target):
    # if the image mode is not RGB, convert it
    if image.mode != "RGB":
        image = image.convert("RGB")

    # resize the input image and preprocess it
    image = image.resize(target)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    #image = imagenet_utilspreprocess_input(image)

    # return the processed image
    return image

def get_predictions():
    

    data = {"success": False}
    task_id = str(uuid.uuid4())
    data ["id"] = task_id
    
    try:
        #file = flask.request.files['image']
        #pil_img = Image.open(file.stream)
        image = flask.request.files["image"].read()
        image = Image.open(io.BytesIO(image))
        image = prepare_image(image, target=(128, 128))
        preds = model.predict(image).tolist()
        #results = imagenet_utils.decode_predictions(preds)
        print(preds)    
        data["predictions"] = preds
        
        data["success"] = True
    except ValueError as e:
        print('ValueError')
        data['Error'] = str(e)
    except Exception as e:
        print('Exception')
        print(e)
        data['Error'] = str(e) 
        
    if "Error" in data.keys():
        print("{} {}".format(task_id, data['Error']))
    response = flask.jsonify(data)
    return response

@app.route("/api/v0", methods=["POST"])
def process_api():
    """
    cURL usage
    curl -F "image=@0_L_CC.png" {ipaddress}:5012/api/v0
    """
    return get_predictions()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5012)
