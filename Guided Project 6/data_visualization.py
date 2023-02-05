import matplotlib.pyplot as plt
import pandas as pd

x = [0, 2, 4, 6, 8, 10, 12, 14, 16]
y = [0, 4, 16, 36, 64, 100, 144, 196, 256]

'''plt.plot(x, y)
plt.title("Example data-Line plot")
plt.show()'''

'''plt.scatter(x, y)
plt.title("Example data- scatter plot")
plt.show()'''

plt.bar(x, y)
plt.title("Example data- bar chart")
plt.show()

fig = plt.figure(figsize=(15, 8))
first_plot = fig.add_subplot(1, 3, 1)
first_plot.plot(x, y, color="red")
first_plot.set_title("example data-Line plot")

second_plot = fig.add_subplot(1, 3, 2)
second_plot.scatter(x, y, color="green")
second_plot.set_title("example data-scatter plot")

third_plot = fig.add_subplot(1, 3, 3)
third_plot.bar(x, y, color="orange")
third_plot.set_title("example data-bar plot")
plt.show()
