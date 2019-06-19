import random
import sys

import BDD_Generala

dicc_anotador = { # Nombre diccionario / ubicación en la lista.)
    'Nombre':   0,
    'Turno':    1,
    '1':        2,
    '2':        3,
    '3':        4,
    '4':        5,
    '5':        6,
    '6':        7,
    'Escalera': 8,
    'Full':     9,
    'Poker':    10,
    'Generala': 11,
    '2Generala':12
}


puntajes_jugador = []

def Cantidad_por_numero(jugada):
    # [Nombre]['1','2','3','4','5','6','Escalera','Full','Poker','Generala','2Generala']
    # Recibe una jugada, y devuelve una lista que contiene de forma ordenada la cantidad de dados que salieron con cada dado.
    lista = [0, 0, 0, 0, 0, 0]  # Lista de apariciones.

    for i in jugada:
        lista[i - 1] = lista[i - 1] + 1  # Suma 1 a la posición que corresponde al número posible (1 al 6).
    # print('<DEBUG>:lista= '+str(lista))
    return lista

def Determinar_jugadas(conjuntos):
    # Se le ingresa un numero de apariciones por numero y devuelve
    # qué tipo de jugada especial es, y qué tipo de jugada simple
    # (toda jugada especial puede ser una jugada simple, aunque no viceversa.
    # En caso de no formarse una jugada especial, devuelve 'null' como 1er argumento.
    resultado = []  # Lista que devuelve la función, primero el tipo de jugada y luego el puntaje.

    if (5 in conjuntos):                        # Generala.
        resultado.append(['Generala', 50])
    elif (4 in conjuntos):                      # Poker.
        resultado.append(['Poker', 40])
    elif (3 in conjuntos and 2 in conjuntos):   # Full.
        resultado.append(['Full', 30])
    elif (conjuntos == [1, 1, 1, 1, 1, 0] or conjuntos == [0, 1, 1, 1, 1, 1]):  # Escalera
        #             [1,2,3,4,5]                     [2,3,4,5,6]
        resultado.append(['Escalera', 20])

    cont = 1
    for num in conjuntos:
        resultado.append([str(cont), num * cont])
        cont = cont + 1

    return list(resultado)  # Devuelve en formato lista, qué jugadas se forman (primero las especiales y luego las simples.

def Tirar_Dados(j, d_n):
    # Recibe una jugada (estado inicial de los dados) y distintas posiciones de dados (d_n -> 1 <= n <= 5)
    # a volver a lanzar (dn=1),y otras a conservar (dn=0)

    if d_n != 0:    #Si no se le ingresa un valor incorrecto...
        contador=0
        for var in d_n:             # Convierte cada elemento de la lista de formato "string" a formato "int".
            d_n[contador]=int(var)
            contador=contador+1
        # DebugPrint('d_n='+str(d_n))
        # DebugPrint('len(d_n)='+str(len(d_n)))

        # ##Puede que haya que sacarlo...
        # while len(d_n) < len(j):      #Hace que el largo de la lista "d_n" sea igual al de "j", agregando elementos al final de esta.
        #     d_n.append(0)
        #
        # for contador in range(0, len(j)):
        #     if d_n[contador] == contador + 1:  # Si coincide el numero (dado seleccionado)...
        #         j[contador] = (random.randrange(1, 7))  # Lanza dado y reemplaza el valor anterior.
        #         # todo: Hacer que en la función de ElegirDados ponga los elementos de la lista que no se usan en 0.
        #         # todo: ejemplo: 1,2,4 -> [1,2,4,0,0]

        for dado in d_n:
            j[dado-1] = (random.randrange(1, 7))  # Lanza dado y reemplaza el valor anterior.

    return j

def OrdenarDados(dados):
    # Ordena los dados de mayor a menor, de izquierda a derecha.

    dados.sort(reverse=True)  # Ordena los elementos de mayor a menor, colocándolos de izquierda a derecha.
    return dados

def DebugPrint(mensaje):
    # Coloca la leyenda "<DEBUG>:" y luego un valor o mensaje convertido a formato string, mostrándolo en pantalla.
    print('<DEBUG>:' + str(mensaje))

def MensajeError(mensaje, wait):
    print('\n### ERROR ###: ' + str(mensaje))
    if wait == 1:
        print('Presione <ENTER> para continuar... ')
        input() #Espera a que se presione <ENTER>...

