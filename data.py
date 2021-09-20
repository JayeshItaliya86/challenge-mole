import pandas as pd
import numpy as np
import os
import shutil

df_mole = pd.read_csv('assets/archive/HAM10000_metadata.csv')
df_mole['target'] = df_mole['dx']

cancer = ['bcc', 'mel']
not_cancer = ['akiec', 'df', 'bkl', 'nv', 'vasc']

df_mole['target'] = df_mole['target'].replace(to_replace=cancer, value=1)
df_mole['target'] = df_mole['target'].replace(to_replace=not_cancer, value=0)

for index, row in df_mole.iterrows():
    image = row['image_id'] 
    if row['cancer'] == 0:
        shutil.move(f"HAM10000_images/{image}.jpg", f"cancer_0/{image}.jpg")
    else:
        shutil.move(f"HAM10000_images/{image}.jpg", f"cancer_1/{image}.jpg")