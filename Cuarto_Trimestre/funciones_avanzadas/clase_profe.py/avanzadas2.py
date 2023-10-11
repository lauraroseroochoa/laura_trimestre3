def base(x): # se define la funcion principal con un parametro
    def suma(y): # declarar una funcion dentro de la funcion base, la cual va a sumar con un parametro
        return x+y # retorna la suma del parametro de la funcion base con el de la funcion suma
        #print(x+y)
    def resta(y): # otra funcion dentro de la base con un parametro
        return x-y # retorna la resta del parametro de la funcion base con el de la funcion resta
    return [suma,resta] # la funcion base retorna una lista para seleccionar suma o resta 

#print(base(1))
usoFuncionRetornada=base(10) # se declara una variable a la que se le asigana la funcion base con el parametro
print(usoFuncionRetornada[1](20)) # se imprime la variable que se declaro antes con la posicion de la lista en la que esta la funcion suma o resta mas el argumento de esa funcion





# def prueba():
#     pass

# print(prueba)

# class Prueba:
#     pass

# x=Prueba()
# print(x)