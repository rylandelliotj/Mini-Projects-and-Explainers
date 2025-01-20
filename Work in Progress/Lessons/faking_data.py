# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 09:08:08 2024

@author: RylaElli
"""

import numpy as np
import matplotlib.pyplot as plt

# Determine sample size
size = 40

# Create your x variables through linspace
# Pos Arg: lower bound, upper bound, number of elements.
# Note: this evenly distributes the points, use np.random.normal() to add on some noise

x = np.linspace(0,10,num=size)
#x = np.arange(0,size,step=1) # alternatively, use this if you want to control the step values (useful for discrete numbers like years)

# Create y variables as f(x)
# This is where you want to plug in your equation
# In thjis example, our function is a*sin(b*x) where a and b are constants
# Add some noise with np.random.normal() to make sure it is not a perfect line. 
# Args: scale = standard deviation, loc = mean, size = number of elements

def function(x,a,b):
    return a * np.sin(b*x)

a = 3.25
b = 1.334
std = 1
mu = 0
y = function(x, a, b) + np.random.normal(size=size, scale=std, loc=mu)

# Let's take a look at the result: a noisy sin wave
plt.scatter(x,y)
plt.show()