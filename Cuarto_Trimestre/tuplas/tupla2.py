y = ()

for i in range(5):
    cadena = input("introduce la cadena de caracteres {}:".format( i + 1))
    y += (cadena,)

inverso = []
for i in range(len(y) - 1, -1, -1):
    inverso.append(y[i])

print("Los elementos de la tupla inversa son:")
for elemento in inverso:
  print(elemento)