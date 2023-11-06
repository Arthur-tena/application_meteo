import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import requests
import json

# Charger les données de pollution à partir d'un fichier CSV
data = pd.read_csv("/Users/arthurtena/Documents/open-meteo-52.52N13.41E38m-3.csv")

# Afficher les premières lignes du DataFrame pour vérifier les données
print(data.head())
col_name=data.columns

#Afficher les données pertinantes :
data=data.drop(columns=['elevation','utc_offset_seconds','timezone','timezone_abbreviation'])

data=data.drop(data.index[0:1])
print(data.head)

#plt.figure(figsize=(8, 6))  # Crée une nouvelle figure
#plt.plot(data.columns[0], data.index[1])
#plt.show()

#On met l'URL de la clef API pour la retrouver avec requests
url= 'https://api.open-meteo.com/v1/meteofrance?latitude=52.52&longitude=13.41&hourly=temperature_2m'

reponse=requests.get(url)

api_key = 'API météo Montpellier'

# Créez un en-tête avec la clé API
headers = {
    'Authorization': f'Bearer {api_key}'
}

# Effectuez la requête GET avec l'en-tête contenant la clé API
response = requests.get(url, headers=headers)
if response.status_code == 200:
    # Affichez le contenu de la réponse
    print(response.json())
else:
    print('La requête a échoué avec le code d\'état :', response.status_code)