# 🩺 Pneumonia Detection Web App

This project is a deep learning-powered web application that detects pneumonia from chest X-ray images. It leverages a pre-trained VGG16 model with transfer learning and is deployed using Flask and Docker.

## 🌐 Live Demo

Hosted on **Render**: [Visit Live App](https://pneumoscan-qcum.onrender.com/)

## 📂 Project Structure

```
├── app.py                  # Flask backend
├── pneumonia.py           # Model training script (VGG16 + Transfer Learning)
├── our_model.h5           # Trained Keras model
├── templates/
│   └── index.html         # Frontend UI
├── static/                # Uploaded images and static files
├── Dockerfile             # Docker configuration
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## ⚙️ How It Works

1. User uploads a chest X-ray image.
2. Image is preprocessed using VGG16-style input.
3. The model predicts whether the person is infected with pneumonia or safe.
4. Prediction is displayed in the browser.

## 🧠 Model Details

- Base Model: **VGG16** (pretrained on ImageNet)
- Custom layers: Flatten + Dense (Softmax for binary classification)
- Dataset: Kaggle Chest X-ray Pneumonia dataset
- Data Augmentation: Zoom, shear, horizontal flip, rescaling
- Training Epochs: 5 (can be increased for better accuracy)

## 🤖 AI Tools & Frameworks Used

| Tool/Library        | Purpose                                      |
|---------------------|----------------------------------------------|
| **TensorFlow / Keras** | Model creation, training, and inference     |
| **VGG16 (pretrained)** | Transfer learning backbone                   |
| **ImageDataGenerator** | Real-time data augmentation                 |
| **Matplotlib**         | Plotting training/validation performance    |
| **NumPy**              | Numerical image array handling              |
| **Keras Preprocessing**| Image loading and formatting                |

## 🐳 Deployment

### Using Docker

```bash
# Build image
docker build -t pneumonia-app .

# Run container
docker run -p 8000:8000 pneumonia-app
```

### Using Render

- Create a new Web Service
- Use the Docker deployment method
- Expose port `8000`
- Use `web: gunicorn app:app` in the `render.yaml` or start command

## 📸 Sample UI

User-friendly interface to upload images and view results.

## 🧪 To Train Your Own Model

```bash
python pneumonia.py
```

## 🧑‍💻 Author

Made with ❤️ by Amritansh Raizada

---
*Last updated: July 20, 2025*
