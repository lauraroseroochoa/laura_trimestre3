import random

def Llenar_list():
    tam=(random.randint(5,10))
    lista=[(random.randrange(100))for i in range (tam)]
    return lista

def Sumar_elementos(lista):
    suma=0
    #tam=Llenar_list
    for i in lista:
        suma+=i
    return suma


def menor_list(lista):
    min_lista=10000
    for i in lista:
        if i<min_lista and i!=0: 
            min_lista = i
    return min_lista
    
    
def mayor_list(lista):
    mayor=0
    for i in lista:
        if  i>mayor:
           mayor=i
    return mayor

def operacion(funcion):
    print(funcion)  

listaa=Llenar_list()  
print(listaa)

operacion(Sumar_elementos(listaa))
operacion(menor_list(listaa))
operacion(mayor_list(listaa))
