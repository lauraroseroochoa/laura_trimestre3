def base(funcion): # se declara la funcion base 
    
    def interna(*args,**kwargs):
        print('Inicia la función base')
        print(funcion(*args,*kwargs))#*    # se imprime la funcion que se da como parametro en la base condos parametros   
        #return funcion(n1,n2)
        #funcion(n1,n2)
        print('Finaliza la función base')
    return interna

def suma2(num1,num2):
    return num1+num2

@base
def suma3(num1,num2,num3):
    return num1+num2+num3


def resta(num1,num2):
    return num1-num2

@base
def multiplicar(num1,num2):
    return num1*num2

var1=base(suma2)
var2=base(resta)
#var1(10,15)#*
#var2(15,10)#*
var1(10,15)
var2(15,10)
multiplicar(4,8)
suma3(1,2,3)