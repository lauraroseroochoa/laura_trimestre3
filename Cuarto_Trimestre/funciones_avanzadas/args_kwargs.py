def funcion(*args, **kwargs):
    for elem in args:
        print(elem)
    
    for key,value in kwargs.items():
        print(f'{key}:{value}')

funcion((1,2,3,4),hola='bye')