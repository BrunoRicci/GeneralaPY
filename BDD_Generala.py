# Funciones par operar con la base de datos. Creación de partidas (tablas con la fecha actual), lectura de partidas (buscar tablas
# existentes y ver el contenido), lectura y escritura de puntajes en partidas.

import sqlite3
import sys          # Para obtener el directorio actual, y para acceder a la hora.

def CrearTabla (tabla, nombre):
    #Crea base de datos con el nombre asignado



directorio_local= str(sys.path[0])          # Directorio local donde se aloja el programa.
nombre_archivo_bdd= 'BDD_Generala.db'       # Nombre del archivo de la BDD

bdd=sqlite3.connect(directorio_local+'\\'+nombre_archivo_bdd)    # Accede a la base de datos.
bdd_actual = bdd.cursor()   #Asigna el cursor.

print('bdd = '+str(directorio_local+'\\'+nombre_archivo_bdd))
print('bdd = '+str(bdd))


bdd_actual.execute('SELECT * FROM "PARTIDA"')

print('Contenido BDD:\n\n'+str(bdd_actual.fetchall()))  #Lee toda la tabla


