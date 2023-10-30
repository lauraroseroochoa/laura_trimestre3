import requests
import json

url="https://httpbin.org/post"#?nombre=juan&documento=12345" ***Esta es una forma de pasarle argumentos 
argumentos={
    'documento': "12345",    # esta es otra froma de pasarle argumentos al post directamente desde un diccionario
    'nombre': "laura"
}
response=requests.post(url, params=argumentos)   # desde python puedo tener acceso a la informacion de la url y con el post aparecen nuevos parametros
response=requests.post(url, json=argumentos)  # se cambia el parametro para tener mas segura la informacion 
#print(response.content.decode())
decodetest=response.content.decode()
print(type(decodetest))
print(response.json())
print('*'*20)
decodetestjson=json.loads(response.content)
print(decodetestjson)
print('*'*20)
print(decodetest)