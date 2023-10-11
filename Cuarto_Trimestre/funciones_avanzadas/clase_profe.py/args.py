# def suma(num1,num2):
#     return num1+num2
#     #print(num1+num2)
# funciones con args: son una convencion que devuelve una tupla
def suma(*args):  # *:representa un desempaquetador para la convencion de args, es el parametro de la funcion suma
    print(type(args)) # imprime el tipo de dato que es args

def mayor(*args): # se declara la funcion mayor con el parametro args
    m=0 # se inicializa una variable
    for i in args:# Inicio del bloque for, con la variable i que va recorrer la tupla de args
        if i>m: # condicion, si la variable i es mayor que la variable m que se inicio antes
            m=i # la variable almacenara el valor mayor que contenga i
    return m # se retorna la variable m que contiene el valor de i

print(mayor(10,23,21,100,1000,1,2,3)) # se imprime la funcion y se pasa como argumento una serie de numeros

#suma(10,23,21)
#suma('hola',122,[],{})