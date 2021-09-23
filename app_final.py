import numpy as np
import streamlit as st
from PIL import Image


from models import skin_or_else_classification, cancer_classification

# Title of the page
st.set_page_config(page_title="Skin Cancer App", layout='wide')


# Main text
st.title("Skin Cancer Identifier App")
st.write("""
This app detects whether or not skin is infected by cancer, based on an image.
\nThis app is __NOT__ meant for medical purposes!
""")

# Sidebar text
st.sidebar.title('Model information')
st.sidebar.write("""
Dataset: The [__HAM10000__](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T)
\nCNN built with Keras (Tensorflow)
\nSequential model: Conv2D, Flatten, Dense
\n1.5M trainable parameters
\nAccuracy: 0.92
\nModel and application created @Becode Gent by 
\n[Anne](https://github.com/annejungers),
[Jayesh](https://github.com/JayeshItaliya86), 
[Jose](https://github.com/Roldan87),
[Logan](https://github.com/lvendrix)
""")

# file upload and handling logic
uploaded_file = st.file_uploader("Upload an image of skin", type=['png', 'jpeg', 'jpg'])
if uploaded_file is not None:
    user_image = Image.open(uploaded_file).convert('RGB')
    st.image(user_image, use_column_width=True)
    label_skin = skin_or_else_classification(user_image)

    # checks if image is a skin image or not (0 = Not skin, 1 = skin)
    if label_skin == 0:
        st.write("""
                This doesn't look like a valid skin image.
                \nPlease restart with a proper image.
                """)

    # if skin image, checks whether skin has cancer or not (1 = Cancer, 0 = No cancer)
    else:
        cancer_prediction = cancer_classification(uploaded_file)
        prediction = np.rint(cancer_prediction)

        st.subheader("Results")
        if prediction[0][0] == 1:
            st.write('⚠️ The skin seems to be infected by __CANCER__ with an accuracy of {:.2f} %.'.format(cancer_prediction[0][0]*100))
            st.write("""
            \nLearn more about skin cancer [here](https://www.mayoclinic.org/diseases-conditions/skin-cancer/symptoms-causes/syc-20377605).
            \nFor further investigation, please contact your doctor.""")

        else:
            st.write('The skin looks normal. This image depicts __HEALTHY SKIN__ with an accuracy of {:.2f} %.'.format(cancer_prediction[0][1]*100))


# Cleans Streamlit layout
hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

