diccionario={'laura': '123',
             'paula': '456',
             'steven': '789',
             'josue': '101',
             'zully': '222',
             'sebastian':'333'}


def ingresar(funcion):
    def envolvente():
        print(funcion(diccio))
    return envolvente

def bienvenida():
    pass


def verificar_usuario(diccio):
    usuario=(input('Ingrese el usuario: '))
    contraseña=(input('Ingrese la contraseña: '))
    for key,value in diccio.items():
        if key==usuario and value==contraseña:
            print('usuario autenticado')
            print(usuario)
    for key,value in diccio.items():
        if key!=usuario and value!=contraseña:
            print('no se encuentra en el sistema')
            


verificar_usuario(diccionario)