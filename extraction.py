import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import requests
import json
import datetime 
from more_itertools import chunked
from IPython.display import display, HTML
#On affiche le jour de la semaine 
maintenant = datetime.datetime.now()

# Calculez la date de fin 
date_fin = maintenant + datetime.timedelta(days=4)

# Formattez les dates au format AAAA-MM-JJ.
date_debut= maintenant.strftime('%Y-%m-%d')
date_fin= date_fin.strftime('%Y-%m-%d')


# Obtenir le jour de la semaine actuel (en anglais)
jour_semaine = maintenant.strftime('%A')  # Format du jour de la semaine (par exemple : "lundi", "mardi", etc.)

#On met l'URL de la clef API pour la retrouver avec requests
url= 'https://api.open-meteo.com/v1/meteofrance?latitude=43.62&longitude=3.86&hourly=temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset&timezone=Europe%2FBerlin'
meteo_url = f'{url}&start_date={date_debut}&end_date={date_fin}'
reponse=requests.get(url)

api_key = 'API météo Montpellier'

# Créez un en-tête avec la clé API
headers = {
    'Authorization': f'Bearer {api_key}'
}
params = {
	"latitude": 52.52,
	"longitude": 13.41,
	"hourly": ["temperature_2m", "relative_humidity_2m", "precipitation", "wind_speed_10m"],
	"daily": ["temperature_2m_max", "temperature_2m_min", "sunrise", "sunset"],
}

response = requests.get(meteo_url, headers=headers, params=params)
if response.status_code == 200:
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
 # Affichez le contenu de la réponse
 data=response.json()
 def date_heure():
    now=datetime.datetime.now()
    #On formate la date et l'heure
    date_format = now.strftime('%Y-%m-%d')  # Format AAAA-MM-JJ
    heure_format = now.strftime('%H')  # Format HH
    return f"{date_format}T{heure_format}:00" 
 time=data[0]['hourly']['time']
 time=list(chunked(time, 24))
 #On classe toutes nos données et on en fait des listes de par jour
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
 sunrise=data[0]['daily']['sunrise']
 sunset=data[0]['daily']['sunset']
 def heure():
    for i in range(24):
       time[0][i]=time[0][i+1]
       a=time[0][i]==date_heure()
       if (a==True):
          return (i)
 Température=[(temp[0][heure()],temp_max[0]),(temp_max[1],temp_min[1]),(temp_max[2],temp_min[2]),(temp_max[3],temp_min[3])]
 Humidité=[(humidity[0][heure()],np.mean(humidity[0])),(np.mean(humidity[1]),np.max(humidity[1])),(np.mean(humidity[2]),np.max(humidity[2])),(np.mean(humidity[3]),np.max(humidity[3]))]
 Vent=[(wind[0][heure()],np.mean(wind[1])),(np.max(wind[1]),np.min(wind[1])),(np.max(wind[2]),np.min(wind[2])),(np.max(wind[3]),np.min(wind[3]))]
 Pluie=[(precipitation[0][heure()],np.mean(precipitation[0])),(np.max(precipitation[1]),np.mean(precipitation[1])),(np.max(precipitation[2]),np.mean(precipitation[2])),(np.max(precipitation[3]),np.mean(precipitation[3]))]
 Soleil=[(sunrise[0],sunset[0]),(sunrise[1],sunset[1]),(sunrise[2],sunset[2]),(sunrise[3],sunset[3])]
 tab=[[Température[i] for i in range(4)],
      [Humidité[i] for i in range(4)],
      [Vent[i] for i in range(4)],
      [Pluie[i] for i in range(4)],
      [Soleil[i] for i in range(4)]
      ]
 Tab=pd.DataFrame(tab,index=['Temperature (en °C)','Humidite (en %)','Vitesse du vent (en km/h)','Precipitation (en mm)','Sunrise/Sunset'],
    columns=[jours()[0],jours()[1],jours()[2], jours()[3]])
 html_Tab = Tab.to_html('meteo.html')
 display(HTML(html_Tab))




 
    

 


 

 

 