def Elegir_dados():
    # Ingresar hasta 5 posiciones separadas por coma (',').
    # Resultado: lista de hasta 5 elementos, sin repetir, ordenados de menor a mayor,
    # que representa qué dados se van a volver a lanzar.

    # Filtrar errores:
    # Si la lista está vacía, devuelve 0.
    # Si hay elementos distintos a [0;9] y ',' (coma), muestra error de que se ingresó mal.
    # Si hay un elemento repetido, muestra error de que se ingresó mal.

    ingreso_ok = 1  #Inicializo variable
    dados = []

    dados = str(input('Ingrese cuáles dados desea volver a lanzar, separados por coma: '))
    dados = dados.split(',')  # Genera lista con los dados
    # DebugPrint('dados='+str(dados))
#    DebugPrint('len(dados)='+str(len(dados)))

    if len(dados) <= 5:     #Si tiene menos de 5 elementos, continúa...
        contador = 0

        #for aux in dados:

        if dados[0] == '':
            ingreso_ok=0 #error. #todo: HACER QUE BLOQUEE ACÁ Y PIDA REINGRESAR

        contador=0  #Contador para recorrer la lista.
        pos=1 #inicializo para un valor que entre al while en el primer ciclo.
        for pos in dados:
            #if type(pos) == type(int(1)):       # Si es numero entero... todo: HACER QUE EVITE LOS CARACTERES NO NUMERICOS...
                if (ingreso_ok != 0 and (int(pos) >= int(0)) and (int(pos) <= int(5))):
                    ingreso_ok = 1
                    contador=contador+1
                else:
                    ingreso_ok = 0

        if contador == len(dados):      #Si todos los elementos cumplieron con la condición de ser de entre 0 y 9...
            ingreso_ok = 1     # Continua...
        else:
            ingreso_ok = 0  # Error, volver a ingresar.
    else:
        ingreso_ok = 0      #Error, volver a ingresar.

#    DebugPrint('dados = ' + str(dados))  # DEBUG: Muestra lista generada.
#    DebugPrint('ingreso_ok=' + str(ingreso_ok))

    if ingreso_ok==0:
        return int(0)       #Devuelve 0.
    elif ingreso_ok==1:
        dados.sort(reverse=False)  # ordena los elementos de menor a mayor.
        return dados                # Devuelve lista como resultado de la función.

def Turno_Jugador(puntaje):
    # Recibe de qué jugador es el turno, para saber qué posiciones de puntajes ya tiene utilizadas, y así
    # no dar posibilidad de sobreescribirlo.
    # Además, si el jugador hizo uno o más tiros y salió del juego, esto queda guardado en su "status", por
    # lo cual esto permite evitar que salga y vuelva a entrar al juego para repetir su turno "desde cero".
    # todo ver posiblildad de hacerla compatible con la generala servida.

    ######################### Recibe el nombre del jugador, y extrae el puntaje con el mismo. ##########################

    jugada = [0, 0, 0, 0, 0]  # Inicializo la lista "jugada" con todos en 0...
    jugada = OrdenarDados(Tirar_Dados(jugada, [1, 2, 3, 4, 5]))  # Tira todos los dados.

    print('- - - - -   TURNO DE '+str(puntaje[dicc_anotador['Nombre']])+'   - - - - -\n')
   # print('   Tiro 1: ' + str(jugada)+'\n')  # Muestra los dados

    # Permite hacer los 3 tiros al jugador, y elegir qué dados volver a tirar...
    # todo: PERMITIR PLANTARSE AHÍ Y NO SEGUIR TIRANDO!! -> Se puede poner "0" al seleccionar dados a relanzar y listo...
    contador_tiros=0
    dados_relanzados=[1,2,3,4,5]    # Inicializo variable, para que lance todos los dados.
    while contador_tiros < 2:  # Ejecuta 2 veces, inciando desde 2.

        jugada = OrdenarDados(Tirar_Dados(jugada, dados_relanzados))  # Lanza los dados...
        print('   Tiro ' + str(contador_tiros+1) + ': ' + str(jugada))  # Muestra los dados

        dados_relanzados=0
        while dados_relanzados == int(0):
            dados_relanzados = Elegir_dados()
            #DebugPrint('dados_relanzados=' + str(dados_relanzados))
            if dados_relanzados[0] == 0:        #Si no se ingresa nada...
                a=0 # Dar aviso de error.
            elif dados_relanzados[0] == '0':
                contador_tiros=4

        contador_tiros = contador_tiros + 1  # Incrementa contador.

    puntaje = Determinar_jugadas(Cantidad_por_numero(jugada))

    # todo: VER PUNTAJE ACTUAL DEL JUGADOR Y PERMITIR ELEGIR EN QUÉ CASILLERO SE QUIERE ANOTAR LOS PUNTOS.
    # todo: Función para leer puntaje. Menú para mostrar posibliidades y elegir una.
    # todo: puntaje=ElegirJugada ...

    print('\nJugada armada: ' + str(puntaje))  # Determina qué jugada logró armar el jugador luego de sus tres tiros.

                    #todo: sumar 5 si "contador_tiros" indica que solo se tiró una vez.
                    #todo: hacer que se indique si fue una jugada servida, ya que en caso se ser generala doble, el jugador gana.
                    #todo: -> Esto se podría hacer así: Si es jugada especial y el puntaje termina en 5, y era Generala, y ya
                    #todo: había salido (generala doble) entonces es generala doble servida.
                                # todo: Para acceder al anotador:    if anotador[jugador][cont] == int(0): lista_aux.append(cont)
                                # todo: busca qué posiciones están en 0 (sin anotar) y las guarda en una lista auxiliar.
    puntaje_final = puntaje           # todo: Hacer función para ver jugadas ya utilizadas y elegir dónde anotar los puntos,
    return puntaje_final

