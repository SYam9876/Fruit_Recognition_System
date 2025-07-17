from flask import Flask, render_template, request, url_for
import tensorflow as tf
import numpy as np
import os
from PIL import Image

app = Flask(__name__)

# Ensure 'static/uploads' directory exists
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load the trained model
model = tf.keras.models.load_model("multiple.h5")

# Define class labels (update according to your dataset)
class_labels = ["Apple", "banana", "guava", "mango","orange", "papaya", "pineapple", "waterapple", "watermelon"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    uploaded_files = request.files.getlist("images")  # Get multiple files
    predictions = []

    for file in uploaded_files:
        if file:
            # Save image to 'static/uploads' directory
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            # Process image
            img = Image.open(file).resize((224, 224))  # Adjust size based on your model
            img = np.array(img) / 255.0  # Normalize
            img = np.expand_dims(img, axis=0)  # Add batch dimension

            # Predict
            pred = model.predict(img)
            predicted_class = class_labels[np.argmax(pred)]
            confidence = round(100 * np.max(pred), 2)

            predictions.append((file.filename, predicted_class, confidence))

    return render_template("result.html", predictions=predictions)

if __name__ == "__main__":
    app.run(debug=True)
