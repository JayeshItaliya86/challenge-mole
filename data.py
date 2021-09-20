import pandas as pd
import numpy as np
import os
import shutil
from PIL import Image, ImageOps

#Read data
df_mole = pd.read_csv('assets/archive/HAM10000_metadata.csv')
df_mole['target'] = df_mole['dx']

#Target
cancer = ['bcc', 'mel']
not_cancer = ['akiec', 'df', 'bkl', 'nv', 'vasc']

df_mole['target'] = df_mole['target'].replace(to_replace=cancer, value=1)
df_mole['target'] = df_mole['target'].replace(to_replace=not_cancer, value=0)

#Images split (0/1)
for index, row in df_mole.iterrows():
    image = row['image_id'] 
    if row['cancer'] == 0:
        shutil.move(f"HAM10000_images/{image}.jpg", f"cancer_0/{image}.jpg")
    else:
        shutil.move(f"HAM10000_images/{image}.jpg", f"cancer_1/{image}.jpg")

#Image Augmentation(greysc-flip-mirror)
PATH = "assets/archive/cancer/"
Copy_to_path="assets/archive/cancer/"

for filename in os.listdir(PATH):
    img = Image.open(os.path.join(PATH, filename)) # images are color images
    gray_img = ImageOps.grayscale(img)             # to grayscale
    gray_img.save(Copy_to_path+'gs_'+filename)
    flip_img = ImageOps.flip(img)                   # flip vertical
    flip_img.save(Copy_to_path+'fv_'+filename)
    mirror_img = ImageOps.mirror(img)                  # mirror (flip horiz)
    mirror_img.save(Copy_to_path+'fh_'+filename)


#DataFrame re-balanced
