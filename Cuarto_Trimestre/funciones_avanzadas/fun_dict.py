def function(**kwargs):
    for key in kwargs.keys():
        print('clave: ',key)

    for key,value in kwargs.items(): #clave valor usando .items, mostrar solo valores usando .values
        print(f'{key}:{value}')
        
def function2(**kwargs):
    for key in kwargs.keys():
        print('valor: ',kwargs[key])
     
function(programa='adso', ficha=2693629,aprendices=16)
function2(programa='adso', ficha=2693629,aprendices=16)