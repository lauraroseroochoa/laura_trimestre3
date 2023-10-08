# escriba un programa que imprima la suma y el promedio de una serie de numeros independientes
def suma_prom(*args):
    suma=0
    cont=0
    for i in args:
        cont+=1
        suma+=i   
        return suma
    x= int((suma)/cont)
    return x


print(suma_prom(4,8,8,1))