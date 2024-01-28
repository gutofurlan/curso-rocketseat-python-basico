#instala a request via pip
#pip3 install requests==2.31.0

print("\n import e uso um modulo de terceiro")
import requests

url = "https://www.example.com"
response = requests.get(url)
print("STATUS RETORNO:", response.status_code)