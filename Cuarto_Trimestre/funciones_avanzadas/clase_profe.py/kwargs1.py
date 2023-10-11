def validar(**kwargs): # se declara la funcion con el parametro de diccionario
   
    for key,value in kwargs.items(): # inicio del ciclo for donde las variables key y value toman el valor de clave y valor de cada dato del diccionario
        if key=="edad": # condicion para saber si la clave es es igual que la que se da como argumento
            print(isinstance(value,int)) # se imprime en pantalla si el dato que almacena la variable value de la clave edad es instancia de un numero entero
        if key=="peso": # clave es igual al argumento que se le pasa a la funcion
            print(isinstance(value,float)) # se imprime en pantalla si el dato que almacena la variable value de la clave peso es instancia de un numero real
        if key=="estatura":
            print(isinstance(value,float)) # se imprime en pantalla si el dato que almacena la variable value de la clave estatura es instancia de un numero real
  

#validar(edad=15,peso=60.0, estatura=1.60)
#validar(edad='siete',peso='39', estatura='1.39')
validar(edad='34',peso=60, estatura=1.90) # se llama la funcion y se dan los argumentos para el diccionario de kwargs
#print(isinstance(60.0,float))