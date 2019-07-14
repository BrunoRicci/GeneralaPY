import random
import sys
import os

import BDD_Generala

dicc_anotador = { # Nombre diccionario / ubicación en la lista.)
    'ID':       0,
    'Turno':    1,
    'Nombre':   2,
    '1':        3,
    '2':        4,
    '3':        5,
    '4':        6,
    '5':        7,
    '6':        8,
    'Escalera': 9,
    'Full':     10,
    'Poker':    11,
    'Generala': 12,
    'Doble generala':13
}


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

    cont = 1
    for num in conjuntos:
        resultado.append([str(cont), num * cont])
        cont = cont + 1

    resultado.append(['Escalera', 0])
    resultado.append(['Full', 0])
    resultado.append(['Poker', 0])
    resultado.append(['Generala', 0])
    resultado.append(['Doble generala', 0])

    if (5 in conjuntos):                        # Generala.
        resultado[dicc_anotador['Generala']-3][1]=50
    elif (4 in conjuntos):                      # Poker.
        resultado[dicc_anotador['Poker']-3][1] = 40
    elif (3 in conjuntos and 2 in conjuntos):   # Full.
        resultado[dicc_anotador['Full']-3][1] = 30
    elif (conjuntos == [1, 1, 1, 1, 1, 0] or conjuntos == [0, 1, 1, 1, 1, 1]):  # Escalera
        #             [1,2,3,4,5]                     [2,3,4,5,6]
        resultado[dicc_anotador['Escalera']-3][1] = 20


    # DebugPrint('resultado = '+str(resultado))
    return list(resultado)  # Devuelve en formato lista, qué jugadas se forman (primero las especiales y luego las simples.


def Tirar_Dados(j, d_n):
    # Recibe una jugada (estado inicial de los dados) y distintas posiciones de dados (d_n -> 1 <= n <= 5)
    # a volver a lanzar (dn=1),y otras a conservar (dn=0)

    if d_n != 0:    #Si no se le ingresa un valor incorrecto...
        contador=0
        for var in d_n:            # Convierte cada elemento de la lista de formato "string" a formato "int".
            d_n[contador]=int(var)
            contador=contador+1
        # DebugPrint('d_n='+str(d_n))
        # DebugPrint('len(d_n)='+str(len(d_n)))


        for dado in d_n:
            if dado != int(0):
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

    print('\nIngrese cuáles dados desea volver a lanzar, separados por coma:')
    print('Para plantarse, ingrese 0 (cero).  \n')
    dados = str(input())
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


