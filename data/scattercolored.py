# libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import csv
 
# y-axis in bold
rc('font', weight='bold')
 
# Values of each group
barsbronze1 = [139, 157, 56, 512, 60, 404, 591]
barssilver2 = [141, 151, 58, 514, 58, 413, 595]
barsgold3 = [140,144,58,510,62,412,595]
 
# Heights of bars1 + bars2
bars = np.add(barsbronze1, barssilver2).tolist()
 
# The position of the bars on the x-axis
r = [0,1,2,3,4,5,6]
 
# Names of group and bar width
names = ['Biathlon', 'Bobsleigh', 'Curling', 'Ice Hockey', 'Luge', 'Skating', 'Skiing']
barWidth = 1
 
# Create brown bars
plt.bar(r, barsbronze1, color='#7f6d5f', edgecolor='white', label="Bronze Medals", width=barWidth)
# Create green bars (middle), on top of the firs ones
plt.bar(r, barssilver2, bottom=barsbronze1, color='#778899', edgecolor='white', label="Silver Medals", width=barWidth)
# Create green bars (top)
plt.bar(r, barsgold3, bottom=bars, color='#DAA520', edgecolor='white', label="Gold Medals", width=barWidth)
plt.legend()

# Custom X axis
plt.xticks(r, names, fontweight='bold', rotation=90)
plt.xlabel("Countries")
plt.ylabel("Total Medals")
plt.title("Total Medals For Each Country In The Winter Olympics")
 
# Show graphic
plt.show()