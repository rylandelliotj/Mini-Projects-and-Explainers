# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 10:47:27 2024

@author: RylaElli
"""

'''
Assume our npv in year one is $1000. 
This means that the total lifetime value of some activity we want to engage in (ex. drilling wells) is worth $1000 to us today
'''
initial_npv = 1000

'''
let's not assume that it is some year in the future, and we want to drill more wells.
As with our first year, we will calculate our npv (see above for explanation)
Feel free to adjust this number to above or below the initial number
'''
future_npv = 2000

'''
Here is where things get important.
Imagine it is still the future year, and I am deciding how many wells to drill.
How do I decide?
One way would be to look at how many wells I drilled in the initial year, 
and see if I have become more profitable (future_npv > initial_npv) or less profitable (future_npv < initial_npv).
If I have become more profitable, I would want to drill more wells compared to that initial year.
But how many wells?
That depends on how sensitive to profit I am, and this is where elasticity comes in.

If I decide that if I am 10% more profitable this year, so therefore I should drill 10% more, 
then activity_factor_elasticity = 1 (unit elastic).

If I am a bit more hestiant to drill as many as I did in the first year (non-proportional, higher),
then 0 > activity_factor_elasticity < 1 (inelastic).

If I see any increase in profit to be a signal of magnificent returns to come in the future (non-proportional, higher),
then activity_factor_elasticity > 1 (inelastic).
'''
activity_factor_elasticity = 0.6

'''
If I am in the future, my wells drilled depends on what was drilled in the initial year,
so we need to have data on how many wells are drilled in the initial year.
This is why the activity factor is 1 for the initial year: we obviously drill 100% of what has been drilled.
Set the 'current year' to be whatever you want to understand.
'''
current_year = 2

if current_year > 1:
    '''
    Now we calculate our activity factor for the future year.
    First we take the difference in the the npv values - how much more/less profitable are we?
    Next, we want to ask the percent increase from year one,
    However, as mentioned, we may not want a proportional increase, so we must multiply by the activity factor elasticity.
    Note that, if elasticity is one, then the increase is proportional.
    Finally, we add one. We do this because one is our baseline.
    All we have done to this point is see the fraction of a proportional increase in profit, 
    but if we were to multiply this number by the number of wells drilled, 
    we would get less wells drilled when we are more profitable!
    That is why we add one.
    '''
    activity_factor = ((future_npv - initial_npv) * activity_factor_elasticity) / initial_npv + 1
else:
    activity_factor = 1

# Here is the activity factor
print("Activity Factor: " + str(activity_factor))

'''
Finally, let's put this to use.
We want to see how many more wells we are going to drill.
All we do to find this is multiply the activity factor by the wells drilled in the initial year.
Note how there is no assumption of data given in the future year;
that is the importance of this exercise: obtain meaningful results without data!
'''

wells_drilled_initial = 10

print('Wells Drilled in First Year: ' + str(wells_drilled_initial))
print('Wells Drilled in Future Year: ' + str(wells_drilled_initial*activity_factor))