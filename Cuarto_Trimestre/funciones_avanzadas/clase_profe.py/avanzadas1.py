def suma(n1,n2): # funcion para sumar dos numeros
    return n1+n2

def resta(n1,n2): # funcion para resta dos numeros
    return n1-n2

def producto(n1,n2): # funcion para multiplicar dos numeros
    return n1*n2

def division(n1,n2): # funcion para division de dos numeros
    return n1/n2

def operacion(funcion,numero1,numero2): # funcion que tiene como parametro una funcion y dos valores
    print(funcion(numero1,numero2))# la funcion imprime la funcion que se usara y los valores 

operacion(suma,10,5) # se llama la fucion principal y se da una de las funciones anteriores como parametro con sus dos valores
