# libraries
import matplotlib.pyplot as plt
import squarify    # pip install squarify (algorithm for treemap)
import csv
 
# If you have 2 lists
squarify.plot(sizes=[653,625,457,440,434,433,360,285,280,263,192,162,158,152,122,94,87,82,79,75,63,60,27,21,18,15,15,15,13,12,11,11,9,7,7,7,6,5,5,2,2,2,2,1,1], label=["USA", "CAN", "NOR", "URS", "FIN", "SWE", "GER", "SUI", "AUT", "RUS", "ITA", "GDR", "TCH", "FRA", "NED", "FRG", "KOR", "CHN", "GBR", "CZE", "JPN", "EUN", "POL", "EUA", "SLO", "LAT", "BLR", "AUS", "BEL", "HUN", "UKR", "CRO", "LIE", "YUG", "KAZ", "EST", "BUL", "SVK", "DEN", "ROU", "PRK", "LUX", "ESP", "UZB", "NZL"], alpha=.7 )
plt.axis('off')
plt.show()
