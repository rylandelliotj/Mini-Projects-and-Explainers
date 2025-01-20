import pandas as pd

#%%

file = "C:\\Users\\rylaelli\\OneDrive - Canada Energy Regulator Régie de l'énergie du Canada\\Work Folder\\Projects\\Scrapes\\IMF Scrape\\imf_prices.csv"
df = pd.read_csv(file, chunksize=10)
above_50 = pd.DataFrame()

for chunk in df:
    filtered_chunk = chunk[chunk['Price (USD)'] > 50]
    filtered_chunk['Price (USD)'] = pd.to_numeric(filtered_chunk['Price (USD)'], downcast='float', errors='coerce')
    above_50 = pd.concat([above_50, filtered_chunk])
    
above_50.info()