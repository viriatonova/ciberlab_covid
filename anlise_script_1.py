import pandas as pd
import numpy as np
from covid_model import *
from pandas.core.frame import DataFrame
import openpyxl


# download o arquivo caso_full.csv no link -> https://brasil.io/dataset/covid19/files/
data = pd.read_csv('/home/viriato/megaterio/cybertech/ciberlab_covid/data_base/caso_full.csv')

cidades = ['Palmeiras', 'Seabra', 'Lençóis', 'Mucugê', 'Andaraí', 'Ibicoara']
tags = ['date', 'last_available_confirmed']
tag_analise = 'last_available_confirmed'


for cidade in cidades:
    if cidade == cidades[0]:
        municipio = data_cidade(data, cidade, tags, tag_analise)
        municipio = municipio.set_index('date')
        df = municipio.resample('M').max()
        df.reset_index(level=0, inplace=True)   
        df.columns = pd.MultiIndex.from_product([[cidade], df.columns])
    else:
        df1 = data_cidade(data, cidade, tags, tag_analise)
        df1 = df1.set_index('date')
        df2 = df1.resample('M').max()
        df2.reset_index(level=0, inplace=True) 
        df2.columns = pd.MultiIndex.from_product([[cidade], df2.columns])
        df = pd.concat([df, df2])

df.to_excel("municipios.xlsx", index=False)  
