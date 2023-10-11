# funcion con parametros args y kwargs
# kwargs: key word crea un diccionario con los argumentos que le pase
def funcion(*args,**kwargs): # ** representa el desempaquetador de kwargs
    for elemento in args: # inicio del bloque for donde la variable recorre la tupla args
        print(elemento) # imprime lo que almacena la variable
    
    for key,val in kwargs.items(): # inico del bloque for que con dos variables que recorre la clave(key) y valor(val) del diccionario kwargs con el metodo .items
        print(f'{key} : {val}') # imprime la clave y el valor que estan en el diccio

funcion(1,2,3,4, fecha='6-10-2023',hora='7:30 am') # llama la funcion y le pasa los argumentos para la tupla y el diccionario

x=100 # variable con un valor
print(isinstance(x,int)) # pregunta si la variable es un numero entero