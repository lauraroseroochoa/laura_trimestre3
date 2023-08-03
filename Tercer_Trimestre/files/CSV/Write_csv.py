import csv 
header=['Fruit','Price']
rows=[['Apple',1200],
      ['Berry',2000],
      ['Lemon',1000],
      ['Melon',3000],
      ['Grapes',4000],
      ['Pear',2000]]

with open ('files/example.csv','w',newline='') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(header)
    csvwriter.writerows(rows)
    
    ##################################################
import csv
diccio=[
    {'name':'Alice','age':18},
    {'name':'Bob','age':19},
    {'name':'John','age':17}
]
header=['name','age']

with open('files/people.csv','w',newline='') as csvfile:
    writer=csv.DictWriter(csvfile,fieldnames=header)
    writer.writeheader()
    writer.writerows(diccio)