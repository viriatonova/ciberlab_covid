import pandas as pd
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


def data_cidade(data: DataFrame, cidade: str, tags: list[str], tag_analise: str) -> DataFrame:
    """
    Isolando os dados do municipio por tags
    e remove duplicatas de dados
    """

    df = data.set_index('city')
    data_cidade = df.loc[cidade, tags]
    data_cidade = data_cidade.drop_duplicates(subset=tag_analise, keep='first')
    data_cidade['date'] = pd.to_datetime(data_cidade['date'])

    return data_cidade


def select_data(data: DataFrame, cidades: list[str], tags: list[str], tag_analise: str) -> DataFrame:
    """
    Seleciona dados de municípios por parametros e
    retorna em um DataFrame.
    """

    first = True
    for cidade in cidades:
        municipio = data_cidade(data, cidade, tags, tag_analise)
        municipio.set_index('date', inplace=True)
        municipio = municipio.resample('M').max()
        municipio = municipio.reset_index(level=0)
        municipio = municipio.rename(
            columns={tag_analise: f'Casos {cidade}'})
        if first:
            first = False
            municipios = municipio
        else:
            municipios = pd.merge(municipios, municipio,
                                    how='outer', on='date')

        municipios.fillna(0, inplace=True)
        
    return municipios
