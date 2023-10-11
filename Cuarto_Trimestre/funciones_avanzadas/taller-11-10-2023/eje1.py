import random

def decorador(funcion):
    print('inicio')
    def envolvente(*args, **kwargs):
      
        return funcion(*args, **kwargs)
      
    return envolvente

@decorador
def lista():
    try:
      lista = [random.randrange(0, 100) for i in range(1, 30)]
    except NameError:
        print('Error:el valor introducido no compatible a (100)')
    return lista

@decorador  
def sumaLista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum

@decorador
def promedioLista(lista):
    return sumaLista(lista)/len(lista)

@decorador
def moda(lista):
    Moda = None
    Cantidad = 0
    for index, numero in enumerate(lista):
        cantidadVecesAparece = lista.count(numero)
        if cantidadVecesAparece > Cantidad:
            Cantidad = cantidadVecesAparece
            Moda = numero
    return Moda

@decorador
def ordenar_lista(lista):
    for i in range(len(lista)):
        min_index = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista 

@decorador
def mediana(lista):
    data = sorted(lista)
    index = len(data) // 2    
    if len(lista) % 2 != 0:
        return data[index]
    return (data[index - 1] + data[index]) / 2

@decorador
def varianza(lista):

    media = sum(lista) / len(lista)
    sumacuadrados = sum((x - media) ** 2 for x in lista)
    varianza = sumacuadrados / len(lista)
    
    return varianza

@decorador
def desviacionestandar(lista):
    resta = []
    elevado = []
    s = 0
    tam = len(lista)

    for i in lista: 
        y = ((i - mediana(lista)) ** 2)
        elevado.append(y) 
    for j in elevado: 
        s += j 
    diviv = (s / (tam - 1)) 
    
    ds = diviv ** 0.5
    return ds


num = lista()
print(num)
print(sumaLista(num))
print(promedioLista(num))
print(moda(num))
print(ordenar_lista(num))
print(mediana(num))
print(varianza(num))
print(desviacionestandar(num))
print(desviacionestandar(num))
