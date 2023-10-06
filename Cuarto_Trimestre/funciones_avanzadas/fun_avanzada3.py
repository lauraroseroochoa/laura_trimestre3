def base(x):
    def interior(y):
        return x+y
    return interior


UsoFuncionRetornada=base(10)
print(UsoFuncionRetornada(20))


def base(x):
    def suma(y):
        return x+y
    def resta(y):
        return x-y
    return [suma,resta]


UsoFuncionRetornada=base(10) # le estoy asignando una direccion de memoria
print(UsoFuncionRetornada[1](20))
