# -*- coding: utf-8 -*-
"""
This is proof of the concept of Expected Value.
EV should converge to reality the greater the sample size.
Let's assume that we want to know approximately how much LNG production is going to come online from new projects in a given future date.
"""

import numpy as np
import matplotlib.pyplot as plt

def ev(size):
    ### Start with the theoretical analysis ###
    
    # First, we asssign the expected capacity of these projects (between 10-70mpta of LNG)
    mpta = np.random.randint(10, 70, size=size)
    
    # Next, we assign liklihood of the project coming online
    probabilities = np.random.rand(size)
    
    # Then, we calculate expected value
    ev = sum(mpta * probabilities)
    
    ### Next, we want to do the empirical analysis. ###
    
    ''' 
    the idea here is to assign a 0 or 1 to the project to show if project comes online,
    but we want this chance to be higher for projects with a higher probability.
    '''
    
    random_numbers = np.random.rand(size) # we need to assign some random numbers.
    online = (random_numbers < probabilities).astype(int) # Now, compare the probabilities with the random numbers to assign a 0 or 1.
    sim = sum(online*mpta) # Take the sum of the boolean value with the production value. This provides the modelled output.
    
    # Get some summary statistics
    difference = sim - ev
    error = difference / sim
    
#    print('Expected MPTA: ' + str(round(ev,2)))
#    print('Empirical (simulated) MPTA: ' + str(sim))
#    print('Difference: ' + str(round(difference,2)))
#    print('Error: ' + str(round(error * 100, 2)) + '%')
    
    return error

print(ev(10000))

### Run with different sizes to see law of large numbers in action ###

start = 10
stop = 3000
step = 1
sizes = np.arange(start, stop, step)

# Turn into a vectorized funciton
vectorize = np.vectorize(ev)

# Get errors
errors = vectorize(sizes)

# Plot errors with sample sizes
plt.plot(sizes, errors)
plt.title("Error size by sample size")
plt.xlabel("Sample Size")
plt.ylabel("Error Size")
plt.show()

print(f'Error at {start} sample size: {round(errors[0] * 100,2)}%')
print(f'Error at {stop} sample size: {round(errors[-1] * 100,2)}%')