def Turno_Jugador(puntaje_jugador):
    # Recibe de qué jugador es el turno, para saber qué posiciones de puntajes ya tiene utilizadas, y así
    # no dar posibilidad de sobreescribirlo.
    # Además, si el jugador hizo uno o más tiros y salió del juego, esto queda guardado en su "status", por
    # lo cual esto permite evitar que salga y vuelva a entrar al juego para repetir su turno "desde cero".
    # todo: ver posiblildad de hacerla compatible con la generala servida.

    ######################### Recibe el nombre del jugador, y extrae el puntaje con el mismo. ##########################

    puntaje_final=puntaje_jugador   #Inicializa variable con el formato correspondiente (formato anotador).
    jugada = [0, 0, 0, 0, 0]  # Inicializo la lista "jugada" con todos en 0...

    print('- - - - -   TURNO DE ' + str(puntaje_final[dicc_anotador['Nombre']]) + '   - - - - -\n')

    MostrarPuntajes(puntaje_jugador)    #Muestra puntaje actual.

    # Permite hacer los 3 tiros al jugador, y elegir qué dados volver a tirar...
    fin_turno=0
    contador_tiros=0
    dados_relanzados=[1,2,3,4,5]    # Inicializo variable, para que lance todos los dados.

    jugada = OrdenarDados(Tirar_Dados(jugada, dados_relanzados))  # Lanza los dados...
    print('   Tiro ' + str(contador_tiros + 1) + ': ' + str(jugada))  # Muestra los dados

    while contador_tiros < 2 and fin_turno == 0:  # Ejecuta 2 veces, inciando desde 2.

        contador_tiros = contador_tiros + 1  # Incrementa contador.

        dados_relanzados=0
        while dados_relanzados == int(0):
            dados_relanzados = Elegir_dados()
            # DebugPrint('dados_relanzados=' + str(dados_relanzados))


            # elif dados_relanzados[0] == '0':
            if type(dados_relanzados)!= type(int(0)):    # Si no es un entero...
                if dados_relanzados[0] == '0':        #todo: Hacer algo para evitar que si el resultado de Elegir_dados da 0 (error) no entre al if que accede a la posicion [0, ya que esto no es posible.
                    # dados_relanzados = [0,0,0,0,0]
                    fin_turno=1
                else:                   # Si se ingresó correctamente uno o más dados..
                    jugada = OrdenarDados(Tirar_Dados(jugada, dados_relanzados))  # Lanza los dados...
                    print('   Tiro ' + str(contador_tiros + 1) + ': ' + str(jugada))  # Muestra los dados
            elif dados_relanzados[0] == 0:        #Si no se ingresa nada...
                MensajeError('Seleccione dados correctamente!')

    puntaje_final = Determinar_jugadas(Cantidad_por_numero(jugada))   # Determina qué jugadas (especiales o no) se lograron.

    # puntaje_jugador[dicc_anotador['Generala'] > 0]

    print('\nElija la jugada a anotar:')  # Determina qué jugada logró armar el jugador luego de sus tres tiros.
    lista_puntaje=[]
    cn=0
    for aux in puntaje_final:     # Recorre los puntajes logrados...

        if contador_tiros == 1 and aux[1] != 0:          # Si fue jugada servida...
            if (aux[0] == 'Escalera') or (aux[0] == 'Full') or (aux[0] == 'Poker') or (aux[0] == 'Generala'):
                #todo: Chequear si el jugador ya hizo generala -> Para finalizar la partida.
                if aux[0] == 'Generala':
                    aux[1] = aux[1] + 10  # Suma 5 por ser jugada servida.
                    return ['Generala',55]      # GENERALA SERVIDA.
                else:
                    aux[1] = aux[1] + 5  # Suma 5 por ser jugada servida.

        elif aux[0] == 'Generala' and puntaje_jugador[dicc_anotador['Generala']] > 0:     # Si ya hizo generala...
            aux = ['Doble generala',60]

        if puntaje_jugador[puntaje_final.index(aux)+3] == (-1):       #Si el casillero no está utilizado...
            print(str(cn)+': '+str(aux))    # Muestra el puntaje.
            lista_puntaje.append(aux)
            cn = cn + 1  # Incrementa el contador.


    aux=-1
    while not (int(aux) >= 0  and int(aux) < cn):    # Mientras se ingrese un numero dentro del rango...
        aux=int(input())                            # Da a elegir un puntaje para anotar.
        # if type(aux) != type(str('')):   # Si no es un caracter (es un número)...
        #     aux=int(aux)
        # else:
        #     aux=0
        # DebugPrint('aux = '+str(aux))
    puntaje_final = lista_puntaje[aux]  # Guarda el puntaje seleccionado.


    # todo: hacer que se indique si fue una jugada servida, ya que en caso se ser generala doble, el jugador gana.
    # todo: -> Esto se podría hacer así: Si es jugada especial y el puntaje termina en 5, y era Generala, y ya
    # todo: había salido (generala doble) entonces es generala doble servida.
    # todo: Para acceder al anotador:    if anotador[jugador][cont] == int(0): lista_aux.append(cont)
    # todo: busca qué posiciones están en 0 (sin anotar) y las guarda en una lista auxiliar.
    # todo: Hacer función para ver jugadas ya utilizadas y elegir dónde anotar los puntos,


    print('Puntaje anotado: ' + str(puntaje_final))
    return puntaje_final


def NuevaPartida():
    # Borrar pantalla.
    print('     Nueva partida:\n\n')

    lista_jugadores=PedirIngresoJugadores()        #Pide que se ingresen los jugadores.
    nombre_partida= BDD_Generala.nombre_partida     #Nombre de la tabla asociada a la partida.
    # cursor=BDD_Generala.bdd_cursor

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

    # DebugPrint('PARTIDAS: '+str(BDD_Generala.LeerPartidas(BDD_Generala.bdd_cursor)))

    BDD_Generala.BorrarTabla(BDD_Generala.bdd_cursor, nombre_partida)       #Borra tabla actual

    tabla_jugadores = ArmarTablaPuntajes(lista_jugadores)
    BDD_Generala.CrearTabla(BDD_Generala.bdd_cursor, nombre_partida, tabla_jugadores)      #Crea tabla (si no existe) con el nombre dado.

    return tabla_jugadores


def CargarPartida():
    nombre='Partida_1'
    # Obtiene el anotador (tabla de puntos) y lo pasa a tipo lista.

    bdd_tablas=BDD_Generala.LeerPartidas(BDD_Generala.bdd_cursor)
    # DebugPrint('bdd_tablas = '+str(bdd_tablas))
    for tabla in bdd_tablas:
        # DebugPrint('tabla[0] = ' + str(tabla[0]))
        if nombre in tabla[0]:    # Si existe la tabla en las existentes...
            tabla = CastearALista(BDD_Generala.LeerTabla(BDD_Generala.bdd_cursor,nombre))

    if tabla != 0:
        return tabla
    else:
        MensajeError('     ¡Partida inexistente! Cree una nueva partida.', 1)
        return 0


