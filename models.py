import numpy as np
from PIL import Image, ImageOps
import os
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow import keras


# Skin image Identifier (1 = Skin, 0 = Not skin)
def skin_or_else_classification(img):
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = keras.models.load_model('models/keras_model_skin_or_else.h5', compile=False)

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = img

    # resize the image to a 224x224 with the same strategy as in TM2:
    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    # turn the image into a numpy array
    image_array = np.asarray(image)

    # display the resized image
    image.show()

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    return np.argmax(prediction)


# Cancer Identifier (1 = Cancer, 0 = Not cancer)
def cancer_classification(uploaded_file):
    with open(os.path.join("cancer_user", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
        user_folder = 'cancer_user/'
        for img in os.listdir(user_folder):
            if img.endswith(('.jpeg', '.jpg', '.png', '.jfif')):
                img = tf.keras.preprocessing.image.load_img(user_folder+img, target_size=(100,125))
                img = image.img_to_array(img)
                img = img.reshape((1, img.shape[0], img.shape[1], img.shape[2]))
                img = preprocess_input(img)
                model = keras.models.load_model('models/base_model_v4.h5', compile=False)
                prediction = model.predict(img)
        f.close()
        for img in os.listdir(user_folder):
            if img.endswith(('.jpeg', '.jpg', '.png', '.jfif')):
                os.remove(user_folder + img)
    return prediction
