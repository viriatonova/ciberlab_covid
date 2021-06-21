import pandas as pd
import numpy as np
from covid_model import *


# download o arquivo caso_full.csv no link -> https://brasil.io/dataset/covid19/files/
data = pd.read_csv('/home/viriato/Documentos/projects/ciberlab_covid/data_base/caso_full.csv')

cidades = ['Palmeiras', 'Seabra', 'Lençóis', 'Mucugê', 'Andaraí', 'Ibicoara']
tags = ['date', 'last_available_confirmed']
tag_analise = 'last_available_confirmed'

for cidade in cidades:
    if cidade == cidades[0]:
        municipios = data_cidade(data, cidade, tags, tag_analise)
    else:
        df = data_cidade(data, cidade, tags, tag_analise)
        municipios = municipios.append(df)
municipios.to_excel('chapada_casos.xlsx')
