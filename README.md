# Skin mole detection application

# Description  
The health company **"skinCare"** wants to create a simple web page where the user could upload a picture of the mole and see the result.  

<img src="visuals/skin_cover.jpg" alt="wine" width="1024"/>

# Installation

## Python version
* Python 3.7


## Packages used
* pandas==1.3.3
* Pillow==8.3.2
* streamlit==0.88.0
* tensorflow-gpu==2.5.0
* keras
* cv2
* sklearn.metrics

# Usage 
| File | Description |
|:---|:---|
|app.py|used for streamlit application|
|skin_cancer_model.py|used for streamlit backend function file|
|models/base_model_v5.h5|saved cnn model|
|models/keras_model_skin_or_else|saved model for streamlit application|

# Data Source
Dataset: The [__HAM10000__](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T)

# Data Visualization


<img src="visuals/lesions_plot.png" alt="wine" width="1024"/>

**nv** - Melanocytic nevi</br>
**mel** - Melanoma</br>
**bkl** - Benign keratosis-like lesions</br>
**bcc** - Basal cell carcinoma</br>
**akiec** - Actinic keratoses and intraepithelial carcinoma</br>
**vasc** - Vascular lesions</br>
**df** - Dermatofibroma</br>

<img src="visuals/classes_plot.png" alt="wine" width="1024"/>

<img src="visuals/resampled_classes_plot.png" alt="wine" width="1024"/>

**0** - Not Cancer</br>
**1** - Cancer
# Model Performance
## Model Arquitecture

<img src="visuals/model_sum.png" alt="wine" width="1024"/>

# Model History
<img src="visuals/history_plot.png" alt="wine" width="1024"/>
# Model Evaluation
<img src="visuals/matrix_model_v2_05.png" alt="wine" width="1024"/>

# Website
https://skin-cancer-application.herokuapp.com/

# Contributors
|Name|Github|
|:---|:---|
| Anne Jungers|https://github.com/annejungers|
|Jayesh Italiya|https://github.com/JayeshItaliya86|
|Jose Roldan|https://github.com/Roldan87|
|Logan Vendrix|https://github.com/lvendrix|

# Timeline
20/09/2021-24/09/2021

