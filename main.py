'''
Categorias disnponiveis: business entertainment generalhealth science sports technology
'''
#title and url

#Import modules
import os
import json
import requests
from dotenv import load_dotenv

#Load API key
load_dotenv()
api_key = os.getenv("API_KEY")

#Request
url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
response = requests.get(url)

#Data JSON
data = response.json()

#Verification of status request and web scraping
#The API that news in key "articles"
if response.status_code == 200:
    articles = data.get('articles', [])
    
    for element in articles:
        title = element.get('title')
        url = element.get('url')
        
        print(f"Title: {title}\nLink: {url}\n{'-'*30}")
else:
    print(f"\nError {response.status_code}\n")