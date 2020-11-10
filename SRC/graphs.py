import pandas as pd
import numpy as np
import sys
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('countriesworld.csv',decimal=',',engine = 'python')
df.head()

df.columns = df.columns.str.rstrip()
df.columns =df.columns.str.replace(" ", "_")
df.rename(columns=lambda x: x.replace("(%)", 'percent'), inplace=True)
df.rename(columns={'GDP_($_per_capita)': 'GDP'}, inplace=True)
df.rename(columns=lambda x: x.replace("(", ''), inplace=True)
df.rename(columns=lambda x: x.replace(")", ''), inplace=True)
df.rename(columns=lambda x: x.replace(".", ''), inplace=True)

df_gdp = df.sort_values('GDP',ascending=False)
x = df_gdp.Country.head(11)
y = df_gdp.GDP.head(11)
plt.title("Gross Domestic Product")
plt.xlabel("Countries with the highest gdp")
plt.ylabel("$ Millions")
plt.bar(x, y)
plt.xticks(rotation=75)
plt.savefig("maxGDB.PNG", bbox_inches='tight')

df_gdp = df.sort_values('GDP')
x = df_gdp.Country.head(11)
y = df_gdp.GDP.head(11)
plt.title("Gross Domestic Product")
plt.xlabel("Countries with the highest gdp")
plt.ylabel("$ Millions")
plt.bar(x, y)
plt.xticks(rotation=75)
plt.savefig("minGDB.PNG", bbox_inches='tight')