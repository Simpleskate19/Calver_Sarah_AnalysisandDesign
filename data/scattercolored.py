# library & dataset
import csv
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
df = sns.load_dataset('iris')
 
# Use the 'hue' argument to provide a factor variable
sns.lmplot( x="sepal_length", y="sepal_width", data=df, fit_reg=False, hue='species', legend=False)
 
# Move the legend to an empty part of the plot
plt.legend(loc='lower right')
 
plt.show()
