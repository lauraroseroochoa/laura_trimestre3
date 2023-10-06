def base(funcion):
    print('Inicia la funcion base')
    def interna(n1,n2):
        print(funcion(n1,n2)) #linea 20 y 21
        return funcion(n1,n2) #linea 23 y 24
    print('Finaliza la funcion base')
    return interna


def suma(num1,num2):
    return num1+num2

def resta(num1,num2):
    return num1-num2

var1=base(suma)
var2=base(resta)
var1(10,15)
var2(15,20)

print(var1(10,15))
print(var2(15,20))