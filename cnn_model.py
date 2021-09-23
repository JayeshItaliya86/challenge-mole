import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import cv2 as cv2
import os
import shutil
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing import image
import tensorflow as tf
from tensorflow.keras import models, layers, Sequential
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, roc_auc_score, roc_curve, auc, classification_report, plot_confusion_matrix, accuracy_score, r2_score


# Get images for preprocessing / resahpe

image_size = (100,125)

def get_preprocessed_images(images_directory: str, image_size: tuple) -> list:
    images = []
    for img in os.listdir(images_directory):
        img = image.load_img(images_directory+img, target_size=image_size)
        img = image.img_to_array(img)
        img = img.reshape((1, img.shape[0], img.shape[1], img.shape[2]))
        img = preprocess_input(img)
        images.append(img)
    return np.vstack(images)

# Load your images and preprocess them.
cancer_images = get_preprocessed_images("assets/archive/cancer/", image_size)
not_cancer_images = get_preprocessed_images("assets/archive/not_cancer/", image_size)

# Make a numpy array for each of the class labels (one hot encoded).
cancer_labels = np.tile([1, 0], (cancer_images.shape[0], 1))
not_cancer_labels = np.tile([0, 1], (not_cancer_images.shape[0], 1))

# Concatenate your images and your labels into X and y.
X = np.concatenate([cancer_images, not_cancer_images])
y = np.concatenate([cancer_labels, not_cancer_labels])


# Split train/test data
train_val_img, test_img, train_val_labels, test_labels = train_test_split(X, y,test_size=0.2, random_state=42, shuffle=True)
train_img, val_img, train_labels, val_labels = train_test_split(train_val_img, train_val_labels,test_size=0.2, random_state=42, shuffle=True)


#CNN Model

# pixel width and height of our images
input_size = (100,125)
# number of filters in the convnet layer
filters = 64
# conv net parameters
strides = (2, 2)
pool_size = (2,2)
kernel_size = (5, 5)


# Create the first version of the model
model = tf.keras.Sequential()
model.add(layers.Conv2D(filters=filters, kernel_size=kernel_size, input_shape=(100,125,3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(2, activation='softmax'))
model.compile(loss=tf.keras.losses.CategoricalCrossentropy(from_logits=False), optimizer='adam', metrics=['accuracy'])
model.fit(train_img, train_labels, epochs=20, batch_size=256)
model.summary()

#Prediction and Conf Matrix
pred = model.predict('test')
matrix = tf.math.confusion_matrix(labels=tf.argmax('true_labels', 1), predictions=tf.argmax('pred', 1))

#Plot Conf Matrix

ax= plt.subplot()
sns.heatmap(matrix, annot=True, fmt='g', ax=ax)

# labels, title and ticks
ax.set_xlabel('Predicted labels');ax.set_ylabel('True labels') 
ax.set_title('Confusion Matrix') 
ax.xaxis.set_ticklabels(['not_cancer', 'cancer'])
ax.yaxis.set_ticklabels(['not_cancer', 'cancer'])
plt.show()
