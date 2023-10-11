# ** representa el desempaquetador de kwargs
# se declara la funcion 
# kwargs: key word crea un diccionario 
def function(**kwargs): # se declra la funcion con un diccionario kwargs
    #print(type(kwargs))
    for key in kwargs.keys(): # la variable key pasa por todas las claves del diccionario
        print(key) # se imprimen las claves
    for value in kwargs.values(): # la variable value pasa por todas los valores del diccionario
         print(value) # se imprimen los valores
    for key,value in kwargs.items(): # las variables key y value pasan por todas las claves y valores del diccionario
        print(f'{key} : {value}') # se imprimen clave y valor 


function(programa="adso",ficha=2693629,aprendices=16)




# dict={
#     'programa':'adso',
#     'ficha':2693629,
#     'aprendices':16
# }