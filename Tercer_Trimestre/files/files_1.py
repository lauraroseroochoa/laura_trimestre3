import os 
stream = open("tercer_trimestre\\files\\prueba.txt", "r")
print(stream.read())

cadena='1234'
if cadena==True:
    print('llena')
else: 
    print('vacia')
    
#tarea
from os import strerror

try: 
    flujo= open("tercer_trimestre\\files\\prueba.txt", 'r', encoding='utf-8')
    stream=flujo.readline()
    for s in flujo:
        if s != '':
            stream+=1
            print(flujo.readline())
        
except IOError:
    print('error')    
    
flujo= open("tercer_trimestre\\files\\prueba.txt", 'r', encoding='utf-8')    
lista=flujo.readlines()
print(len(lista))
print('lista')