def CastearALista (tupla):
    for aux in tupla:
        tupla[tupla.index(aux)]=list(aux)   # Elige el elemento en la posición de "aux" y lo castea a tipo "list".

    return tupla


def PedirIngresoJugadores ():

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
    # Recibe una columna (hay una por jugador) y la inserta en el anotador.

    anotador = []
    columna = []
    num_jugador=1  #Arranca en 1 (PK de la BDD).

    for nombre in jugadores:
        columna.append(num_jugador)
        num_jugador=num_jugador+1       #Incrementa numero
        columna.append(0)       # Coloca numero de turno en la columna
        columna.append(nombre)  # Coloca el nombre en la columna
        for i in range(0,11):           # Agrega 11 elementos a la lista, incializando todos en valor int(-1) -> casillero vacío.
            columna.append(int(-1))
        # DebugPrint('columna = ' + str(columna))

        anotador.append(columna)        # Agrega columna generada al anotador.
        columna=[]                      # Limpia lista de columna.

    anotador[0][dicc_anotador['Turno']]=1       #Pone numero "1" en el primer jugador; indicando que va por el primer tiro...
    # DebugPrint('anotador = ' + str(anotador))

    return anotador


def CorrerJuego (tabla_puntajes):
    # El juego siempre se desarrolla a partir de una tabla; la cual incluye en una de las posiciones, el número
    # de turno (jugador) y el número de tiro actual.
    # Controla el orden de los turnos de los jugadores.

    finalizar_ronda = 0    # Inicializo variable

    jugador = ObtenerTurnoJugador(tabla_puntajes)  # Obtiene el turno del jugador correspondiente.
    num_ronda = ObtenerRonda(tabla_puntajes)    # Obtiene el número de ronda actual


    # DebugPrint('tabla_puntajes = '+str(tabla_puntajes))
    cantidad_jugadores=len(tabla_puntajes)

    while num_ronda < 11 :
        # jugador = ObtenerTurnoJugador(tabla_puntajes)  # Obtiene el turno del jugador correspondiente.

        while jugador <= cantidad_jugadores and finalizar_ronda != 1:        # Recorre los turnos hasta que se termine la ronda...

            puntaje=Turno_Jugador(tabla_puntajes[jugador-1])  # Inicia el turno del jugador... el -1 es xq empieza en 0.
            # os.system('cls')
            if puntaje != ['Generala',55] :   # Si no hizo generala servida...
                tabla_puntajes = ModificarAnotador(tabla_puntajes, jugador-1, puntaje)          # Anota el puntaje.
                tabla_puntajes = ModificarAnotador(tabla_puntajes, jugador-1, ['Turno', 0])   # Finaliza turno jugador actual.

                if jugador < cantidad_jugadores:    # Incrementa al siguiete jugador.
                    jugador=jugador+1
                else:
                    finalizar_ronda=1
                    jugador=1

                tabla_puntajes = ModificarAnotador(tabla_puntajes, jugador-1, ['Turno', 1]) # Turno del próximo jugador.

                BDD_Generala.ModificarTabla(BDD_Generala.bdd_cursor,BDD_Generala.nombre_partida,tabla_puntajes)    # Guarda el anotador en la BDD.

            else:
                print(' ---- GENERALA SERVIDA ----')
                # print('   .- JUEGO  TERMINADO -.')
                num_ronda=11        #Finaliza el juego

        num_ronda=num_ronda+1   #Incrementa el numero de ronda.
        finalizar_ronda=0

    print('\n\n_________________________________ FIN DEL JUEGO _________________________________\n')
    MostrarPuntajes(tabla_puntajes)
    print('\nPuestos y puntajes totales:')

    lista_puntajes = DeterminarPuntajes(tabla_puntajes)
    # DebugPrint('lista_puntajes =' + str(lista_puntajes))
    lista_aux = []
    i=0
    for i in lista_puntajes:
        lista_aux.append(i[1])

    lista_aux.sort(reverse=True)  #Ordena de menor a mayor

    lista_resultados = []
    for cn in range (0,len(lista_aux)):
        for i in lista_puntajes:     #Recorre los resultados, ordenados de menor a mayor
            # DebugPrint('i = ' + str((i)))
            # DebugPrint('index = '+str(lista_puntajes.index(i)))
            # DebugPrint('valor_comparacion = '+str(lista_aux[lista_puntajes.index(i)]))
            if i[1]==lista_aux[cn]:
                lista_resultados.append(i)
            # DebugPrint('lista_resultados =' + str(lista_resultados))

    i=0
    for i in lista_resultados:
        print(  str(lista_resultados.index(i) + 1) +'°-> ' + str(i[0]) + ' : ' + str(i[1]) +'.'  )

    input('\n        Presione ENTER para cerrar el juego.')   # Espera a que se presione ENTER para cerrar.
