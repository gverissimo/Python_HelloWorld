# output Python and platform info
import sys; print('Python %s on %s' % (sys.version, sys.platform))

# ________________________________
# do the "hello world thing
print(); print()
print("Hello world!")



# ________________________________
# very simple use of variables (and use of debugger)
print(); print()
length=2.0
width=1.1
area=length*width
print("The area of length =", length, "and width =", width, "is:", area)


# Sample using matplotlib from:
# https://www.machinelearningplus.com/plots/matplotlib-tutorial-complete-guide-python-plot-examples/
# Scatterplot with varying size and color of points
import matplotlib.pyplot as plt
import pandas as pd

# use panda to download .csv dataset from web into "midwest" frame
midwest = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/midwest_filter.csv")

# Plot
fig = plt.figure(figsize=(14, 7), dpi= 80, facecolor='w', edgecolor='k')
plt.scatter('area', 'poptotal', data=midwest, s='dot_size', c='popdensity', cmap='Reds', edgecolors='black', linewidths=.5)
plt.title("Bubble Plot of PopTotal vs Area\n(color: 'popdensity' & size: 'dot_size' - both are numeric columns in midwest)", fontsize=16)
plt.xlabel('Area', fontsize=18)
plt.ylabel('Poptotal', fontsize=18)
plt.colorbar()
plt.show()

# push a one line change from personal laptop