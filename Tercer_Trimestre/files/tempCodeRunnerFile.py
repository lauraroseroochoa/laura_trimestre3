from os import strerror

try: 
    flujo= open("tercer_trimestre\\files\\prueba.txt", 'r', encoding='utf-8')
    stream=flujo.readline()
    for s in flujo:
        if s != '':
            print(flujo.readline())
        
except IOError:
    print('error')    