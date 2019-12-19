# libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
 
# Data
df=pd.DataFrame({'x': range(1,11), 'y1': np.random.randn(10), 'y2': np.random.randn(10)+range(1,11), 'y3': np.random.randn(10)+range(11,21) })
 
# multiple line plot
plt.plot( '1', '1', data=df, marker='o', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4)
plt.plot( '2', '2', data=df, marker='', color='olive', linewidth=2)
plt.plot( '3', '3', data=df, marker='', color='olive', linewidth=2, linestyle='dashed', label="toto")
plt.legend()
plt.show()