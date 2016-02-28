"""
Generating random data and fitting the data using 
least squares linear regression. 
m > n
"""

import numpy as np
import matplotlib.pyplot as plt

# Number of Data points
m = 25

# Number of Parameters
n = 2

# Generate random numbers, output an array/matrix. 
# rand(# of rows, # of columns)
# *10 adjusts the decimal place 
x = np.random.rand(m,n)*10

# Generate a mXn matrix 
# First row is ones
# Second row is the first column of x
# Then take the Transpose so the rows are columns
# First column is ones, sencond column is the first column of x
a = np.matrix([np.ones(m), x[:,0]]).T

# Generate a mX1 matrix
# The second column of x
b = np.matrix(x[:,1]).T

# Multiply a transpose time a and take the inverse
# and multiply it by a transpose and b
# Solving the Normal Equations
# yy are the beta's in a nX1 matrix
yy = (a.T * a).I * a.T * b

# Generate 50 points as input for the solution function
# return evenly spaced numbers over a specified interval
# (start, stop, num_of_points)
xx = np.linspace(1, 10, 50)

# Generate the approximated y values using the betas and
# the 50 generated points
y = np.array(yy[0] + yy[1] * xx)

# Opening a window instance
plt.figure(1)

# Plotting the line using the generated x and y values
plt.plot(xx, y.T, color='r')

# Plotting the origional random points
plt.scatter(x[:,0], x[:,1])

# Holding the window open
plt.show()

