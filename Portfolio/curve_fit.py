# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 09:40:57 2024

@author: RylaElli
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# Define your equation. In this case, the Arps equation.
def model(t, qi, b, Di):
    return qi * (1 + b * Di * t)**(-1/b)

# Create fake data (see faking_data.py for explanation)
size = 20
T = np.linspace(0, size-1, num=size)

mu = 0
std = 1.5
QI = 20
b = 1
di = 0.3
avg_prod = model(T, QI, b, di) + np.random.normal(size=size, loc=mu, scale=std)

# Use your initial guess for the model parameters
initial_guess = [avg_prod.max(), 1, 0.1]

# Define upper and lower bounds
bounds = ([-np.inf, 1, 0], [np.inf, 2, np.inf])

# Use curve_fit
# Pos Args: function, x axis data, y axis data, p0=initial guess for parameters, bounds=max and min allowable parameter magnitudes
# Results are given as a tuple: parameters and a covariance matrix
# The covariance with itself tells you how sensitive the parameter is to change.
# A higher number indicates high sensitivity, and potentially unuseful parameter.
parameters, covariance = curve_fit(model, T, avg_prod, p0=initial_guess, bounds=bounds)

# Create data of estimated y (avg_prod) at each x (T) given the model parameters
# This can be used to create a line with plt.plot()
ans = model(T, parameters[0], parameters[1], parameters[2])

# Plot the results
plt.scatter(T, avg_prod, label='Data')
plt.plot(T, ans, color='red', label='Decline Curve')
plt.title('Transient Flow for a Well (Test)')
plt.xlabel('Production Month')
plt.ylabel('Average Production')
plt.xticks(np.arange(0, size, step=2))
plt.legend()
plt.show()