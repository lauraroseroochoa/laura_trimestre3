import math
def ecuacion_Cuadratica():
    try:
        a= int(input('ingresa el valor  de A para la ecuacion: '))
        b= int(input('ingresa el valor de B para la ecuacion: '))
        c= int(input('ingresa el valor de C para la ecuacion: '))
        x1= -b + math.sqrt(b**2 - 4 * a * c)/ 2 * a
        x2= -b - math.sqrt(b**2 - 4 * a * c)/ 2 * a
        if a == 0:
             raise ZeroDivisionError
        print ('la forma positiva de funcion es:',x1)
        print ('la forma negativa de funcion es:',x2)
    except ValueError:
        print('ingresa un valor valido para el programa')
    except ZeroDivisionError:
        print('No se puede dividir por cero')
    except TypeError:
        print('el numero debe ser positivo')
        
    except KeyboardInterrupt:
        print('se interrumpio el programa')
    except:
        print('Ocurrio un Error')
        
#ecuacion_Cuadratica(1,5,4)
ecuacion_Cuadratica()