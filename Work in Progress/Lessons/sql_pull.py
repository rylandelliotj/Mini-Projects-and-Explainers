#%% Import packages
import sqlalchemy
import pyodbc
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from urllib.parse import quote_plus

#%% Make a connection to CERSEI
params = quote_plus(r'DRIVER={SQL Server Native Client 11.0};SERVER=pSQL22CAP;DATABASE=EnergyData;Trusted_Connection=yes')
conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
engine = sqlalchemy.create_engine(conn_str)

table = 'AER_ST39'
df = pd.read_sql_table(table, engine)