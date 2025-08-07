# Fruit Recognition System

A web-based deep learning project that identifies 9 different fruits using a Convolutional Neural Network (CNN) model built with TensorFlow and deployed via a Flask web application.

## Project Overview

This project is designed to recognize and classify fruit images uploaded by users through a web interface. It leverages MobileNetV2, a lightweight and efficient CNN, to ensure high accuracy and performance. The system is suitable for use cases in agriculture, food processing, inventory management, and smart kitchens.

---

## Objectives

- Create a user-friendly web interface for image uploading.
- Preprocess images to ensure consistency in model inputs.
- Train a CNN (MobileNetV2) on a 9-class fruit dataset.
- Integrate the trained model with a Flask-based web app.
- Display fruit predictions and confidence scores to the user.

---

## Model Details

- **Architecture**: MobileNetV2 (100 layers frozen)
- **Optimizer**: Adam
- **Loss Function**: Categorical Crossentropy
- **Training Strategy**:
  - Data Augmentation: rotation, zoom, flip, shift
  - EarlyStopping and ReduceLROnPlateau callbacks
- **Accuracy Achieved**: ~98%

---

## Fruits Recognized

- Apple
- Banana
- Guava
- Mango
- Orange
- Papaya
- Pineapple
- Water Apple
- Watermelon

---

## Tools & Technologies

| Tool       | Purpose                           |
|------------|-----------------------------------|
| **Kaggle** | Dataset sourcing & exploration    |
| **Google Colab** | Model training using GPU      |
| **VS Code** | Web development & integration     |
| **TensorFlow** | Model building & training       |
| **Flask**   | Backend web framework            |
| **HTML/CSS** | Frontend design for webpages     |

---

## Results

- **Confusion Matrix** and **classification report** used for performance evaluation
- Excellent prediction accuracy on unseen test data
- Real-time fruit classification with user-uploaded images
