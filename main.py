#Nao commitar até ter total segurança e deixar claro no README
# que dev-se criar uma conta no site e colocar link do NEwsAPI, 
# e basta clonar o repositorio e por sua propria api key

#Organizar os dados, primeiro usar a formataçao de strings junto ao beautigul soup

#Categorias disnponiveis: business entertainment generalhealth science sports technology

#Import modules
import requests
from dotenv import load_dotenv

load_dotenv("test.env")

#tlvz tenha que importar os e pegar a api key de forma segura do arquivo .env

#Input

#Request
url = "https://newsapi.org/v2/everything?q=bitcoin&apiKey=API_KEY"
response = requests.get(url)

if response.status_code == 200:
    print("Request successful")
    print(response.json())
else:
    print("Error 404")