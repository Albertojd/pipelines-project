import pandas as pd
import numpy as np
import sys
import seaborn as sns
import matplotlib.pyplot as plt

def cleaning():
    import pandas as pd
    df = pd.read_csv('countriesworld.csv' ,decimal=',', encoding = 'latin1')
    df.columns = df.columns.str.rstrip()
    df.columns =df.columns.str.replace(" ", "_")
    df.Country =df.Country.str.rstrip()
    df = df.set_index(['Country'])
    df.rename(columns=lambda x: x.replace("(%)", 'percent'), inplace=True)
    df.rename(columns={'GDP_($_per_capita)': 'GDP'}, inplace=True)
    df.rename(columns=lambda x: x.replace("(", ''), inplace=True)
    df.rename(columns=lambda x: x.replace(")", ''), inplace=True)
    df.rename(columns=lambda x: x.replace(".", ''), inplace=True)
    df = df.drop(['Area_sq_mi', 'Pop_Density_per_sq_mi','Coastline_coast/area_ratio','Phones_per_1000',
              'Climate','Agriculture','Service','Industry','Agriculture','Other_percent','Crops_percent'], axis = 1)    
    return df

cleaning().to_csv (r'\Users\alber\IRONHACK\proyectos\pipelines-project\CleanWorld.csv ', index = False)