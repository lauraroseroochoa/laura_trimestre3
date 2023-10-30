def ip (funcion):
    def ipconfig (*args):
        if validacion(args) == True:
            return(funcion(args))
    return ipconfig

def conversion (args):
    tupla = ()
    for i in args:
        lista = []
        suma = 0
        numero = ""
        for h in i:
            if not (h == "."):
                lista.append(h)
            else:
                suma += 1 
                if suma == 3:
                    lista.append(h)
        for z in lista:
            numero += z
        tupla += (float(numero) ,)
    return tupla

def validacion (args):
    if not (len(args) > 1): 
        for i in args:
            args = i
    direc = []
    for i in args:
        octeto = ""
        for h in i:
            if h == ".":
                direc.append(int(octeto))
                octeto = ""
            else:
                octeto += h
        direc.append(int(octeto))
    try:
        for i in direc:
            if not(i >= 0 and i <= 255):
                raise ValueError
        return True
    except ValueError:
        print("El ip ingresada no es valida")

@ip
def ip_class (args):
    validar = False
    if not (len(args) > 1): 
        for i in args:
            args = i
            validar = True
    tupla = conversion (args)
    lista = []
    for i in tupla:
        if i > 0.0 and i < 127255255.255:
            if validar == True:
                lista.append ("Clase A")
            else:
                print(f"{i} es de Clase A (redes grandes)")
        elif i > 12800.0 and i < 191255255.255:
            lista.append ("Clase B")
            print(f"{i} es de Clase B (redes medianas)")
        elif i > 19200.0 and i < 2232515255.255:
            if validar == True:
                lista.append ("Clase C")
            else:
                print(f"{i} es de Clase C (redes pequeñas)")
        elif i > 22400.0 and i < 239255255.255:
            if validar == True:
                lista.append ("Clase D")
            else:
                print(f"{i} es de Clase D (Multicast)")
        elif i > 22400.0 and i < 255255255.255:
            if validar == True:
                lista.append ("Clase E")
            else:
                print(f"{i} es de Clase E (Investigacion)")
        else:
            print(False)
    return lista

@ip
def ip_host (args):
    tupla = conversion (args)
    for i in tupla:
        if i > 0.0 and i < 127255255.255:
            print(f"{i} puede direccionar 16.777.214")
        elif i > 12800.0 and i < 191255255.255:
            print(f"{i} puede direccionar 65.534")
        elif i > 19200.0 and i < 223255255.255:
            print(f"{i} puede direccionar 254")
        elif i > 22400.0 and i < 239255255.255:
            print(f"{i} no aplica")
        elif i > 22400.0 and i < 255255255.255:
            print(f"{i} no aplica")
        else:
            print(False)     

@ip
def ip_priv_publi (args):
    tupla = conversion (args)
    for i in tupla:
        if i > 10000000.0 and i < 10255255.255 or i > 17216000.0 and i < 17232255.255 or i> 192168000.0 and i < 192169255.255:
            print(f"{i} IP PRIVADA")
        else:
            print(f"{i} IP PUBLICA")


@ip
def ip_subnetting (args):
    lista = ip_class(args)
    for i in lista:
        if i == "Clase A":
            print("La mascara en decimal es: 255.0.0.0")
            print("La mascara en CIDR es: /8")
        elif i == "Clase B":
            print("La mascara en decimal es: 255.255.0.0")
            print("La mascara en CIDR es: /16")
        elif i == "Clase C":
            print("La mascara en decimal es: 255.255.255.0")
            print("La mascara en CIDR es: /24")
        elif i == "Clase D":
            print("La mascara en decimal es: 255.255.255.255")
            print("La mascara en CIDR es: /32")
        elif i == "Clase E":
            print("La mascara en decimal es: 255.255.255.255")
            print("La mascara en CIDR es: /32")
        
        
ip_class("127.88.5.5" , "20.14.50.30")
ip_host("127.88.5.5" , "20.14.50.30")
ip_priv_publi("172.31.255.255","192.168.255.255")
ip_subnetting("127.88.5.5" , "20.14.50.30")