def suma(num1,num2):
    x=num1+num2
    return x
def resta(num1,num2):
    x=num1-num2
    return x
def producto(num1,num2):
    x=num1*num2
    return x
def division(num1,num2):
    x=num1/num2
    return x

def operacion(funcion,numero1,numero2):
    print(funcion(numero1,numero2))

suma(1,6)
resta(8,8)
producto(3,3)
division(10,2)
operacion(resta,14,3)