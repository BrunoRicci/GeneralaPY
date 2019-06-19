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

def EscribirTabla (bdd,nombre,lista):
    #Crea un registro y escribe una lista de datos ordenados en el mismo.

    print('DEBUG: lista = ' + str(lista))
    # print('DEBUG: lista[0] = ' + str(lista[0]))
    # print('DEBUG: lista[-1] = ' + str(lista[-1]))

    if len(lista) == 14:
        #bdd.execute()
        bdd.execute("""
        INSERT INTO """ '\''+str(nombre)+'\''""" ('ID','Turno','Nombre','Uno','Dos','Tres','Cuatro','Cinco','Seis','Escalera','Full','Poker','Generala','2Generala') VALUES
        """+ str(lista) + ';' """
        """)

        bdd_actual.commit()



def IniciarBDD (directorio, nombreBDD):
    #Recibe el directorio y el nombre de la base de datos.

    #nombreBDD = 'BDD_Generala.db'  # Nombre del archivo de la BDD
    #directorio = str(sys.path[0])  # Directorio local donde se aloja el programa.

    bdd = sqlite3.connect(directorio + '\\' + nombreBDD)  # Accede a la base de datos.

    # print('bdd = ' + str(directorio + '\\' + nombreBDD))
    # print('bdd = ' + str(bdd))

    return bdd



directorio_local= str(sys.path[0])          # Directorio local donde se aloja el programa.

bdd_actual=IniciarBDD(directorio_local, 'BDD_Generala.db')  #Se conecta a la base de datos.
bdd_cursor= bdd_actual.cursor()  # Asigna el cursor.

nombre_partida='Partida_1'

# CrearTabla(bdd_actual,nombre_partida)
#
# EscribirTabla(bdd_cursor,'Partida_1',tuple([1,'BRUNO',1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]))
#
# LeerTabla(bdd_cursor,nombre_partida)
# print('Contenido BDD:\n\n'+str(bdd_cursor.fetchall()))  #Lee toda la tabla
