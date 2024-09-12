# Plant Disease Detection App

This is a CNN-based plant disease detection model deployed on Hugging Face. The app classifies plant images into 29 different categories of diseases and healthy plants. The model can identify common diseases in plants such as *Apple Scab*, *Corn Northern Leaf Blight*, *Tomato Yellow Leaf Curl Virus*, and more. The app is designed to assist users in identifying plant diseases quickly by uploading an image, which the model then analyzes to provide the top predicted disease class.

## Model Overview

- **Model Architecture**: Sequential CNN
- **Total Parameters**: 3,831,556 (14.62 MB)
- **Trainable Parameters**: 3,830,468 (14.61 MB)
- **Non-Trainable Parameters**: 1,088 (4.25 KB)
  
The model was trained on a dataset containing:
- **Training Images**: 53,693 images across 29 classes.
- **Testing Images**: 12,067 images across 29 classes.
- **Validation Images**: 1,358 images across 29 classes.

### Supported Plant Diseases
The model supports detection for the following plant diseases and healthy plants:

1. Apple Black Rot
2. Apple Cedar Rust
3. Apple Healthy
4. Apple Scab
5. Bell Pepper Bacterial Spot
6. Bell Pepper Healthy
7. Cherry Healthy
8. Cherry Powdery Mildew
9. Corn Cercospora Leaf Spot
10. Corn Common Rust
11. Corn Healthy
12. Corn Northern Leaf Blight
13. Grape Black Rot
14. Grape Esca (Black Measles)
15. Grape Healthy
16. Grape Leaf Blight
17. Peach Bacterial Spot
18. Peach Healthy
19. Potato Early Blight
20. Potato Healthy
21. Potato Late Blight
22. Strawberry Healthy
23. Strawberry Leaf Scorch
24. Tomato Bacterial Spot
25. Tomato Early Blight
26. Tomato Healthy
27. Tomato Late Blight
28. Tomato Septoria Leaf Spot
29. Tomato Yellow Leaf Curl Virus

## Features

- **Real-Time Disease Detection**: Upload an image of a plant leaf to receive a diagnosis from the model.
- **Model Accuracy**: The model is trained to provide accurate predictions across 29 different classes.
- **Top 5 Predictions**: The app displays the top 5 disease categories for each uploaded image, including probabilities for each.
- **Example Images**: Predefined example images are provided to test the app easily.

## Frontend: Gradio Interface
The frontend is powered by Gradio, offering a simple and interactive interface to upload images, view results, and test sample images.
