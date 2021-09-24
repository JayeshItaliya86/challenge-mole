# Import libraries
import pandas as pd
import numpy as np
import os
import shutil
from PIL import Image, ImageOps

# To read the dataset
df_mole = pd.read_csv('assets/archive/HAM10000_metadata.csv')
df_mole['target'] = df_mole['dx']

# To set the target
cancer = ['bcc', 'mel']
not_cancer = ['akiec', 'df', 'bkl', 'nv', 'vasc']

df_mole['target'] = df_mole['target'].replace(to_replace=cancer, value='cancer')
df_mole['target'] = df_mole['target'].replace(to_replace=not_cancer, value='not_cancer')

# To create an empty folder as per target values and copy the images from main folder to classification folder of target
def spliting_fill_img(df_in: pd.DataFrame, img_folder: str):

    list_imgs = list(df_in['image_id'])
    folder = os.listdir(img_folder)
    
    # To create an empty folder as per target values
    for i in range(len(df_in.target.unique())):
        path1 = os.path.join('./assets/archive/', df_in.target.unique()[i])
        if not os.path.isdir(path1):
            os.mkdir(path1) 

    df_in = df_in.set_index('image_id')
    for image in list_imgs:
        fname = image + '.jpg'
        label = df_in.loc[image,'target']

        if fname in folder:
            # source path to image
            src = os.path.join(img_folder, fname)
            # destination path to image
            dst = os.path.join('./assets/archive/', label, fname)
            # copy the image from the source to the destination
            shutil.copyfile(src, dst)

spliting_fill_img(df_mole, 'assets/archive/HAM10000_images_part_1')
spliting_fill_img(df_mole, 'assets/archive/HAM10000_images_part_2')

# To define the path
PATH = "assets/archive/cancer/"
Copy_to_path = "assets/archive/cancer/"

# Image Augmentation(flip-mirror-rotate)
for filename in os.listdir(PATH):
    img = Image.open(os.path.join(PATH, filename))    # images are color images
    flip_img = ImageOps.flip(img)                     # flip the images vertical
    flip_img.save(Copy_to_path+'fv_'+filename)
    mirror_img = ImageOps.mirror(img)                 # mirror the images (flip horizontal)
    mirror_img.save(Copy_to_path+'fh_'+filename)
    rotate_img = img.rotate(45, expand=True)           # rotate the images (45 degree)
    rotate_img.save(Copy_to_path+'rt_'+filename)                
