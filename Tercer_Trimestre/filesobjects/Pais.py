class Pais:
    def __init__(self,name_pais,altura,poblacion,superficie):
        self.__name_pais= name_pais
        self.__altura=altura
        self.__poblacion=poblacion
        self.__superficie=superficie
    def info(self):
        return f"{self.__name_pais} {self.__altura} {self.__poblacion} {self.__superficie}"

    def getNombrePais(self):
        return self.__name_pais

    def getAltura(self):
        return self.__altura

    def getPoblacion(self):
        return self.__poblacion

    def getSuperficie(self):
        return self.__superficie
    
    def sumaSuperficie(self,):
        self.__superficie
        sum=0
        for x in lista:
            sum+=x
            return sum

    def promedioLista(lista):
        return sumaLista(lista)/len(lista)