def NuevaPartida():
    # Borrar pantalla.
    print('     Nueva partida:\n\n')

    lista_jugadores=PedirJugadores()        #Pide que se ingresen los jugadores.

    print('Los jugadores son:')  # Imprime la lista de jugadores.
    for aux in lista_jugadores:
        print(aux)

    # avance_ok=0
    # while avance_ok != 'S' or avance_ok != 'N'
    #     avance_ok = str(input('¿Desea continuar? <S/N>'))  # Pregunta de confirmación.
    #     if avance_ok == 'S':
    #         #Continua...
    #         a=0
    #     elif: avance_ok == 'N':
    #         #Vuelve atrás... -> Llamar a la misma función?
    #         a=0

    tabla_jugadores=ArmarTablaPuntajes(lista_jugadores)

    #todo: GRABAR TABLA GENERADA EN BASE DE DATOS.
    #todo: Hacer función que reciba tabla (verificar que sea información úttil por las dudas) y
    #todo: y la guarde en BDD.

    #todo: Si la tabla se genera correctamente, avanza y la dewuelve como resultado de esta función.
    #todo: Si no, devuelve un int(0) (ERROR).

    return tabla_jugadores

def CargarPartida():
    nombre='Partida_1'
    return BDD_Generala.LeerTabla(nombre)

def PedirJugadores ():

    lista_jugadores = []  # Inicializo una lista que contendrá los nombres de cada jugador

    avance_ok = 0  # Inicializo variable.
    jugador = ''  # Inicalizo variable...
    while avance_ok != 1:  # Pide jugadores hasta que ingrese '0'. Mientras
        # todo: Poner opción para cancelar/ir para atrás... -> Cómo hacer para detectar la tecla <ESC> presionada??
        jugador = str(input('   Ingrese el nombre de un jugador y presione <ENTER>...\n '))
        jugador = jugador.upper()  # Pone todas las letras en mayúsculas...

        if jugador != '0':
            if jugador != '':  # Si ingresa datos válidos...
                lista_jugadores.append(jugador)  # Agrega jugador a la lista.
            else:
                MensajeError('Ingrese un nombre válido.', 0)
        else:
            if len(lista_jugadores) < 2:
                MensajeError('Debe ingresar por lo menos DOS jugadores...', 0)
                avance_ok = 0
            else:
                avance_ok = 1  # Sale del loop

    # DebugPrint('lista_jugadores= '+str(lista_jugadores))
    return lista_jugadores

