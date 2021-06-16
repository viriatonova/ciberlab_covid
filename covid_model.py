import pandas as pd
import numpy as np

data = pd.read_csv('/home/viriato/megaterio/cybertech/ciberlab_covid/data_base/caso_full.csv', index_col='city')

def data_cidade(data, cidade):
    ''' 
    Isolando os dados por municipio
    '''
    data_cidade = data.loc[cidade, ['date', 'estimated_population_2019','last_available_confirmed', 
    'last_available_deaths', 'new_confirmed', 'new_deaths', 'is_repeated']]
    return data_cidade

#def 


if __name__ == '__main__':
    
    palmeiras_excel = data_cidade(data, "Palmeiras")
    palmeiras_excel.to_excel('Palmeiras_casos.xlsx', sheet_name='data_palmeiras', index=False)


