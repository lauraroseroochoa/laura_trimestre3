def base(funcion): # se declara la funcion con el argumento a usar que seria una funcion ya que python las toma como ciudadanos de primera clase es decir como objetos
    print('Inicia la función base') # inicia
    def interna(): # la funcion se compone de una funcion interna que a su vez recibe una funcion
        funcion()    
    print('Finaliza la función base')
    return interna # retorna la funcion interna que a su vez contiene una funcion 

# se declaran funciones independientes para usarlas como argumento dentro de la funcion base
def integrada():
    print('Funcion Integrada')

def otraFuncion():
    print('Otra Funcion')

var1=base(integrada)
var2=base(otraFuncion)
var1()
var2()


# def integrada(parametro):
#     print(f'{parametro} de la funcion Integrada')