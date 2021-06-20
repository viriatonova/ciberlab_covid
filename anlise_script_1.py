import pandas as pd
import numpy as np
from covid_model import *


# download o arquivo caso_full.csv no link -> https://brasil.io/dataset/covid19/files/
data = pd.read_csv('/home/viriato/Documentos/projects/ciberlab_covid/data_base/caso_full.csv')

tags = ['date', 'last_available_confirmed']
remove_duplicate = 'last_available_confirmed'
cidade = 'Palmeiras'

palmeiras = data_cidade(data, cidade, tags)
analise_palmeiras = cidade_analise(palmeiras, remove_duplicate)
analise_palmeiras.to_excel('Covid_palmeiras.xlsx', index=True)

'''
tags = ['date', 'estimated_population', 'last_available_confirmed', 'last_available_deaths', 'new_deaths', 'last_available_date']
municipios = ['Palmeiras', 'Seabra', 'Lençóis', 'Mucugê', 'Andaraí', 'Ibicoara']
chapada_1 = data_select(data, municipios, tags)
'''
