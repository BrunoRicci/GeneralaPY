# Funciones par operar con la base de datos. Creación de partidas (tablas con la fecha actual), lectura de partidas (buscar tablas
# existentes y ver el contenido), lectura y escritura de puntajes en partidas.

import sqlite3
import sys          # Para obtener el directorio actual, y para acceder a la hora.


def CrearTabla (bdd, nombretabla, tabla_jugadores):
    #Crea anotador (tabla) de puntaje en una base de datos, con el nombre dado.
                    # IF NOT EXISTS
    bdd.execute("""
        CREATE TABLE IF NOT EXISTS """ '\'' + str(nombretabla) + '\'' """ (
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

    for registro in tabla_jugadores:    # Registro: Contiene una columna del anotador (una por jugador).
        EscribirTabla(bdd,nombretabla,registro)


def BorrarTabla (bdd, nombretabla):
    bdd.execute('DROP TABLE '+str(nombretabla)+';')

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


def EscribirTabla (bdd, nombretabla, lista):
    #Crea un registro y escribe una lista de datos ordenados en el mismo.

    # print('DEBUG: lista[0] = ' + str(lista[0]))
    # print('DEBUG: lista[-1] = ' + str(lista[-1]))

    if len(lista) >= 13:    #Puede o no tener campo de PK
        lista=tuple(lista)  # Transforma la lista a una tupla, para convertir los corchetes a paréntesis
                            # y hacer así una instrucción compatible ocn la base de datos.
        print('DEBUG: lista = ' + str(lista))

        bdd.execute("""
        INSERT INTO """ '\'' + str(nombretabla) + '\''""" ('ID','Turno','Nombre','Uno','Dos','Tres','Cuatro','Cinco','Seis','Escalera','Full','Poker','Generala','2Generala') VALUES
        """ + str(lista) + ';' """
        """)

    bdd_actual.commit()


def ModificarTabla (bdd, nombretabla, lista):
    # Recibe una BDD, busca la tabla "nombre" e inserta una lista de datos.

    # todo: Usar el diccionario + la lista de puntajes para conformar una secuencia de "update + set" en SQL.
    # Hacer el set varias veces (recorriendo cada elemento de la lista
    # 'nombre' = valor
    # WHERE 'ID' = contador
    # Y al final poner el commit.

    largolista=len(lista)       # Largo de la lista.
    id=0
    atributo=str(nombretabla)
    aux = []

    for aux in lista:
        # contador = 0
        # for aux in aux:        # Copia el contenido de la columna (registro) en la lista "lista".
        #bdd.execute()      # En columna 'Nombre', pone comillas así la BDD toma el valor como texto.
        bdd.execute("""
                    UPDATE """ + str(atributo) + """
                SET 'ID'        = """ + str(aux[0]) + """ ,
                    'Turno'     = """ + str(aux[1]) + """ ,
                    'Nombre'    = ' """ + str(aux[2]) + """ ' ,
                    'Uno'         = """ + str(aux[3]) + """ ,
                    'Dos'         = """ + str(aux[4]) + """ ,
                    'Tres'         = """ + str(aux[5]) + """ ,
                    'Cuatro'         = """ + str(aux[6]) + """ ,
                    'Cinco'         = """ + str(aux[7]) + """ ,
                    'Seis'         = """ + str(aux[8]) + """ ,
                    'Escalera'  = """ + str(aux[9]) + """ ,
                    'Full'      = """ + str(aux[10]) + """ ,
                    'Poker'     = """ + str(aux[11]) + """ ,
                    'Generala'  = """ + str(aux[12]) + """ ,
                    '2Generala' = """ + str(aux[13]) + """

                    WHERE 'ID'  = """ + str((aux[0])) + """;
                """)

    bdd.commit()
           #fixme: El commit debería hacerse en otra función, o no?


def IniciarBDD (directorio, nombreBDD):
    #Recibe el directorio y el nombre de la base de datos.

    #nombreBDD = 'BDD_Generala.db'  # Nombre del archivo de la BDD
    #directorio = str(sys.path[0])  # Directorio local donde se aloja el programa.

    bdd = sqlite3.connect(directorio + '\\' + nombreBDD)  # Accede a la base de datos.

    # print('bdd = ' + str(directorio + '\\' + nombreBDD))
    # print('bdd = ' + str(bdd))

    return bdd


def BuscarTablas (bdd):

    bdd.execute('SELECT name FROM sqlite_master')

    lista_tablas =(bdd.fetchall())

    # print('lista_tablas:')
    # print('lista_tablas[0]= ',str(lista_tablas[0][0]))
    # print('lista_tablas[1]= ',str(lista_tablas[1][0]))

directorio_local= str(sys.path[0])          # Directorio local donde se aloja el programa.

bdd_actual=0 #Indica que no hay BDD abierta
bdd_actual=IniciarBDD(directorio_local, 'BDD_Generala.db')  #Se conecta a la base de datos.
bdd_cursor= bdd_actual.cursor()  # Asigna el cursor.

nombre_partida='Partida_1'

# BuscarTablas(bdd_cursor)


####################### Pruebas ###########################
# LeerPartidas(bdd_cursor)


# EscribirTabla(bdd_cursor,'Partida_1',tuple([1,'BRUNO',1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]))
#
# LeerTabla(bdd_cursor,nombre_partida)
# print('Contenido BDD:\n\n'+str(bdd_cursor.fetchall()))  #Lee toda la tabla
