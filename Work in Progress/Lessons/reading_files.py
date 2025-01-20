import csv
import pandas as pd

#%%

file = "C:\\Users\\rylaelli\\OneDrive - Canada Energy Regulator Régie de l'énergie du Canada\\Work Folder\\Projects\\Scrapes\\IMF Scrape\\imf_prices.csv"
filtered_file = "C:\\Users\\rylaelli\\OneDrive - Canada Energy Regulator Régie de l'énergie du Canada\\Work Folder\\Projects\\Scrapes\\IMF Scrape\\imf_prices_filtered.csv"

with open(file, 'r') as infile, open(filtered_file, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    for row in reader:
        if '2024' in row[0]:
            writer.writerow(row)
            
pd.read_csv(filtered_file)