palabras=('go','run','love')

while True:
    print('1-Contar')
    print('2-modificar')
    print('3-eliminar')
    print('4-Mostrar')
    print('5-Salir')


    selector=(input('Digite la opcion: ')) 
    match selector:
        case '1': 
            cadena=(input('Ingrese una cadena de texto: '))
            num_aparece=0
        case '2':
            cadena1=(input('Ingrese una cadena de texto: '))
            cadena=(input('Ingrese una cadena de texto: '))
        case '3':  
            break