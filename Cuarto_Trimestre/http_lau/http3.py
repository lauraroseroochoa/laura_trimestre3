import requests
import json

url = "https://httpbin.org/get"
response = requests.get(url)
print(response.content.decode)
print(type(response.content.decode()))
#dict = {response.content.decode()}
#print(dict)
#print(type(dict))

json_response = json.loads(response.content)
print(type(json_response))
print(json_response)
for i in json_response.keys():
    print(i)
    for j in json_response[i].keys():
        print(j)