#   ---------------------------------------------------------------------------------------------------------


def MostrarPuntajes (tabla):
    #Muestra los puntajes, partiendo de una tabla en el formato normalizado. Si se envía una columna, muestra solo esa.

    print('_____________________________ PUNTAJES: ______________________________')
    print('Jugador       | 1  | 2  | 3  | 4  | 5  | 6  | E  | F  | P  | G  | 2G |')

    if len(tabla) == 14:    #Si puede ser una única columna...
        if type(tabla[0])==(type (int(0))):    #Si lo que contiene no es una lista...
            tablaaux = []  # FIXME: ARREGLAR!! Se puso esto para que "columna" tome un único valor en caso de no ser tabla (lista simple).
            tablaaux.append(tabla)  # Crea una lista de listas, incluyendo la columna y una vacía.
            tablaaux.append([''])   # Agrega una lista "dummy" para que la variable "columna" tome el valor de listas completas.
            tabla = tablaaux


    for columna in tabla:

        if len(columna) == 14:  # Si es una lista válida (formato normalizado, 14 elementos)...
            aux = []  # Creo lista.
            largonombre = len(columna[dicc_anotador['Nombre']])  # Largo del nombre.
            aux.append(columna[dicc_anotador['Nombre']]+str(' '*(13-largonombre)))        #Coloco nombre

            for cn in range(3,14):      # Recorre los datos de los puntajes
                if columna[cn] < 10:
                    aux.append(' '+str(columna[cn]))
                else:
                    aux.append(columna[cn])

                if columna[cn] == (-1):   # Si no hay nada anotado...
                    aux[cn - 2]= '--'    # Coloca espacio en blanco.

            string=''
            for i in aux:
                string = string + str(( str(i) +' | '))
            print(str(string))

    print('______________________________________________________________________\n')


def ObtenerTurnoJugador (anotador):
    jugador_actual=0
    largo=len(anotador)     #Cantidad de jugadores
    # DebugPrint('lista:')
    for lista in anotador:      #Poner centinela para no hacer el loop completo innecesariamente
        # DebugPrint('lista : '+str(lista))
        if int(lista[dicc_anotador['Turno']]) >= 1:      #Si es el turno del jugador...
            jugador_actual=lista[dicc_anotador['ID']]   #Guarda el ID (numero de jugador).

    # DebugPrint('jugador_actual: '+str(jugador_actual))

    return jugador_actual   #Devuelve el ID de jugador.


def ObtenerRonda (anotador):
    # Busca en el anotador la cantidad de filas (jugadores) que hay con valores distintos a -1 (utilizados).
    # Busca en la columna del jugador actual, la cantidad de "-1" que aparecen en los puntajes.
    ronda_actual = 11 - anotador[ObtenerTurnoJugador(anotador)-1].count(int(-1))
    # DebugPrint('ronda_actual = '+str(ronda_actual))
    return ( ronda_actual )    #Resta 1 porque el N° de jugador se asocia al ID (empieza en 1).


def ModificarAnotador (anotador, jugador, valor):
    # En un determinado anotador (tabla formada por listas), selecciona la lista de un jugador, y le anota un puntaje en
    # la posición indicada. La posición se encuentra por diccionario, ya que la variable "valor" es una lista con la jugada
    # donde se va anotar (números o jugadas especiales), mas el valor del puntaje a anotar.

    # Coloca en la posición incicada (en cuál de todos los puntajes) el valor numérico del puntaje.
    anotador[jugador][dicc_anotador[str(valor[0])]] = valor[1]     #Pone el valor numérico en la posición del puntaje.
    # DebugPrint('    anotador:')
    # for aux in anotador:
    #     # DebugPrint('Jugador '+str(aux[dicc_anotador['Nombre']])+': '+str(aux))
    #     a=0
    return anotador


def DeterminarPuntajes (tabla):

    lista_puntajes=[]
    for puntaje_jugador in tabla:

        lista_aux=[]
        lista_aux.append(puntaje_jugador[dicc_anotador['Nombre']])  #Posición para el nombre.
        lista_aux.append(0)     #Posición para el puntaje total.
        for i in range(3,14):
            if i > 0:   # Si el casillero del puntaje es mayor a 0 (está utilizado)...
                lista_aux[1] = lista_aux[1] + puntaje_jugador[i]

        lista_puntajes.append(lista_aux)

    return lista_puntajes


def SalirJuego():
    #Sale del juego.
    exit(1) #Finaliza con valor 1.


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

    if type(tabla) == list:
        CorrerJuego(tabla)      #Inicia el juego con la tabla actual seleccionada (nueva o continuada).
    else:
        MensajeError('   El juego se cerrará.',1)

    SalirJuego()


    return 1 #Finaliza el programa sin error...


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

MenuPrincipal()
#CorrerJuego(CargarPartida())

#ASDSADASD