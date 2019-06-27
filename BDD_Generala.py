# Funciones par operar con la base de datos. Creación de partidas (tablas con la fecha actual), lectura de partidas (buscar tablas
# existentes y ver el contenido), lectura y escritura de puntajes en partidas.

import sqlite3
import sys          # Para obtener el directorio actual, y para acceder a la hora.


def CrearTabla (bdd, nombre):
    #Crea anotador (tabla) de puntaje en una base de datos, con el nombre dado.
                    # IF NOT EXISTS
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


def LeerTabla (bdd, nombretabla):
    bdd.execute('SELECT * FROM '+str(nombretabla))
    # print('leido: '+str(bdd.fetchall()))

    return( bdd.fetchall() )


def LeerPartidas (bdd):
    # Recibe una base de datos, y busca todas las tablas que hay, devolviendo una lista de las mismas.

    bdd.execute("""
    SELECT name FROM sqlite_master WHERE type = "table";
""")
    # print('Tablas leídas: '+str(bdd.fetchall()))
    return bdd.fetchall()


def EscribirTabla (bdd, nombre, lista):
    #Crea un registro y escribe una lista de datos ordenados en el mismo.

    # print('DEBUG: lista[0] = ' + str(lista[0]))
    # print('DEBUG: lista[-1] = ' + str(lista[-1]))

    if len(lista) >= 13:    #Puede o no tener campo de PK
        lista=tuple(lista)  # Transforma la lista a una tupla, para convertir los corchetes a paréntesis
                            # y hacer así una instrucción compatible ocn la base de datos.
        print('DEBUG: lista = ' + str(lista))

        bdd.execute("""
        INSERT INTO """ '\''+str(nombre)+'\''""" ('ID','Nombre','Turno','Uno','Dos','Tres','Cuatro','Cinco','Seis','Escalera','Full','Poker','Generala','2Generala') VALUES
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

bdd_actual=0 #Indica que no hay BDD abierta
bdd_actual=IniciarBDD(directorio_local, 'BDD_Generala.db')  #Se conecta a la base de datos.
bdd_cursor= bdd_actual.cursor()  # Asigna el cursor.

nombre_partida='Partida_1'



####################### Pruebas ###########################
# LeerPartidas(bdd_cursor)


# EscribirTabla(bdd_cursor,'Partida_1',tuple([1,'BRUNO',1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]))
#
# LeerTabla(bdd_cursor,nombre_partida)
# print('Contenido BDD:\n\n'+str(bdd_cursor.fetchall()))  #Lee toda la tabla
