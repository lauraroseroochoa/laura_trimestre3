def cont_caracteres(file):
    with open(file, 'r') as fileread:
      cont_caracter = 0
      linea = fileread.read()
      for letras in linea:
          print(letras, end='')
          cont_caracter += 1
      print(f'caracteres: {cont_caracter} en el archivo')        

cont_caracteres('laura.txt')

def cont_lineas(file):
  with open(file, 'r') as fileread:
      cont_linea = 0
      linea = fileread.readline()
      while linea != '':
        cont_linea += 1
        linea = fileread.readline()
      print(f'numero lineas: {cont_linea} en el archivo')
    
cont_lineas('laura.txt')