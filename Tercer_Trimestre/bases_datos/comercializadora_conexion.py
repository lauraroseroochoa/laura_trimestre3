#import mysql.connector
from mysql.connector import *

db_lau= mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='comercializadora'
)
cursor=db_lau.cursor()
cursor.execute('SHOW DATABASES')
for dbs in cursor:
    print(dbs)

lista_lau= []
# cursor.execute("SHOW TABLES")
# for n in cursor:
#     print(n)
    
# cursor.execute("""INSERT INTO sellers (seller_id, name_seller)VALUES (6,'MATEO VARGAS') """)
# db_lau.commit()
# cursor.execute('select * from sellers')
for sel in cursor:
    print(sel)


#cursor.execute("""UPDATE products set desciption='solo productos, info privada' where id_products=1 """)
# db_lau.commit()
cursor.execute('SELECT * FROM  productos')
for sel in cursor:
    print(sel)

#cursor.execute("""DELETE from users where id_user=3 """)
# db_lau.commit()