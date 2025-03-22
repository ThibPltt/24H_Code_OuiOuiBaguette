import requests

url = "http://my-json-server.typicode.com/rtavenar/fake_api/tasks"

reponse = requests.get(url)
print(reponse)