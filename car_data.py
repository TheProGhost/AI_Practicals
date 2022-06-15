import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

dataset = pd.read_csv("car_ad.csv", encoding ="iso-8859-9")

# Droping the drive values having NaN 
dataset = dataset.dropna(subset=['drive'])

dataset.head()



# Taking care of missing data
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(dataset[['engV']])
dataset[['engV']] = imputer.transform(dataset[['engV']])


imputer = SimpleImputer(missing_values=0, strategy='mean')
imputer.fit(dataset[['mileage']])
dataset[['mileage']] = imputer.transform(dataset[['mileage']]) 
print(dataset)
imputer.fit(dataset[['price']])
dataset[['price']] = imputer.transform(dataset[['price']])
print(dataset[['price']])

print(dataset.describe(include='all'))

# Encoding categorial data

from sklearn.preprocessing import LabelEncoder
LE_dataset = LabelEncoder()
dataset['car']= LE_dataset.fit_transform(dataset['car'])
dataset['body']= LE_dataset.fit_transform(dataset['body'])
dataset['engType']= LE_dataset.fit_transform(dataset['engType'])
dataset['registration']= LE_dataset.fit_transform(dataset['registration'])
dataset['registration']= LE_dataset.fit_transform(dataset['registration'])
dataset['drive']= LE_dataset.fit_transform(dataset['drive'])
print(dataset)


from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
dataset = np.array(ct.fit_transform(dataset))
print(dataset)


# Getting values in variables
x = dataset[['car','body','mileage','engV','engType','registration','year','model','drive']]
print(x)

y = dataset[['price']]
print(y)