from covid_model import *

#tags_casos_full : 'last_available_deaths' / 'last_available_confirmed'

# download o arquivo caso_full.csv no link -> https://brasil.io/dataset/covid19/files/
data = pd.read_csv('/home/viriato/Documentos/projects/ciberlab_covid/data_base/caso_full.csv')

'''
cidades = ['Palmeiras', 'Seabra', 'Lençóis', 'Mucugê', 'Andaraí', 'Ibicoara']
tags = ['date', 'last_available_deaths']
tag_analise = 'last_available_deaths'

covid = data_select(data,cidades, tags, tag_analise)
print(covid)
#covid.to_excel("municipios.xlsx")  
'''

# Dividindo a Bahia em zonas turisticas 

todos_santos = [
'Salvador', 'Aratuípe', 'Cachoeira', 'Candeias', 'Itaparica', 'Vera Cruz', 
'Madre de Deus', 'Maragogipe', 'Muniz Ferreira', 'Nazaré', 
'Salinas da Margarida', 'Santo Amaro', 'São Félix', 'São Francisco do Conde', 'Saubara', 'Simões Filho'
]

# Verification tag existence
verification_city(data, todos_santos)
