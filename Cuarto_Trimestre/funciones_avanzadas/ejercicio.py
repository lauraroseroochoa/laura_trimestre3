edad=(input('Ingrese la edad: '))
estatura=(input('Ingrese la estatura: '))
peso=(input('Ingrese el peso de la persona: '))

def validar(**kwargs):
    for key,value in kwargs.items():
        print(f'clave: {key} : valor: {value}')
    for key,value in kwargs.items():
        
        if key=='edad':
           value=int(value)
           print(isinstance(value,int))
        else:
           print('no es valido')
        if key=='estatura':
           for i in value:
              if i=='.':
                 value=float(value)
                 print(isinstance(value,float))

        if key=='peso':
           for i in value:
              if i=='.':
                 value=float(value)
                 print(isinstance(value,float))

validar(edad=edad,estatura=estatura,peso=peso)