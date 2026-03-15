'''
Only 'us' is working in request api
'''

#Import modules
import os
import json
import requests
from dotenv import load_dotenv

#Load API key
load_dotenv()
api_key = os.getenv("API_KEY")

#Authentication
if not api_key:
    print("\n⚠️  Atention: the variable 'API_KEY' not found.")
    print("\nCreate a '.env' file with your key of NewsAPI")
    os.exit(1)

print("\nAuthentication validate sucessful.")

#Input user
topic = input("\nWhich topic you want see news?: ").lower().strip()
url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={api_key}"

#Request
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
        description = element.get('description')
        print(f"\n{'-'*30}\n\n{title}\n{description}\n\nLink: {url}")
else:
    print(f"\nError {response.status_code}\n")