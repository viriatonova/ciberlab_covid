import pandas as pd
import numpy as np
from covid_model import *


# download o arquivo caso_full.csv no link -> https://brasil.io/dataset/covid19/files/
data = pd.read_csv('/home/viriato/Documentos/projects/ciberlab_covid/data_base/caso_full.csv')

cidades = ['Palmeiras', 'Seabra', 'Lençóis', 'Mucugê', 'Andaraí', 'Ibicoara']
tags = ['date', 'last_available_confirmed']
tag_analise = 'last_available_confirmed'
df1 = pd.DataFrame((cidades), columns =['Cidades']) 

for cidade in cidades:
    if cidade == cidades[0]:
        municipio = data_cidade(data, cidade, tags, tag_analise)
        municipio = municipio.set_index('date')
        soma = municipio.resample('M').sum()
        df1['date'] = soma.index
        df1['last_available_confirmed'] = soma['last_available_confirmed']
    else:
        df = data_cidade(data, cidade, tags, tag_analise)
        df = df.set_index('date')
        soma = df.resample('M').sum()
        df1['date'] = soma.index
        df1['last_available_confirmed'] = soma.append[soma['last_available_confirmed']]
        
print(df1)

#municipios = municipios.groupby(['city']).max()
#municipios['mes'] = pd.DatetimeIndex(municipios['date']).month
#municipios = municipios.groupby(['city']).max()
#municipios = municipios.set_index('date')
#print(municipios)
#municipios.to_excel('test.xlsx')
