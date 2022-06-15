import pandas as pd 
import matplotlib as plt

df = pd.DataFrame({'Name' : ['lol1','lol2','lol3','lol4'], 'Salary' : [10000,200000,3500,650015]})
# print(df.head)

# printing statistics

# print(f"Min : {df['Salary'].min()}")
# print(f"Max : {df['Salary'].max()}")
# print(f"Mean : {df['Salary'].mean()}")
# print(f"Median : {df['Salary'].median()}")
# print(f"Mode : {df['Salary'].mode()}")

# decription
# print(df['Salary'].describe()['count'])

salary = df['Salary']
salary.plot.hist(title="salary distribution", color = 'grey', bins = 25)
plt.pyplot.axvline(salary.mean(),color='blue', linestyle = 'dashed', linewidth = 2)
plt.pyplot.axvline(salary.median(),color='red', linestyle = 'dashed', linewidth = 2)
plt.pyplot.show()