import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('iris.csv')
# print(df.head(50))

sepal_length = df['sepal.length']
sepal_width = df['sepal.width']
petal_length = df['petal.length']
petal_width = df['petal.width']
print(df.describe())


# plotting

sepal_length.plot.hist(title="distribution", color = 'darkgrey', bins = 25)
plt.axvline(sepal_length.mean(),color='blue', linestyle = 'dashed', linewidth = 2)
plt.axvline(sepal_length.median(),color='red', linestyle = 'dashed', linewidth = 2)

sepal_width.plot.hist(title="distribution", color = 'brown', bins = 25)
plt.axvline(sepal_width.mean(),color='blue', linestyle = 'dashed', linewidth = 2)
plt.axvline(sepal_width.median(),color='red', linestyle = 'dashed', linewidth = 2)

petal_length.plot.hist(title="distribution", color = 'orange', bins = 25)
plt.axvline(petal_length.mean(),color='blue', linestyle = 'dashed', linewidth = 2)
plt.axvline(petal_length.median(),color='red', linestyle = 'dashed', linewidth = 2)

petal_width.plot.hist(title="distribution", color = 'green', bins = 25)
plt.axvline(petal_width.mean(),color='blue', linestyle = 'dashed', linewidth = 2)
plt.axvline(petal_width.median(),color='red', linestyle = 'dashed', linewidth = 2)

plt.show()