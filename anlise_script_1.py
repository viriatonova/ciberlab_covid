import openpyxl
from covid_model import *
import pandas as pd
import numpy as np
from openpyxl import load_workbook


#tags_casos_full : 'last_available_deaths' / 'last_available_confirmed' / 'date' / 

# download o arquivo caso_full.csv no link -> https://brasil.io/dataset/covid19/files/
data = pd.read_csv('/home/viriato/megaterio/cybertech/ciberlab_covid/data_base/caso_full.csv')
tags = ['date', 'last_available_confirmed']
tag_analise = 'last_available_confirmed'

# Chapada Diamantina
    # Circuito da Chapa Norte
chapada_norte = [
'Bonito', 'Campo Formoso', 'Quixabeira', 'Jacobina', 'Miguel Calmon', 'Ourolândia', 'Pindobaçu', 'Senhor do Bonfim', 'Utinga'
]

'''
covid = data_select(data, chapada_norte, tags, tag_analise)
covid.to_excel("chapada_norte.xlsx")
'''

    # Circuito do Diamante
diamante = [
'Andaraí', 'Ibicoara', 'Iraquara', 'Itaeté', 'Lençóis', 'Mucugê', 'Barra da Estiva', 'Boninal', 'Iramaia', 
'Itaberaba', 'Ituaçu', 'Nova Redenção', 'Palmeiras', 'Seabra'
]

    # Circuito do Ouro
ouro = [
    'Abaíra', 'Jussiape', 'Paramirim', 'Piatã', 'Dom Basílio', 'Rio de Contas'
]
    # Circuito Chapada Velha
velha = [
'Barra do Mendes', 'Brotas de Macaúbas', 'Gentio do Ouro', 'Central'
]

# Bahia de Todos os Santos 

todos_santos = [
'Salvador', 'Aratuípe', 'Cachoeira', 'Candeias', 'Itaparica', 'Vera Cruz', 
'Madre de Deus', 'Maragogipe', 'Muniz Ferreira', 'Nazaré', 
'Salinas da Margarida', 'Santo Amaro', 'São Félix', 'São Francisco do Conde', 'Saubara', 'Simões Filho'
]

# Caminhos do Jequiriçá

jequiriça = [
'Amargosa', 'Jiquiriçá', 'Milagres', 'Mutuípe', 'Santa Inês', 
'Ubaíra', 'Castro Alves', 'Cruz das Almas', 'Dom Macedo Costa', 'Santa Terezinha', 'Varzedo', 'Itatim'
]

# Caminhos do Oeste
oeste = [
'Barra', 'Barreiras', 'Santa Rita de Cássia', 'São Desidério', 'Bom Jesus da Lapa', 'Correntina', 'Ibotirama', 
'Santa Maria da Vitória', 'Jaborandi', 'São Félix do Coribe' 
]

# Caminhos do Sudoeste
sudoeste = ['Iguaí', 'Jequié', 'Maracás', 'Vitória da Conquista']

# Caminhos do Sertão
sertao = [
'Feira de Santana', 'Canudos', 'Euclides da Cunha', 'Itapicuru', 'Tucano', 'Cipó', 'Uauá', 'Adustina', 'Alagoinhas', 'Irará', 
'Banzaê', 'Paripiranga', 'Santo Estêvão'
]

# Costa do Dendê
dende = [
'Cairu', 'Camamu', 'Valença', 'Taperoá', 'Igrapiúna', 'Ituberá'
]

# Costa dos Coqueiros
coqueiros = [
'Mata de São João', 'Jandaíra', 'Entre Rios', 'Conde', 'Lauro de Freitas', 'Esplanada', "Dias d'Ávila", 'Camaçari'
]

# Costa do Cacau
cacau = [
    'Ilhéus', 'Itacaré', 'Ipiaú', 'Maraú', 'Una', 'Canavieiras', 'Itabuna', 'Uruçuca', 'Santa Luzia', 'Pau Brasil', 'São José da Vitória'
]

# Costa das Baleias
baleias = [
'Alcobaça', 'Caravelas', 'Itamaraju', 'Mucuri', 'Nova Viçosa', 'Prado', 'Teixeira de Freitas' 
]

# Costa do Descobrimento
descobrimento = [
'Porto Seguro', 'Santa Cruz Cabrália', 'Belmonte', 'Guaratinga'
]

# Lagos e Cânios do São Francisco
francisco = [
'Paulo Afonso', 'Santa Brígida'
]

# Vale do São Francisco
vale_francisco = [
'Juazeiro', 'Sobradinho', 'Remanso', 'Curaçá', 'Sento Sé'
]

zonas_bahia = [
chapada_norte, diamante, ouro, velha, todos_santos, jequiriça,
oeste, sudoeste, sertao, dende, coqueiros, cacau, baleias, descobrimento,
francisco, vale_francisco
]

path = '/home/viriato/megaterio/cybertech/ciberlab_covid/zonas_bahia.xlsx'
book = load_workbook(path)
covid = pd.ExcelWriter(path, engine='openpyxl')
covid.book = book

cont = 0
for zona in zonas_bahia:
    tur_bahia = data_select(data, zona, tags, tag_analise)
    tur_bahia.to_excel(covid, sheet_name=f'zona{cont}', index=False)
    covid.save()
    cont += 1
covid.close()
