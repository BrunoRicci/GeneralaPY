# Funciones par operar con la base de datos. Creación de partidas (tablas con la fecha actual), lectura de partidas (buscar tablas
# existentes y ver el contenido), lectura y escritura de puntajes en partidas.

import sqlite3
import sys          # Para obtener el directorio actual, y para acceder a la hora.

def CrearTabla (bdd, nombre):
    #Crea anotador (tabla) de puntaje en una base de datos, con el nombre dado.

   bdd.execute("""
        CREATE TABLE IF NOT EXISTS """ '\'' + str(nombre) + '\'' """ (
    	'ID' INTEGER PRIMARY KEY AUTOINCREMENT,
    	'Turno' INTEGER,
    	'Nombre' TEXT,
    	'Uno' INTEGER,
    	'Dos' INTEGER,
    	'Tres' INTEGER,
    	'Cuatro' INTEGER,
    	'Cinco' INTEGER,
    	'Seis' INTEGER,
    	'Escalera' INTEGER,
    	'Full' INTEGER,
    	'Poker' INTEGER,
    	'Generala' INTEGER,
    	'2Generala' INTEGER
        );
                    """)

def LeerTabla (bdd, nombre):
    bdd.execute('SELECT * FROM '+str(nombre))

def EscribirTabla (bdd,lista):
    #Crea un registro y escribe una lista de datos ordenados en el mismo.

    #"INSERT INTO " + '\'' +str(nombre)+ '\' + ({,,,TABLA ORDENADA,,,}) VALUES ()  '
    a=0

directorio_local= str(sys.path[0])          # Directorio local donde se aloja el programa.
nombre_archivo_bdd= 'BDD_Generala.db'       # Nombre del archivo de la BDD

bdd=sqlite3.connect(directorio_local+'\\'+nombre_archivo_bdd)    # Accede a la base de datos.
bdd_actual = bdd.cursor()   #Asigna el cursor.

print('bdd = '+str(directorio_local+'\\'+nombre_archivo_bdd))
print('bdd = '+str(bdd))

nombre='Partida_1'

CrearTabla(bdd_actual,nombre)

LeerTabla(bdd_actual,nombre)

print('Contenido BDD:\n\n'+str(bdd_actual.fetchall()))  #Lee toda la tabla
