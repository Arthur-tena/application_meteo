import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import requests
import json
import datetime 
from more_itertools import chunked

#On charge les données de meteo à partir d'un fichier CSV
#data = pd.read_csv("/Users/arthurtena/Documents/application_meteo/data/weather.csv")

# Afficher les premières lignes du DataFrame pour vérifier les données
#print(data.head())
#col_name=data.columns

#Afficher les données pertinantes :
#data=data.drop(columns=['elevation','utc_offset_seconds','timezone','timezone_abbreviation'])
#data=data.drop(data.index[0:1])
#print(data.head)

#On crée une fonction qui donne la date et l'heure actuelle 


#On affiche le jour de la semaine 
maintenant = datetime.datetime.now()

# Obtenir le jour de la semaine actuel (en anglais)
jour_semaine = maintenant.strftime('%A')  # Format du jour de la semaine (par exemple : "lundi", "mardi", etc.)

#On rends les jours de la semaine en français
def jour():
    if (jour_semaine=='Monday'):
     return ('Lundi')
    elif (jour_semaine=='Tuesday'):
      return 'Mardi'
    elif (jour_semaine=='Wednesday'):
     return 'Mercredi'
    elif (jour_semaine=='Thursday'):
     return 'Jeudi'
    elif (jour_semaine=='Friday'):
     return 'Vendredi'
    elif (jour_semaine=='Saturday'):
     return 'Samedi'
    else : return 'Dimanche'

#On affecte à chaque jour un chiffre pour pouvoir le retrouver facilement 
correspondance = {
    'Lundi': 1,
    'Mardi': 2,
    'Mercredi': 3,
    'Jeudi': 4,
    'Vendredi': 5,
    'Samedi':6,
    'Dimanche':7
}
j=correspondance.get(jour()) # jour actuelle

def jours():
   if (j==1):
      return(['Lundi', 'Mardi', 'Mercredi', 'Jeudi'])
   elif(j==2):
      return(['Mardi', 'Mercredi', 'Jeudi', 'Vendredi'])
   elif(j==3):
      return(['Mercredi', 'Jeudi', 'Vendredi', 'Samedi'])
   elif(j==4):
      return(['Jeudi', 'Vendredi', 'Samedi', 'Dimanche'])
   elif(j==5):
      return(['Vendredi', 'Samedi', 'Dimanche', 'Lundi'])
   elif(j==6):
      return(['Samedi', 'Dimanche', 'Lundi','Mardi'])
   else : return('Dimanche', 'Lundi','Mardi', 'Mercredi')

print(jours())

#On met l'URL de la clef API pour la retrouver avec requests
url= 'https://api.open-meteo.com/v1/meteofrance?latitude=43.62&longitude=3.86&hourly=temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset&timezone=Europe%2FBerlin'

reponse=requests.get(url)

api_key = 'API météo Montpellier'

# Créez un en-tête avec la clé API
headers = {
    'Authorization': f'Bearer {api_key}'
}
params = {
	"latitude": 52.52,
	"longitude": 13.41,
	"hourly": ["temperature_2m", "relative_humidity_2m", "rain", "wind_speed_10m"],
	"daily": ["temperature_2m_max", "temperature_2m_min", "sunrise", "sunset"],
}

response = requests.get(url, headers=headers, params=params)
if response.status_code == 200:
    # Affichez le contenu de la réponse
    data=response.json()
    def date_heure():
      now=datetime.datetime.now()
      #On formate la date et l'heure
      date_format = now.strftime('%Y-%m-%d')  # Format AAAA-MM-JJ
      heure_format = now.strftime('%H')  # Format HH
      return f"{date_format}T{heure_format}:00" 
    print(date_heure())

    #On crée une matrice qui sera notre tableau à afficher à la fin 
    tab=np.zeros((5,4))
    Tab=pd.DataFrame(tab, index=['Température (en °C)', 'Humidité (en %)', 'Vitesse du vent (en km/h)', 'Précipitation max (en mm)','Sunset/Sunrise '], columns=[jours()[0],jours()[1],jours()[2], jours()[3]])
    #On classe toutes nos données et on en fait des listes de par jour
    time=data[0]['hourly']['time']
    time=list(chunked(time, 24))
    temp=data[0]['hourly']['temperature_2m']
    temp=list(chunked(temp, 24))
    humidity=data[0]['hourly']['relative_humidity_2m']
    humidity=list(chunked(humidity, 24))
    wind=data[0]['hourly']['wind_speed_10m']
    wind=list(chunked(wind, 24))
    precipitation=data[0]['hourly']['precipitation']
    precipitation=list(chunked(precipitation, 24))
    temp_max=data[0]['daily']['temperature_2m_max']
    temp_min=data[0]['daily']['temperature_2m_min']
    Tab.iat[0,1]=[temp_max[1],temp_min[1]]
    Tab.iat[0,2]=[temp_max[2],temp_min[2]]
    Tab.iat[0,3]=[temp_max[3],temp_min[3]]
    sunrise=data[0]['daily']['sunrise']
    sunset=data[0]['daily']['sunset']
    Tab.iat[4,0]=[sunset[0],sunrise[0]]
    Tab.iat[4,1]=[sunset[1],sunrise[1]]
    Tab.iat[4,2]=[sunset[2],sunrise[2]]
    Tab.iat[4,3]=[sunset[3],sunrise[3]]

    


else:
    print('La requête a échoué avec le code d\'état :', response.status_code)



