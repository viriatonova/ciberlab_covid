import pandas as pd
import numpy as np


def data_cidade(data, cidade, tags):
    ''' 
    Isolando os dados por municipio.
    '''
    data_cidade = data.loc[cidade, tags]
    return data_cidade


def data_select(data, municipios, tags):
    '''
    Selecionando dados de municipios especificos.
    '''
    for cidade in municipios:
        if cidade == municipios[0]:
            data_municipios = data.loc[cidade, tags]
        else:
            cidade_check = data.loc[cidade, tags]
            data_municipios = data_municipios.append(cidade_check)
    return data_municipios


def data_anual(data_municipios, minicipios):
    data_covid_select = pd.DataFrame(
        {
            'Palmeiras':
            'Seabra':
            'Lençoís':
            'Mucugê':
            'Andaraí':
            'Ibicoara':
         }
    )
    for cidade in data_municipios.loc[municipios]:
        
    return




if __name__ == '__main__':
    
    # download o arquivo caso_full.csv no link -> https://brasil.io/dataset/covid19/files/
    data = pd.read_csv('/home/viriato/Documentos/projects/ciberlab_covid/data_base/caso_full.csv', index_col='city')
    
    tags = ['date', 'estimated_population', 'last_available_confirmed', 'last_available_deaths', 
    'new_deaths', 'last_available_date']
    municipios = ['Palmeiras', 'Seabra', 'Lençóis', 'Mucugê', 'Andaraí', 'Ibicoara']
    chapada_1 = data_select(data, municipios, tags)

    #print(chapada_1.set_index('date'))
    #chapada_1.to_excel('Covid_chapada.xlsx', index=True)
