from flask import Flask, render_template, request, jsonify
from keras_preprocessing import image
from keras.models import load_model
from keras.applications.vgg16 import preprocess_input
import numpy as np
import os

app = Flask(__name__)

# Load model
model = load_model('our_model.h5')
model.make_predict_function()

# Prediction function
def predict_label(img_path):
    try:
        # Try loading and processing the image
        img = image.load_img(img_path, target_size=(224, 224))
        imagee = image.img_to_array(img)
        imagee = np.expand_dims(imagee, axis=0)
        img_data = preprocess_input(imagee)
        prediction = model.predict(img_data)

        # Return prediction results
        if prediction[0][0] > prediction[0][1]:
            return 'Person is safe.'
        else:
            return 'Person is affected by Pneumonia.'
    except Exception as e:
        # If image processing fails, return None
        return None

# Route to main page
@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template("index.html")

# Route to handle image submission
@app.route("/submit", methods=['POST'])
def get_output():
    if request.method == 'POST':
        img = request.files.get('my_image')

        if img is None or img.filename == '':
            return jsonify({'error': 'No image uploaded. Please upload an image.'})

        img_path = os.path.join("static", img.filename)
        img.save(img_path)

        p = predict_label(img_path)

        if p is None:
            return jsonify({'error': 'Invalid image. Please upload a valid image.', 'img_path': 'static/invalid_image.jpg'})

        return jsonify({'prediction': p, 'img_path': img_path})

if __name__ == '__main__':
    # app.debug = True
    app.run(debug=True, port=8000)
