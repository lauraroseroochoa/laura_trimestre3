notas=[]
suma=0
cont=0
max_nota=0
min_nota=1000
for i in range(5):
    nota=(int(input(f'Ingrese las notas del alumno {i+1}: ')))
    notas.append(nota)
    cont+=1
    if  nota>max_nota:
      max_nota=nota
    elif nota< min_nota:
      min_nota=nota
print('las notas son: ',notas)

for nota in notas:
    suma+=nota    

def Media(sum1,con):
    x= int((sum1)/con)
    print('la media de las notas es: ',x)

Media(suma,cont)
print('la nota maxima del alumno es: ',max_nota)
print('la nota minima del alumno es: ',min_nota)





