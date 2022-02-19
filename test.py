import pandas as pd
import numpy as np
import time
from sklearn.preprocessing import LabelEncoder
df=pd.read_csv(r"C:\Users\Shivam\Desktop\Python Codes\calc_case_description_train_set1.csv")
df=df.replace(np.nan,0)
x=LabelEncoder()
df['left or right breast']=x.fit_transform(df['left or right breast'].astype('str'))
df['image view']=x.fit_transform(df['image view'].astype('str'))
df['calc type']=x.fit_transform(df['calc type'].astype('str'))
df['calc distribution']=x.fit_transform(df['calc distribution'].astype('str'))
df['pathology']=x.fit_transform(df['pathology'].astype('str'))
print(df.head(10))
start = time.time()
print(start)
