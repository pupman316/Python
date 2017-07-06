# import plotly.plotly as plotLib
# import plotly.graph_objs as graphLib
import matplotlib.pyplot as plt
import numpy as np

#plt.interactive(False)  # Recommended from Stack Exchange

print("Hello World", "\n")

# Random number generation is handled here
N = 50
x = np.linspace(0.0, 1.0, N)
y = np.random.randn(N)

colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radii

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()

# # Create random data with numpy
# N = 500
# random_x = np.linspace(0, 1, N)
# random_y = np.random.randn(N)
#
# # Create a trace
# trace = graphLib.Scatter(
#     x = random_x,
#     y = random_y
# )
#
# data = [trace]
#
# plotLib.iplot(data, filename='basic')






# test = [1, 2, 3, 4, 5]
# for x in test:
#     print(x)

print("\n", "Goodbye World!")
