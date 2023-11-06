import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import requests
import json
import datetime 

#On charge les données de meteo à partir d'un fichier CSV
data = pd.read_csv("/Users/arthurtena/Documents/application_meteo/data/weather.csv")

# Afficher les premières lignes du DataFrame pour vérifier les données
print(data.head())
col_name=data.columns

#Afficher les données pertinantes :
data=data.drop(columns=['elevation','utc_offset_seconds','timezone','timezone_abbreviation'])
data=data.drop(data.index[0:1])
print(data.head)

#On crée une fonction qui donne la date et l'heure actuelle 
def date_heure():
    now=datetime.datetime.now()
    #On formate la date et l'heure
    date_format = now.strftime('%Y-%m-%d')  # Format AAAA-MM-JJ
    heure_format = now.strftime('%H:%M')  # Format HH:MM

    return f"{date_format}T{heure_format}" 

print(date_heure())

#On affiche le jour de la semaine 
maintenant = datetime.datetime.now()
print(maintenant.weekday())
# Obtenir le jour de la semaine actuel (en texte)
jour_semaine = maintenant.strftime('%A')  # Format du jour de la semaine (par exemple : "lundi", "mardi", etc.)
print("Jour de la semaine actuel :", jour_semaine)


#On crée une boucle qui nous donne la température à l'heure actuelle
for i in range(2, 97):
    if date_heure()==data.iloc[i,1]:
        print(data.iloc[i, 2])

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



