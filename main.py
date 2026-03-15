'''
Organizar os dados, primeiro usar a formataçao de strings junto ao beautigul soup
Categorias disnponiveis: business entertainment generalhealth science sports technology
'''

#Import modules
import os
import requests
from dotenv import load_dotenv

#Load API key
api_key = os.getenv("API_KEY")
load_dotenv()

#Request
url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
response = requests.get(url)

#Verification of status request and web scraping
if response.status_code == 200:
    print("\nRequest successful\n")
else:
    print("\nError 404\n")