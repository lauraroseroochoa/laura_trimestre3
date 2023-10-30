import requests
url="http://api.github.com/users"
sesion=requests.session()
sesion.auth=('lauraroseroochoa','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')
response=sesion.get(url)

if response.status_code == 200:
    response1=sesion.get('http://github.com/lauraroseroochoa')
    print(response1.cookies)
    print(response.content)
