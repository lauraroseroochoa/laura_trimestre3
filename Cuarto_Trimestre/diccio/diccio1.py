precio_Frutas = {
    "manzana": 0.55,
    "plátano": 0.75,
    "pera": 0.85,
    "naranja": 0.95,
    "sandía": 1.25,
}
nombre_fruta = input("Introduce el nombre de la fruta: ")
precio = float(input("Introduce el precio de la fruta: "))
cantidad = float(input("Introduce la cantidad vendida: "))

if nombre_fruta in precio_Frutas:
    precio_final = precio * cantidad
    print("El precio final de la fruta {} es de {} €".format(nombre_fruta, precio_final))

else:
    precio_Frutas[nombre_fruta] = precio
    precio_final = precio * cantidad
    print("La fruta {} no existe en el diccionario, pero se añadedo con el precio {} ".format(nombre_fruta, precio))

continuar = input("¿Quieres hacer otra consulta? (si/no): ")

while continuar == "si":

    nombre_fruta = input("Introduce el nombre de la fruta: ")

    precio = float(input("Introduce el precio de la fruta: "))

    cantidad = float(input("Introduce la cantidad vendida: "))

    if nombre_fruta in precio_Frutas:
        precio_final = precio * cantidad
        print("El precio final de la fruta {} es de {} €".format(nombre_fruta, precio_final))

    else:
        precio_Frutas[nombre_fruta] = precio
        precio_final = precio * cantidad
        print("La fruta {} no existe en el diccionario, pero se ha añadido con el precio {} €".format(nombre_fruta, precio))

    continuar = input("¿Quieres hacer otra consulta? (si/no): ")