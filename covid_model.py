import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame


def verification_city(data, cidades) -> None:
    '''
    Verifica se o nome da cidade consta
    no arquivo de dados
    '''
    for cidade in cidades:
        df = data.set_index('city')
        verify = cidade in df.index
        print(f'{cidade} - {verify}')
    return None


def data_cidade(data, cidade, tags, tag_analise) -> DataFrame:
    ''' 
    Isolando os dados do municipio por tags 
    e remove duplicatas de dados
    '''
    df = data.set_index('city')
    data_cidade = df.loc[cidade, tags]
    data_cidade = data_cidade.drop_duplicates(subset=tag_analise, keep='first')
    data_cidade['date'] = pd.to_datetime(data_cidade['date'])
    return data_cidade


def data_select(data, cidades, tags, tag_analise) -> DataFrame:
    '''
    Selecionando dados de municipios por parametro e 
    reunindo em um dataframe
    '''
    for cidade in cidades:
        if cidade == cidades[0]:
            municipio = data_cidade(data, cidade, tags, tag_analise)
            municipio = municipio.set_index('date')
            df = municipio.resample('M').max()
            df.reset_index(level=0, inplace=True)   
            df.rename(columns={tag_analise : f'{cidade} casos'})
        else:
            df1 = data_cidade(data, cidade, tags, tag_analise)
            df1 = df1.set_index('date')
            df2 = df1.resample('M').max()
            df2.reset_index(level=0, inplace=True) 
            df2.columns = pd.MultiIndex.from_product([[cidade], df2.columns])
            df2.rename(columns={tag_analise: f'{cidade} casos'})
            df = pd.concat([df, df2])
    municipio_select = df
    return municipio_select
