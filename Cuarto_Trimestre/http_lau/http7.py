import requests
url="http://api.github.com/users"
sesion=requests.session()
sesion.auth=('lauraroseroochoa','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')
response=sesion.get(url)

if response.status_code == 200:
    response1=sesion.get('http://github.com/lauraroseroochoa')
    print(response1.cookies)
    print(response.content)
