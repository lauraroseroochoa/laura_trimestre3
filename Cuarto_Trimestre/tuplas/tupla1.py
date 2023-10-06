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
            for palabra in palabras:
                if palabra == cadena:
                num_aparece += 1
            print(f"La cadena '{cadena}' aparece {num_aparece} veces")
        case '2':
            cadena1=(input('Ingrese una cadena de texto: '))
            cadena_new=(input('Ingrese una cadena de texto nueva: '))
            for i, palabra in enumerate(palabras):
                if palabra == cadena1:
                    palabras[i] = cadena_new
        case '3':  
            cadena = input("Introduce la cadena a eliminar: ")
            palabras = tuple(palabra for palabra in palabras if palabra != cadena)
        case '4': 
        print("La lista es:")
        for palabra in palabras:
            print(palabra)
        case '5':
        break 