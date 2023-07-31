def contador_lineas_caracter(file):
    cont_caracter = 0
    cont_lineas = 0
    fileread = open(file, 'rt')
    linea = fileread.readline()
    while linea != '':
        cont_lineas += 1
        for letras in linea:
            print(letras, end='')
            cont_caracter += 1
        linea = fileread.readline()
    fileread.close()
    print("\n numero de caracteres en el archivo: ", cont_caracter)
    print("numero de líneas en el archivo:  ", cont_lineas)
    
contador_lineas_caracter('datos_personales.txt')