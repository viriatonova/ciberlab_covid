from covid_model import *

# download o arquivo caso_full.csv no link -> https://brasil.io/dataset/covid19/files/
data = pd.read_csv('/home/viriato/Documentos/projects/ciberlab_covid/data_base/caso_full.csv')

#tags_casos_full : 'last_available_deaths' / 'last_available_confirmed'

cidades = ['Palmeiras', 'Seabra', 'Lençóis', 'Mucugê', 'Andaraí', 'Ibicoara']
tags = ['date', 'last_available_deaths']
tag_analise = 'last_available_deaths'

covid = data_select(data,cidades, tags, tag_analise)
print(covid)
#covid.to_excel("municipios.xlsx")  
