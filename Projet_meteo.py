from tkinter import *
import tkinter as TK
from datetime import *
import requests 
import pytz
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from PIL import Image, ImageTk
app=Tk()
app.title("Prévisions météorologiques de Montpellier") # on choisit le nom de l'application
app.geometry("750x350") # on choisit la taille de l'application 
app.configure(bg="#87CEFA") #on choisit la couleur bleue ciel du fond 

image_icone=PhotoImage(file="/Users/arthurtena/projet_meteo/Images/sunny_sun_cloud_weather_cloudy_icon_194237.png")
app.iconphoto(False,image_icone)

app.mainloop()


