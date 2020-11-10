import json
import requests
import pandas as pd
from pandas import json_normalize
from IPython.display import Image
from IPython.core.display import HTML 

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

class color:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def capital(x):
    url = f"https://restcountries.eu/rest/v2/name/{x}?fullText=true"
    response = requests.get(url)
    data = response.json()
    capital = [x["capital"] for x in data]
    return print(f'Capital:',color.BOLD+capital[0]+color.END)

def timezone(x):
    url = f"https://restcountries.eu/rest/v2/name/{x}?fullText=true"
    response = requests.get(url)
    data = response.json()
    timezone = [x["timezones"] for x in data]
    return print(f'Time zone:',color.BOLD+timezone[0][0]+color.END)

def nativename(x):
    url = f"https://restcountries.eu/rest/v2/name/{x}?fullText=true"
    response = requests.get(url)
    data = response.json()
    results = [x["nativeName"] for x in data]
    return print(f'Native name:',color.BOLD+results[0]+color.END)

def languages(x):
    url = f"https://restcountries.eu/rest/v2/name/{x}?fullText=true"
    response = requests.get(url)
    data = response.json()
    results = [x["languages"] for x in data]
    lang = [x["name"] for x in results[0]]
    return print(f'Language:',color.BOLD+lang[0]+color.END)

def currencies(x):
    url = f"https://restcountries.eu/rest/v2/name/{x}?fullText=true"
    response = requests.get(url)
    data = response.json()
    results = [x["currencies"] for x in data]
    curr = [x["name"] for x in results[0]]
    return print(f'Currecy:',color.BOLD+curr[0]+color.END)

def area(x):
    url = f"https://restcountries.eu/rest/v2/name/{x}?fullText=true"
    response = requests.get(url)
    data = response.json()
    area = [x["area"] for x in data]
    return int(area[0])

def flag(x):
    url = f"https://restcountries.eu/rest/v2/name/{x}?fullText=true"
    response = requests.get(url)
    data = response.json()
    results = [x["flag"] for x in data]
    return Image(url=results[0])

def api(x):
    url = f"https://restcountries.eu/rest/v2/name/{x}?fullText=true"
    response = requests.get(url)
    results = response.json()
    return results

def world(x):
    data = cleaning()
    x= x.capitalize()
    results = api(x)
    print(f'It seems that you want to know something about {x}, find below some information' )
    population = (data.loc[x,'Population'])
    gdp = (data.loc[x,'GDP'])
    birth= (data.loc["Spain",'Birthrate'])
    death= (data.loc["Spain",'Deathrate'])
    density=population/area(x)
    capital(x)
    languages(x)
    nativename(x)
    currencies(x)
    timezone(x)
    
    print(f'Population:',color.BOLD+'{0:,}'.format(population)+color.END)
    print(f'Gross Domestic Product:',color.BOLD+'{0:,}'.format(gdp)+color.END,'$')
    print(f'Birthrate:',color.BOLD+'{0:,}'.format(birth)+color.END,'‰' )
    print(f'Deathrate:',color.BOLD+'{0:,}'.format(death)+color.END,'‰' )
    print(f'population density;',color.BOLD+'{0:,}'.format(density)+color.END,'hab/km²')
    display(flag(x))
    return