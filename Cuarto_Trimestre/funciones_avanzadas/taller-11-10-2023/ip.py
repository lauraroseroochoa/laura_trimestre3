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
    direc = []
    val = []
    suma = 0
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
    tupla = conversion (args)
    for i in tupla:
        if i > 0.0 and i < 127255255.255:
            print(f"{i} es de Clase A (redes grandes)")
        elif i > 12800.0 and i < 191255255.255:
            print(f"{i} es de Clase B (redes medianas)")
        elif i > 19200.0 and i < 2232515255.255:
            print(f"{i} es de Clase C (redes pequeñas)")
        elif i > 22400.0 and i < 239255255.255:
            print(f"{i} es de Clase D (Multicast)")
        elif i > 22400.0 and i < 255255255.255:
            print(f"{i} es de Clase E (Investigacion)")
        else:
            print(False)

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
        
        
ip_class("127.88.5.5" , "20.14.50.30")
ip_host("127.88.5.5" , "20.14.50.30")
ip_priv_publi("172.31.255.255","192.168.255.255")