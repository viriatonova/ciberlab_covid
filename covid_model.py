import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame


def data_cidade(data, cidade, tags, tag_analise) -> DataFrame:
    ''' 
    Isolando os dados do municipio por tags 
    e remove duplocadas de dados
    '''
    df = data.set_index('city')
    data_cidade = df.loc[cidade, tags]
    data_cidade = data_cidade.drop_duplicates(subset=tag_analise, keep='first')
    data_cidade['date'] = pd.to_datetime(data_cidade['date'])
    return data_cidade


def data_select(data, municipios, tags):
    '''
    Selecionando dados de municipios especificos.
    '''
    data_municipios = data.set_index('city')
    for cidade in municipios:
        if cidade == municipios[0]:
            data_municipios = data.loc[cidade, tags]
        else:
            cidade_check = data.loc[cidade, tags]
            data_municipios = data_municipios.append(cidade_check)
    return data_municipios
