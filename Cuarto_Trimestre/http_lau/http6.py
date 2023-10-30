import requests

url = 'https://cdn.pixabay.com/photo/2017/01/14/12/59/iceland-1979445_640.jpg'
response = requests.get(url,stream=True)

with open('noon/download.jpg','wb') as file:
    for pedazo in response.iter_content():    
        file.write(pedazo)