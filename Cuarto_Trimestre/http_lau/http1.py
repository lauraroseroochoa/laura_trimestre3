import requests
url = "https://httpstat.us/505"
response = requests.get(url)
print('sfdfffffffffff',response.status_code)
if response.status_code >= 200 and response.status_code <= 300:
    print(response.content)
elif response.status_code >= 300 and response.status_code <= 400:
    print('redireccion')
elif response.status_code >= 400 and response.status_code <= 500:
    print('error cliente')
elif response.status_code >= 500 :
    print('error em el servidor')
