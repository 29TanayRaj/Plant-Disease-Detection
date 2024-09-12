
# Library Dependencies 
import tensorflow as tf
from tensorflow import keras
from keras import Sequential
from keras.layers import Dense,Conv2D,MaxPooling2D,Flatten,BatchNormalization,Dropout
from keras.layers import Input, Lambda, Dense, Flatten, Activation, Dropout
from keras.preprocessing import image
import matplotlib.pyplot as plt
import numpy as np
from keras import applications
from keras.callbacks import ModelCheckpoint,EarlyStopping
from PIL import Image
from IPython.display import display
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import classification_report,confusion_matrix
import seaborn as sns 
import gradio as gr
import os

# importing the model 
model = keras.models.load_model('CNN_Model.keras')

# Function to get the predictions 
def get_image_dim(file_path):

    classes = ['Apple Black Rot','Apple Cedar Rust','Apple Healthy','Apple Scab','Bell Pepper Bacterial Spot',
              'Bell Pepper Healthy','Cherry Healthy','Cherry Powdery Mildew','Corn Cercospora Leaf Spot',
             'Corn Common Rust','Corn Healthy','Corn Northern Leaf Blight','Grape Black Rot',
             'Grape Esca (Black Measles)','Grape Healthy','Grape Leaf Blight','Peach Bacterial Spot',
             'Peach Healthy','Potato Early Blight','Potato Healthy','Potato Late Blight',
             'Strawberry Healthy','Strawberry Leaf Scorch','Tomato Bacterial Spot','Tomato Early Blight',
             'Tomato Healthy','Tomato Late Blight','Tomato Septoria Leaf Spot','Tomato Yellow Leaf Curl Virus']

    img = Image.open(file_path)

    original_label = img.filename.split('\\')[-1].split('.')[0]

    img = img.resize((256,256))
    img_array = np.array(img) / 256
    img_array = img_array.reshape(-1,256, 256, 3)

    prediction = model.predict(img_array)[0]
    prediction_prob = list(zip(classes,prediction))
    prediction_prob.sort(key=lambda x: x[1],reverse=True)

    return original_label,dict(prediction_prob[0:5])

# function to generate a gradio app interface for the project. 
interface = gr.Interface(
    fn=get_image_dim, 
    inputs=gr.Image(type="filepath", label="Upload Plant Image",
                    height=500,width=600,interactive=True), 
    outputs=[gr.Textbox(label="Original Image Label"),
             gr.Label(num_top_classes=5, label="Model Prediction")],
    title='Plant Disease Detection',
    description="Upload an image of a plant to detect diseases and get disease type.\n"
                "The Model can currently handle 29 classes.\n"
                "Users can try out the examples below."
                "Note: Original Image label only shows correct result for the examples given below",
    examples=[ ["Strawberry Leaf Scorch.jpg"],['Corn Common Rust.JPG'],['Apple Black Rot.JPG'],
              ['Peach Bacterial Spot.JPG'],['Grape Esca (Black Measles).JPG'],['Cherry Powdery Mildew.JPG'],
              ['Tomato Septoria Leaf Spot.JPG'],['Grape Leaf Blight.JPG'],['Grape Healthy.JPG']],
    allow_flagging="never",
    theme="default",
).launch(share=True)
