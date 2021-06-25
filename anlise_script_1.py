from covid_model import *

# download o arquivo caso_full.csv no link -> https://brasil.io/dataset/covid19/files/
data = pd.read_csv('/home/viriato/Documentos/projects/ciberlab_covid/data_base/caso_full.csv')

#tags_casos_full : 'last_available_deaths' / 'last_available_confirmed'

cidades = ['Palmeiras', 'Seabra', 'Lençóis', 'Mucugê', 'Andaraí', 'Ibicoara']
tags = ['date', 'last_available_deaths']
tag_analise = 'last_available_deaths'


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

df.to_excel("municipios.xlsx")  
