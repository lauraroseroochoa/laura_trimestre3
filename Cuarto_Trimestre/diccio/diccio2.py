resultados={}
NomAlumnos= input("ingrese el nombre del estudiante: ")
NotasAlumno = float (input("ingrese la nota del estudiante: "))

continuar = input("¿Quieres añadir otro alumno? (Si/No): ")
if NomAlumnos in resultados:
   resultados[NomAlumnos].append(NotasAlumno)
else:
    resultados[NomAlumnos] = [NotasAlumno]

while continuar == "Si":
    NomAlumnos = input("Introduce el nombre del alumno: ")

    NotasAlumno= float(input("Introduce la nota del alumno: "))

    resultados[NomAlumnos].append(NotasAlumno)

    continuar = input("¿Quieres añadir otro alumno? (Si/No): ")

for NomAlumnos, NotasAlumno in resultados.items():
    print("el alumno {} tiene como resultado las siguintes notas: {}".format(NomAlumnos, NotasAlumno))