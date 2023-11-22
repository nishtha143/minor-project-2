# -*- coding: utf-8 -*-
"""Minor_Project_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1L7tbyT4INxcTnBXstu05EGWHid-LZ_DO

**IMPORT LIBRARIES**
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler


# %matplotlib inline

"""**LOAD** **DATASET**"""

model = pd.read_csv('/content/test.csv')

"""**PRINT FIRST 5 ROWS OF DATASET**"""

model.head()

"""**SUMMARIZE THE NUMERICAL DATA IN OUR DATASET**"""

model.describe()

"""**GIVE INFORMATION OF DATASET**"""

model.info()

"""**GIVES NUMBER OF ROWS AND COLUMNS**"""

model.shape

"""**HISTOGRAM OF THE BHK_NO.**"""

sns.histplot(model['BHK_NO.'])
plt.xlim(0, 5)
plt.ylim(0, 31000)
plt.show()

"""**HEATMAP OF THE CORRELATION MATRIX OF THE DATAFRAME**


"""

plt.figure(figsize=(12, 6))
sns.heatmap(model.corr(),
            cmap = 'BrBG',
            fmt = '.2f',
            linewidths = 2,
            annot = True)

"""**MODEL ANALYSIS BETWEEN DIFFERENT ATTRIBUTES**

"""

import pandas as pd

model_analysis = model[(model['BHK_NO.'] > 5) & (model["SQUARE_FT"] > 5000) & (model['POSTED_BY']=='Owner')]

print(model_analysis)
model_analysis.count()

target_word = 'Delhi'
model_state= model[model['ADDRESS'].str.contains(target_word, case=False)]

print(model_state)
model_state.count()

import pandas as pd
target_word = 'Delhi'
model_state= model[model['ADDRESS'].str.contains(target_word, case=False)]

model_analysis = model[(model['BHK_NO.'] > 1) & (model["SQUARE_FT"] > 500) & (model['POSTED_BY']=='Owner') & (model['ADDRESS'].str.contains('Delhi', case=False))]

print(model_analysis )
model_analysis.count()