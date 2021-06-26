from covid_model import *

#tags_casos_full : 'last_available_deaths' / 'last_available_confirmed'

# download o arquivo caso_full.csv no link -> https://brasil.io/dataset/covid19/files/
data = pd.read_csv('/home/viriato/megaterio/cybertech/ciberlab_covid/data_base/caso_full.csv')

# Analise Chapada Diamantina
'''
chapada = ['Palmeiras', 'Seabra', 'Lençóis', 'Mucugê', 'Andaraí', 'Ibicoara']
tags = ['date', 'last_available_deaths']
tag_analise = 'last_available_deaths'
covid = data_select(data, chapada, tags, tag_analise)
covid.to_excel("municipios.xlsx")
'''

# Analise Bahia de Todos os Santos 
todos_santos = [
'Salvador', 'Aratuípe', 'Cachoeira', 'Candeias', 'Itaparica', 'Vera Cruz', 
'Madre de Deus', 'Maragogipe', 'Muniz Ferreira', 'Nazaré', 
'Salinas da Margarida', 'Santo Amaro', 'São Félix', 'São Francisco do Conde', 'Saubara', 'Simões Filho'
]
tags = ['date', 'last_available_confirmed']
tag_analise = 'last_available_confirmed'
covid2 = data_select(data,todos_santos, tags, tag_analise)
covid2.to_excel("municipios.xlsx")

# Analise Caminhos do Jequiriçá
jequiriça = [
    
]

# Verification tag existence
'''
verification_city(data, todos_santos)
'''
