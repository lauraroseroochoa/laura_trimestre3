def base(funcion):
    print('Inicia la funcion base')
    def interna():
        funcion()
    print('Finaliza la funcion base')
    return interna

#def integrada(parametro):
    #print(f'{parametro} de la funcion integrada')

def integrada():
    print('funcion integrada')    

def otra_funcion():
    print('otra funcion')  

var1=base(integrada)
var2=base(otra_funcion)
var1()
var2()