def ArmarTablaPuntajes (jugadores):
    # Arma una lista con los jugadores y sus posibles puntajes, incializados todos en int(0).
    # Los puntajes se deben almacenar en formato string; de haber uno en formato int (como el 0 inicial),
    # quiere decir que el puntaje de esa jugada no ha sido utilizado aún y que está disponible (no tachado).

    anotador = []
    columna = []

    for nombre in jugadores:
        columna.append(nombre)  # Coloca el nombre en la columna
        columna.append(0)       # Coloca numero de turno en la columna
        for i in range(0,11):           # Agrega 11 elementos a la lista, incializando todos en valor int(-1) -> casillero vacío.
            columna.append(int(-1))
        # DebugPrint('columna = ' + str(columna))
        anotador.append(columna)        # Agrega columna generada al anotador.
        columna=[]                      # Limpia lista de columna.

    #DebugPrint('anotador = ' + str(anotador))

    return anotador

def CorrerJuego (tabla_puntajes):
    # El juego siempre se desarrolla a partir de una tabla; la cual incluye en una de las posiciones, el número
    # de turno (jugador) y el número de tiro actual.
    # Controla el orden de los turnos de los jugadores.

    finalizar_ronda = 0    # Inicializo variable
    num_ronda = 0   # todo: A esta variable hay que asignarle el valor actual de la partida.
                    # todo: Hacer función que lea el anotador y vea cuántos casilleros tienen marcados exclusivamente TODOS los jugadores, para obtenerlo.
    # todo: Obtener numero de turno de jugador. -> Leyendo la columna ""

    # Obtiene nombres de todos los jugadores de la tabla.
    lista_jugadores = []


    DebugPrint('tabla_puntajes = '+str(tabla_puntajes))
    cantidad_jugadores=len(tabla_puntajes)
    DebugPrint('type tabla_puntajes: '+str(type(tabla_puntajes)))
    DebugPrint('len(tabla_puntajes) = '+str(len(tabla_puntajes)))


    while num_ronda < 11 or finalizar_ronda != 1:
        jugador = 0  # Inicializo variable de turno de jugador -> todo: Leer el numero de turno desde el anotador.

        while jugador < (cantidad_jugadores):        # Recorre los turnos hasta que se termine la ronda...
            puntaje=Turno_Jugador(tabla_puntajes[jugador])      # Inicia el turno del jugador...

            if puntaje != 'FIN':
                tabla_puntajes=AnotarPuntaje(tabla_puntajes,jugador,puntaje)       # Anota el puntaje.
                jugador = jugador + 1
            else:
                finalizar_ronda = 1

        num_ronda=num_ronda+1   #Incrementa el numero de ronda.



def AnotarPuntaje (anotador, jugador, valor):
    # En un determinado anotador (tabla formada por listas), selecciona la lista de un jugador, y le anota un puntaje en
    # la posición indicada. La posición se encuentra por diccionario, ya que la variable "valor" es una lista con la jugada
    # donde se va anotar (números o jugadas especiales), mas el valor del puntaje a anotar.

    return anotador

def SalirJuego():
    #Sale del juego.
    return 1


def MenuPrincipal():

    print('-------------------------------GENERALA-------------------------------')

    print('\n\nElija una opción y presione <ENTER>')
    print('\n')
    print('1 - Nuevo juego.')
    print('2 - Cargar juego.')      # Minimo requerimiento: que se pueda leer una sola jugada (no más de una).
    print('3 - Salir.')

    opcion=int(input())

    if opcion == 1:
        tabla=NuevaPartida()        # Crea una nueva tabla de puntajes y la guarda en la BDD.
    elif opcion == 2:
        tabla=CargarPartida()       # Lee una tabla de puntajes ya existente.
    elif opcion == 3:
        SalirJuego()

    CorrerJuego(tabla)      #Inicia el juego con la tabla actual seleccionada (nueva o continuada).

#############################################################################-
############################### PROGRAMA ####################################-
#############################################################################-


# MenuPrincipal()


#Turno_Jugador(1)  # Turno del jugador numero 1

#Tirar_Dados([0,0,0,0,0],['1','2','3'])
#DebugPrint('Tirar_Dados= '+str(Tirar_Dados([0,0,0,0,0],['1','2','4'])))


#jugada=Tirar_Dados([0,0,0,0,0],[1,2,3,4,5])
# #DebugPrint('jugada= '+str(jugada))
#DebugPrint('Elegir_Dados()=' + str(Elegir_dados()))

#DebugPrint('Turno_Jugador: '+str(Turno_Jugador(1)))

#ArmarTablaPuntajes(['Jugador 1','Jugador 2','Jugador 3'])


CorrerJuego(NuevaPartida())

