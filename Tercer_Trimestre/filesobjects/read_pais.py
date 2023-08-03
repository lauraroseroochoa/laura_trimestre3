from Pais import *
import csv
listaPais=[]
with open('C:\\Users\\SENA\\Downloads\\pais.csv', encoding='utf-8') as csvPaisFile:

    csvReader= csv.reader(csvPaisFile)    
    for row in csvReader:
        object_pais=Pais(row[1],row[7],row[3],row[4])
        listaPais.append(object_pais)


#print(listaPais) #aprendices como objetos

for country in listaPais:
    print('name_ country:',country.getNombrePais())
    print('altura:',country.getAltura())
    print('poblacion:',country.getPoblacion())
    print('Superficie:',country.getSuperficie())

