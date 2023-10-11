

def clases_ip(ip):
    lista = []
    cifras = ""
    for caracter in ip:
        if caracter == ".":
            lista.append(int(cifras))
            cifras = ""
        else:
            cifras += caracter
    lista.append(int(cifras)) 
    print(lista)
    rango_1 = (0, 127)
    rango_2 = (0,255)
    rango_3 = (0,255)
    rango_4=(0, 255) 
    rango_5=(128,191)
    rango_6=(192,223)
    rango_7=(224,239)
    rango_8=(240,255)
    if (rango_1[0] <= lista[0] <= rango_1[1] and
        rango_2[0] <= lista[1] <= rango_2[1] and
        rango_3[0] <= lista[2] <= rango_3[1] and
        rango_4[0] <= lista[3] <= rango_4[1]):
        print('La dirección IP es clase A')
        
    if (rango_5[0] <= lista[0] <= rango_5[1] and
        rango_2[0] <= lista[1] <= rango_2[1] and
        rango_3[0] <= lista[2] <= rango_3[1] and
        rango_4[0] <= lista[3] <= rango_4[1]):
        print("La dirección IP es clase B")
    if (rango_6[0] <= lista[0] <= rango_6[1] and
        rango_2[0] <= lista[1] <= rango_2[1] and
        rango_3[0] <= lista[2] <= rango_3[1] and
        rango_4[0] <= lista[3] <= rango_4[1]):
        print("La dirección IP es clase C")
    if (rango_7[0] <= lista[0] <= rango_7[1] and
        rango_2[0] <= lista[1] <= rango_2[1] and
        rango_3[0] <= lista[2] <= rango_3[1] and
        rango_4[0] <= lista[3] <= rango_4[1]):
        print("La dirección IP es clase D")
    if (rango_8[0] <= lista[0] <= rango_8[1] and
        rango_2[0] <= lista[1] <= rango_2[1] and
        rango_3[0] <= lista[2] <= rango_3[1] and
        rango_4[0] <= lista[3] <= rango_4[1]):
        print("La dirección IP es clase E")
    
    
def publi_priv(ip):
    lista = []
    cifras = ""
    for caracter in ip:
        if caracter == ".":
            lista.append(int(cifras))
            cifras = ""
        else:
            cifras += caracter
    lista.append(int(cifras)) 
    rango_1 = (1,126)
    rango_2=(128,191)
    rango_3=(192,223)
    rango_4=(10,10)
    rango_5=(172,172)
    rango_6=(16,31)
    rango_7=(192,192)
    rango_8=(168,168)
    if rango_1[0] <= lista[0] <= rango_1[1]:
        print('La dirección IP es publica A')
    if rango_2[0] <= lista[0] <= rango_2[1]:
        print('La dirección IP es publica B')
    if rango_3[0] <= lista[0] <= rango_3[1]:
        print('La dirección IP es publica C')
    if rango_4[0] <= lista[0] <= rango_4[1]:
        print('La dirección IP es privada A')
    if (rango_5[0] <= lista[0] <= rango_5[1] and
        rango_6[0] <= lista[1] <= rango_6[1]):
        print('La dirección IP es privada B')
    if (rango_7[0] <= lista[0] <= rango_7[1] and
        rango_8[0] <= lista[1] <= rango_8[1]):
        print('La dirección IP es privada C')
    


clases_ip("123.133.12.1")
clases_ip("129.133.12.1")
clases_ip("200.133.12.1")
clases_ip("230.133.12.1")
clases_ip("241.133.12.1")
    
publi_priv("123.133.12.1")
publi_priv("129.133.12.1")
publi_priv("200.133.12.1")
publi_priv("230.10.12.1")
publi_priv("172.13.12.1")
publi_priv("192 .168.12.1") 
