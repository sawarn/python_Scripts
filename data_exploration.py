import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
#from numba import njit
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv(r"/home/shivam/Downloads/calc_case_description_train_set .csv")
print(len(data))
print(data.columns)

d_head = data.head(5)
d_shape = data.shape
print(d_head, d_shape)

clean = data.isna().sum()
print(clean)
data = data.dropna(axis= 1, how = 'any')

d_shape_new = data.shape
print(d_shape_new)

print(data.describe())

features_mean = list(data.columns[1:13])
print (features_mean)

print(data['pathology'].value_counts())
print(data['left or right breast'].value_counts())
print(data['image view'].value_counts())

sns.countplot(data['pathology'], label = "Count")
plt.show()
sns.countplot(data['left or right breast'], label = "Breast Portion")
plt.show()
sns.countplot(data['image view'], label = "Position")
plt.show()


print(data.dtypes)

#pathology_encoded = LabelEncoder()
#data.iloc[:,9] = pathology_encoded.fit_transform(data.iloc[:,9].values)
#print(pathology_encoded.fit_transform(data.iloc[:,1].values))

sns.pairplot(data, hue = "pathology")
plt.show()

print(data.corr())
plt.figure(figsize = (10,10))
sns.heatmap (data.corr(), annot=True, square = True, fmt='.0%')
plt.show()

color_disc = {'Malignant':'red', 'Benign':'blue'}
colors = data['pathology'].map(lambda x: color_disc.get(x))
scatter = pd.plotting.scatter_matrix(data[features_mean], c = colors, alpha= 0.4, figsize = ((15,15)))
plt.show()
