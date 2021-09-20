import pandas as pd
import numpy as np

df_mole = pd.read_csv('assets/archive/HAM10000_metadata.csv')
df_mole['target'] = df_mole['dx']

cancer = ['bcc', 'mel']
not_cancer = ['akiec', 'df', 'bkl', 'nv', 'vasc']

df_mole['target'] = df_mole['target'].replace(to_replace=cancer, value=1)
df_mole['target'] = df_mole['target'].replace(to_replace=not_cancer, value=0)