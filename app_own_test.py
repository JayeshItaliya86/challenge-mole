import streamlit as st
from models_own import skin_or_else_classification, cancer_classification, get_preprocessed_images
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


def get_preprocessed_images(image_name, image_size: tuple) -> list:
    img = image.load_img(image_name, target_size=image_size)
    img = image.img_to_array(img)
    img = img.reshape((1, img.shape[0], img.shape[1], img.shape[2]))
    img = preprocess_input(img)
    return img

# file upload and handling logic
uploaded_file = st.file_uploader("Upload an image of skin", type=['png', 'jpeg', 'jpg'])
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, use_column_width=True)
    #with open(os.path.join("cancer_user", uploaded_file.name), "wb") as f:
    #    f.write(uploaded_file.getbuffer())
    #st.success("Saved File")
    #time.sleep(20)
    processed_image = get_preprocessed_images(uploaded_file, (100,125))
    #model = keras.models.load_model('models/base_model_v2.h5', compile=False)
    #model.predict(processed_image)
    st.write("")
    st.subheader("Result")
    st.write('this is image')




    # resize the image to a 224x224 with the same strategy as in TM2:
    # resizing the image to be at least 224x224 and then cropping from the center
    # newsize = (100, 125)
    # image = image.resize(newsize)
    # image_sequence = image.getdata()
    # image_array = np.array(image_sequence)
    #img = image_array.reshape( image_array.shape[0], image_array.shape[1], image_array.shape[2])
    #img = preprocess_input(image_array)
else:
    processes_image = get_preprocessed_images('cancer_1_sample/flip_horizontal_ISIC_0024315.jpg', (100,125))
    st.write(processes_image)
    st.write(processes_image.shape)
    #st.write(img)
    #st.write(img.shape)





