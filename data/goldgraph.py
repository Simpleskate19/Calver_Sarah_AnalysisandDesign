# libraries
import matplotlib.pyplot as plt
import numpy as np
import csv

# Total medal trends - sampled years (20 year increments)
# 1924, 1948, 1968, 1984, 2006, 2014
# columns 0 (year) and column 4 (country)
# 
m_1924 = 36
m_1948 = 41
m_1968 = 51
m_1984 = 56
m_2006 = 99
m_2014 = 113
w_1924 = 2
w_1948 = 5
w_1968 = 15
w_1984 = 18
w_2006 = 77
w_2014 = 93

categories = []

with open('OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)

	line_count = 0
 
# create data
values=np.cumsum(np.random.randn(1000,1))
 
# use the plot functi# output a chart here! a line chart would probably be best
womenCounts = [w_1924, w_1948, w_1968, w_1984, w_2006, w_2014]
menCounts = [m_1924, m_1948, m_1968, m_1984, m_2006, m_2014]
years = [1924, 1948, 1968, 1984, 2006, 2014]

plt.plot(years, womenCounts, color="blue", linewidth=4.0, label="Women Medals")
plt.plot(years, menCounts, color="red", linewidth=6.0, linestyle="dashed", label="Men Medals")
plt.legend()
plt.xlabel("Olmypic Year")
plt.ylabel("Total Medals")
plt.title("Men vs Women In Total Olympic Medals")
plt.show()