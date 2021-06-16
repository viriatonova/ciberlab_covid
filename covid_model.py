import pandas as pd
import numpy as np

# download o arquivo caso_full.csv no link -> https://brasil.io/dataset/covid19/files/
data = pd.read_csv('/home/viriato/megaterio/cybertech/ciberlab_covid/data_base/caso_full.csv', index_col='city')


def data_cidade(data, cidade):
    ''' 
    Isolando os dados por municipio.
    '''
    data_cidade = data.loc[cidade, ['date', 'estimated_population_2019','last_available_confirmed', 
    'last_available_deaths', 'new_confirmed', 'new_deaths', 'is_repeated']]
    return data_cidade


def data_comparado(data, lista_municipios, tag):
    '''
    Comparando dados vários municipios.
    O parametro tag seleciona a coluna de dados há ser comparada.
    '''
    for cidade in len(lista_municipios):
        data_municipio = data.loc[cidade,[tag]]
        data_municipio.to_excel('municipios_comparados.xlsx', sheet_name=f'data_{cidade}', index=False)
    return None


if __name__ == '__main__':
    
    print(data)

    #municipios = ['Palmeiras', 'Seabra', 'Lençois', 'Mucugê', 'Andarai']
    '''palmeiras_excel = data_cidade(data, "Palmeiras")
    palmeiras_excel.to_excel('Palmeiras_casos.xlsx', sheet_name='data_palmeiras', index=False)'''

