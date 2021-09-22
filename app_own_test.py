import streamlit as st
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from PIL import Image, ImageOps
from tensorflow.keras.preprocessing import image
import numpy as np
import os
import time

# Title of the page
st.set_page_config(page_title="Skin Cancer App")

# Title and introduction
st.title("Skin Cancer Identifier App")
st.write("""
This app detects whether or not skin is infected by cancer, based on an image.
\n Model and application created by 
[Anne](https://github.com/annejungers),
[Jayesh](https://github.com/JayeshItaliya86), 
[Jose](https://github.com/Roldan87)
and [Logan](https://github.com/lvendrix)
@Becode Gent.
\nThis app is __NOT__ meant for medical purposes!
""")


image_size = (100,125)

# file upload and handling logic
uploaded_file = st.file_uploader("Upload an image of skin", type=['png', 'jpeg', 'jpg'])
if uploaded_file is not None:
    user_image = Image.open(uploaded_file).convert('RGB')
    st.image(user_image, use_column_width=True)
    with open(os.path.join("cancer_user", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
        st.success("Saved File")
        time.sleep(2)
        user_folder = 'cancer_user/'
        for img in os.listdir(user_folder):
            img = tf.keras.preprocessing.image.load_img(user_folder+img, target_size=(100,125))
            img = image.img_to_array(img)
            img = img.reshape((1, img.shape[0], img.shape[1], img.shape[2]))
            img = preprocess_input(img)
            model = keras.models.load_model('base_model_v4.h5', compile=False)
            pred = model.predict(img)
            prediction = np.rint(pred)
            #st.write(pred)
            st.subheader("Dx")
            if prediction[0][0] == 1:
                st.write('Cancer with {:.2f} % accuracy'.format(pred[0][0]*100))
            else:
                st.write('Not Cancer with {:.2f} % accuracy'.format(pred[0][1]*100))
            time.sleep(5)
            f.close()
            for img in os.listdir(user_folder):
                os.remove(user_folder+img)
else:
    st.write('File Not Valid. Please Upload a Mole Picture with format: *.PNG / *.JPEG / *.JPG')




