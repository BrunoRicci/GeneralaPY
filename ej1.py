import random

jugadas_posibles = {
    # Nombre diccionario / Tupla: (Tupla1, Tupla2)
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,

    'Escalera': ([], []),
    'Full': ([], []),
    'Poker': ([], []),
    'Generala': ([], []),
    '2Generala': ([], [])
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


def MensajeError(mensaje):
    print('\n### ERROR ###: ' + str(mensaje))
    print('Presione <ENTER> para continuar... ')


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
    DebugPrint('dados='+str(dados))
#    DebugPrint('len(dados)='+str(len(dados)))

    if len(dados) <= 5:     #Continúa...
        contador = 0

        #for aux in dados:

        if dados[0] == '':
            ingreso_ok=0 #error. #todo: HACER QUE BLOQUEE ACÁ Y PIDA REINGRESAR

        contador=0  #Contador para recorrer la lista.
        pos=1 #inicializo para un valor que entre al while en el primer ciclo.
        for pos in dados:
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


def Turno_Jugador(jugador):
    # Recibe de qué jugador es el turno, para saber qué posiciones de puntajes ya tiene utilizadas, y así
    # no dar posibilidad de sobreescribirlo.
    # Además, si el jugador hizo uno o más tiros y salió del juego, esto queda guardado en su "status", por
    # lo cual esto permite evitar que salga y vuelva a entrar al juego para repetir su turno "desde cero".
    # todo ver posiblildad de hacerla compatible con la generala servida.

    jugada = [0, 0, 0, 0, 0]  # Inicializo la lista "jugada" con todos en 0...
    jugada = OrdenarDados(Tirar_Dados(jugada, [1, 2, 3, 4, 5]))  # Tira todos los dados.

    print('   Tiro 1: ' + str(jugada))  # Muestra los dados

    # Permite hacer los 3 tiros al jugador, y elegir qué dados volver a tirar...
    # todo: PERMITIR PLANTARSE AHÍ Y NO SEGUIR TIRANDO!!
    for contador_tiros in range(2, 4):  # Ejecuta 2 veces, inciando desde 2.

        dados_relanzados=0
        while dados_relanzados == int(0):
            print('\n   Seleccione qué número(s) de dado quiere volver a tirar separados por coma. ')
            dados_relanzados = Elegir_dados()
            #DebugPrint('dados_relanzados=' + str(dados_relanzados))
            if dados_relanzados == 0:        #Si no se ingresa nada...
                # Dar aviso de error.
                a=0

        jugada = OrdenarDados(Tirar_Dados(jugada, dados_relanzados))  # PRUEBA: Lanza todos los dados...

        print('   Tiro ' + str(contador_tiros) + ': ' + str(jugada))  # Muestra los dados

        contador_tiros = contador_tiros + 1  # Incrementa contador.

    puntaje = Determinar_jugadas(Cantidad_por_numero(jugada))

    # todo: VER PUNTAJE ACTUAL DEL JUGADOR Y PERMITIR ELEGIR EN QUÉ CASILLERO SE QUIERE ANOTAR LOS PUNTOS.
    # todo: Función para leer puntaje. Menú para mostrar posibliidades y elegir una.
    # todo: punaje=ElegirJugada ...
    print('\n\nJugada armada: ' + str(puntaje))  # Determina qué jugada logró armar el jugador luego de sus tres tiros.

    puntaje_final = 0  # todo: Hacer función para ver jugadas ya utilizadas y elegir dónde anotar los puntos,
    return puntaje_final


def MenuPrincipal():
    a = 0


#############################################################################-
############################### PROGRAMA ####################################-
#############################################################################-


# MenuPrincipal()


#Turno_Jugador(1)  # Turno del jugador numero 1

#Tirar_Dados([0,0,0,0,0],['1','2','3'])
#DebugPrint('Tirar_Dados= '+str(Tirar_Dados([0,0,0,0,0],['1','2','4'])))

#

#jugada=Tirar_Dados([0,0,0,0,0],[1,2,3,4,5])
# #DebugPrint('jugada= '+str(jugada))
DebugPrint('Elegir_Dados()=' + str(Elegir_dados()))

#DebugPrint('Turno_Jugador: '+str(Turno_Jugador(1)))
