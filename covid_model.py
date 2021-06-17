import pandas as pd
import numpy as np


def data_cidade(data, cidade, tags):
    ''' 
    Isolando os dados por municipio.
    '''
    data_cidade = data.loc[cidade, tags]
    return data_cidade


def data_comparado(data, municipios, tags):
    '''
    Comparando dados vários municipios.
    '''
    for cidade in municipios:
        if cidade == municipios[0]:
            data_municipios = data.loc[cidade, tags]
        else:
            cidade_check = data.loc[cidade, tags]
            data_municipios = data_municipios.append(cidade_check)
    return data_municipios


if __name__ == '__main__':
    
    # download o arquivo caso_full.csv no link -> https://brasil.io/dataset/covid19/files/
    data = pd.read_csv('/home/viriato/Documentos/projects/ciberlab_covid/data_base/caso_full.csv', index_col='city')
    
    tags = ['date', 'estimated_population', 'last_available_confirmed', 'last_available_deaths', 
    'new_deaths', 'last_available_date']

    municipios = ['Palmeiras', 'Seabra', 'Lençóis', 'Mucugê', 'Andaraí', 'Ibicoara']
    
    chapada_1 = data_comparado(data, municipios, tags)
    chapada_1.to_excel('Covid_chapada.xlsx', index=True)

    '''palmeiras_excel = data_cidade(data, "Palmeiras")
    palmeiras_excel.to_excel('Palmeiras_casos.xlsx', sheet_name='data_palmeiras', index=False)'''
