import pandas as pd
import numpy as np


def data_cidade(data, cidade, tags):
    ''' 
    Isolando os dados do municipio por tags.
    '''
    data_cidade = data.set_index('city')
    data_cidade = data_cidade.loc[cidade, tags]
    return data_cidade

def cidade_analise(data_cidade, tags):
    '''
    Remove os dados repetidos do data frame 
    gerado pela função data_cidade
    '''
    df = data_cidade.drop_duplicates(subset=tags, keep='first')
    return df


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
