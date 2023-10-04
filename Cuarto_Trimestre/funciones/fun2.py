print('menu principal')
def CantSec(h,m,s):
    result= h*3600 + m * 60 + s
    print('el valor del tiempo en segundos es: ',result)


def CantHMS(s):
    h= s//3600
    s= s % 3600
    m= s//60
    s= s%60
    print('el valor de los segundos en horas, minutos y segundos es: ',h,m,s)


while True:
    print('1-Convertir a segundos')
    print('2-Convertir a horas, minutos y segundos')
    print('3-salir')

    selector=(input('Digite la opcion: ')) 
    match selector:
        case '1': 
            hora=int(input('Ingrese el numero de la hora: '))
            minutos=int(input('Ingrese el numero de minutos: '))
            segundos=int(input('Ingrese el numero de segundos: '))
            CantSec(hora,minutos,segundos)
        case '2':
            second=int(input('Ingrese el numero de segundos: ')) 
            CantHMS(second)
        case '3':  
            break
