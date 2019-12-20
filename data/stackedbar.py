# libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import csv
 
# y-axis in bold
rc('font', weight='bold')
 
# Values of each group
barsbronze1 = [167, 107, 127, 93, 221, 177, 97, 132, 103, 79, 77, 54, 76, 81, 42, 47, 10, 36, 34, 35, 24, 14, 11, 5, 12, 7, 5, 7, 7, 8, 5, 1, 5, 1, 3, 1, 3, 1, 0, 2, 1, 0, 1, 0, 0,]
barssilver2 = [319, 203, 171, 97, 147, 129, 126, 77, 98, 90, 57, 50, 80, 35, 38, 24, 26, 30, 11, 12, 22, 10, 10, 8, 4, 8, 4, 3, 4, 4, 1, 6, 2, 6, 3, 2, 2, 2, 5, 0, 1, 2, 0, 0, 1]
barsgold3 = [167, 315, 159, 250, 66, 127, 137, 76, 79, 94, 58, 58, 2, 36, 42, 23, 51, 16, 34, 28, 17, 36, 6, 8, 2, 0, 6, 5, 2, 0, 5, 4, 2, 0, 1, 4, 1, 2, 0, 0, 0, 0, 1, 1, 0,]
 
# Heights of bars1 + bars2
bars = np.add(barsbronze1, barssilver2).tolist()
 
# The position of the bars on the x-axis
r = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44]
 
# Names of group and bar width
names = ['USA', 'CAN', 'NOR', 'URS', 'FIN', 'SWE', 'GER', 'SUI', 'AUT', 'RUS', 'ITA', 'GDR', 'TCH', 'FRA', 'NED', 'FRG', 'KOR', 'CHN', 'GBR', 'CZE', 'JPN', 'EUN', 'POL', 'EUA', 'SLO', 'LAT', 'BLR', 'AUS', 'BEL', 'HUN', 'UKR', 'CRO', 'LIE', 'YUG', 'KAZ', 'EST', 'BUL', 'SVK', 'DEN', 'ROU', 'PRK', 'LUX', 'ESP', 'UZB', 'NZL']
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
plt.title("Men vs Women In Total Olympic Medals")
 
# Show graphic
plt.show()
