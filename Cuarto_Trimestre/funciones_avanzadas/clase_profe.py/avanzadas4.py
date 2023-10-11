def base(funcion): # se declara la funcion con el argumento a usar que seria una funcion ya que python las toma como ciudadanos de primera clase
    #print('Inicia la función base')
    def interna(n1,n2): # funcion dentro de la funcion base con dos parametros
        #print(funcion(n1,n2))#*
        return funcion(n1,n2) # se retorna la funcion que se da como parametro en la base 
    #print('Finaliza la función base')
    return interna # se retorna la funcion interna que contiene la funcion

def suma(num1,num2):
    return num1+num2

def resta(num1,num2):
    return num1-num2

@base
def multiplicar(num1,num2):
    return num1*num2

var1=base(suma)
var2=base(resta)
#var1(10,15)#*
#var2(15,10)#*
var1(10,15)
var2(15,10)
multiplicar(4,8)