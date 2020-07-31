import pandas as pd 
import numpy as np
import tensorflow 
import tensorflow.keras.backend as K 
from tensorflow import keras 
from PIL import Image
import streamlit as st

class FixedDropout(tensorflow.keras.layers.Dropout):
    def _get_noise_shape(self, inputs):
        if self.noise_shape is None:
            return self.noise_shape
        symbolic_shape = K.shape(inputs)
        noise_shape = [symbolic_shape[axis] if shape is None else shape
        for axis, shape in enumerate(self.noise_shape)]
        return tuple(noise_shape)


model = tensorflow.keras.models.load_model("effnet.h5", compile=False, custom_objects={"FixedDropout":FixedDropout})

st.title("Predicting Rock-Paper-Scissors")

st.subheader("Predicting uploaded images")

up = st.file_uploader("Choose your image", type='png')


if up:
    img = Image.open(up).convert('RGB')
    st.image(img)


labels = {0:"This is a rock",1:"This is a paper",2:"This is a scissor"}

if st.button('predict'):
    img = img.resize((32,32))
    X = np.asarray(img)
    X = X.astype('float32')
    X /= 255
    X = np.expand_dims(X, axis=0)
    prediction = model.predict(X)
    cls_number = np.argmax(prediction)
    st.write(labels[cls_number])
