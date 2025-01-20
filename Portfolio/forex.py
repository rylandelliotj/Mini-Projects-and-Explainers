# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 13:56:10 2024

@author: RylaElli
"""
import numpy as np
import matplotlib.pyplot as plt

cad_holding = 15
usd_holding = 10
forex = np.linspace(0.1, 5, 100)

def total_holdings(currency, forex):
    if currency.upper() == 'CAD':
        return cad_holding + (usd_holding / forex)
    elif currency.upper() == 'USD':
        return (cad_holding / forex) + usd_holding
    else:
        print("currency not compatible with function")


currency = 'CAD'
foreign_currency = "USD" if currency == "CAD" else "CAD"
cad = total_holdings(currency, forex)

fig, ax = plt.subplots()
ax.plot(forex, cad, label = f'CAD: ${cad_holding}\nUSD: ${usd_holding}')
ax.axvspan(1, 5, alpha = 0.25, color = 'green', label = f'Appreciating {foreign_currency}\n({foreign_currency[0:2]} imports from {currency[0:2]})')
ax.axvspan(0, 1, alpha = 0.25, color = 'red', label = f'Depreciating {foreign_currency}\n({foreign_currency[0:2]} exports to {currency[0:2]})')
ax.set_ylim(0)
ax.set_xlim(0, 5)
plt.xticks(np.linspace(0, 5, 11), rotation = 45)
plt.legend()
plt.xlabel(f'Forex {"(CAD / USD)" if currency == "USD" else "(USD / CAD)"}')
plt.ylabel(f'Total holdings in ${currency}')
plt.title('Total Holdings by Forex')
plt.show()