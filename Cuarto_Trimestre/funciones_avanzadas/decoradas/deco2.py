diccionario={'laura': '123',
             'paula': '456',
             'steven': '789',
             'josue': '101',
             'zully': '222',
             'sebastian':'333'}


def ingresar(funcion):
    def envolvente():
        funcion()

def bienvenida():
    pass


def verificar_usuario(diccio):
    usuario=(input('Ingrese el usuario: '))
    contraseña=(input('Ingrese la contraseña: '))
    for key,value in diccio.items():
        if key==usuario and value==contraseña:
            print('usuario autenticado')
            print(usuario)
    else:
        print('no se encuentra en el sistema')


verificar_usuario(diccionario)