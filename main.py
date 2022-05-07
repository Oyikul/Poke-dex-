import pypokedex
import PIL.Image , PIL.ImageTk
import tkinter as tk
import urllib3
from io import BytesIO
from bs4 import BeautifulSoup
import requests
#import pyttsx3


window = tk.Tk()
window.geometry("700x600")
window.title("Replit Pokedex")
window.config(padx=10, pady = 10)

title_label = tk.Label(window, text="The POKEDEX on REPLIT")
title_label.config(font=("Arial", 32)) 
title_label.pack(padx=10, pady=10)

pokemon_image = tk.Label(window)
pokemon_image.pack(padx=10, pady=10)

pokemon_info = tk.Label(window)
pokemon_info.config(font=("Arial", 20))
pokemon_info.pack(padx=10, pady=10)


pokemon_types = tk.Label(window)
pokemon_types.config(font=("Arial", 20))
pokemon_types.pack(padx=10, pady=10)

pokemon_description = tk.Label(window)
pokemon_description.config(font=("Arial", 12))
pokemon_description.pack(padx=10, pady=10)

# Uncomment this function only if you are on laptop or computer. Do not uncomment if you are using Replit.

# def speak(audio):
#   engine = pyttsx3.init()
#   engine.say(audio)
#   engine.runAndWait()

def load_pokemon():
  pokemon = pypokedex.get(name=text_id_name.get(1.0, "end-1c"))

  http = urllib3.PoolManager()
  response = http.request('GET', pokemon.sprites.front.get('default'))
  image = PIL.Image.open(BytesIO(response.data))
  
  img = PIL.ImageTk.PhotoImage(image)
  pokemon_image.config(image=img)
  pokemon_image.image = img


  pokemon_info.config(text=f"{pokemon.dex} - {pokemon.name}".title())
  pokemon_types.config(text=" - ".join([t for t in pokemon.types]).title())

    # Assign URL
  url = " https://pokeapi.co/api/v2/pokemon-color/{id or name}/"+text_id_name.get(1.0, "end-1c")
    
  # Fetch raw HTML content
  html_content = requests.get(url).text
    
  # Now that the content is ready, iterate 
  # through the content using BeautifulSoup:
  
  soup = BeautifulSoup(html_content, "html.parser")
    
  # similarly to get all the occurences of a given tag
  
  #print(soup.find('p', attrs={'class': 'version-xactive'}).text)

  description = soup.find('p', attrs={'class': 'version-x active'})
  
  if description:
    pokemon_description.config(wraplength=600, text=description.text)
    print(description.text)
    #speak(pokemon_description) Use this function only if you are on laptop or computer. Do not uncomment if you are using Replit.


label_id_name = tk.Label(window, text="ID or Name")
label_id_name.config(font=("Arial", 20))
label_id_name.pack(padx=10, pady=10)

text_id_name = tk.Text(window, height=1)
text_id_name.config(font=("Arial", 20))
text_id_name.pack(padx=10, pady=10)

btn_load = tk.Button(window, text="Load Pokemon!", command=load_pokemon)
btn_load.config(font=("Arial", 20))
btn_load.pack(padx=10, pady=10)


window.mainloop()