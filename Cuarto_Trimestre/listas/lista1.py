precio=[8000,500,10000,400,6000]
cantidad=[0] * 4
sucursal= 4

for i in range(4):
    cantidad[i]=int(input(f'Ingrese la cantidad del producto{i+1}:'))

cant_total= [0]* 5
for i in range(4):
    for j in range(5):
        cant_total[j] += cantidad[i][j]