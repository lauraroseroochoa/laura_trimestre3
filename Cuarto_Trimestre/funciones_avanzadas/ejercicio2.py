def calcular_precio_total(*args,**kwargs):
    precio_total=0
    x=0
    for key,value in kwargs.items():
        print(f'clave: {key} : valor: {value}')
    for value in kwargs.values():
        precio_total+=value
    print('el precio total es: ',precio_total)
    for i in args:
        x=i/100
        for value in kwargs.values():
            s=x*value
            desc=s-value
            print(desc)


        


calcular_precio_total((10,20,5),celular=1020000, manzana=1000, arroz=5000)
