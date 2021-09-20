import pandas as pd
import numpy as np
import os
import shutil
from PIL import Image, ImageOps

df_mole = pd.read_csv('assets/archive/HAM10000_metadata.csv')
df_mole['target'] = df_mole['dx']

cancer = ['bcc', 'mel']
not_cancer = ['akiec', 'df', 'bkl', 'nv', 'vasc']

df_mole['target'] = df_mole['target'].replace(to_replace=cancer, value=1)
df_mole['target'] = df_mole['target'].replace(to_replace=not_cancer, value=0)

for index, row in df_mole.iterrows():
    image = row['image_id'] 
    if row['target'] == 0:
        shutil.move(f"assets/archive/HAM10000_images/{image}.jpg", f"assets/archive/cancer_0/{image}.jpg")
    else:
        shutil.move(f"assets/archive/HAM10000_images/{image}.jpg", f"assets/archive/cancer_1/{image}.jpg")


PATH = "assets/archive/cancer/"
Copy_to_path = "assets/archive/cancer/"

for filename in os.listdir(PATH):
    img = Image.open(os.path.join(PATH, filename))  # images are color images
    gray_img = ImageOps.grayscale(img)             # to grayscale
    gray_img.save(Copy_to_path+filename+'_gs.jpeg')
    flip_img = ImageOps.flip(img)                   # flip vertical
    flip_img.save(Copy_to_path+filename+'_fv.jpeg')
    mirror_img = ImageOps.mirror(img)                  # mirror (flip horiz)
    mirror_img.save(Copy_to_path+filename+'_fh.jpeg')
