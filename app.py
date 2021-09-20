import streamlit as st
from PIL import Image
from models import skin_or_else_classification, cancer_classification

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

# file upload and handling logic
uploaded_file = st.file_uploader("Upload an image of skin", type=['png', 'jpeg', 'jpg'])
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, use_column_width=True)
    st.write("")
    st.subheader("Result")

    # Load models
    label_skin = skin_or_else_classification(image)
    label_cancer = cancer_classification(image)

    # checks if image is a skin image or not (0 = Not skin, 1 = skin)
    if label_skin == 0:
        st.write("""
                This doesn't look like a valid skin image.
                \nPlease restart with a proper image.
                """)
    # if skin image
    else:
        # checks if skin image has cancer or not (0 = Cancer, 1 = No cancer). Should reverse labels?
        # No cancer
        if label_cancer == 1:
            st.write("The skin looks normal. This image depicts __HEALTHY SKIN__.")
        # Cancer
        else:
            st.write("""
            ⚠️ The skin seems to be infected by __CANCER__.
            \nLearn more about skin cancer [here](https://www.mayoclinic.org/diseases-conditions/skin-cancer/symptoms-causes/syc-20377605).
            \nFor further investigation, please contact your doctor.""")

# Cleans Streamlit layout
hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)