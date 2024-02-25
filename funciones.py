import numpy as np
import random 

# Función que crea tablero 10x10 

def crear_tablero(tamaño=(10, 10)):
    return np.full(tamaño, "_")

# Función que genera barcos random y comprueba que no se salgan de las dimensiones del tablero 

def crear_barco_random(eslora):
    fila_a = random.randint(0, 9)
    columna_a = random.randint(0, 9)
    orientacion = random.choice(["S", "O", "E", "N"])

    barco = [(fila_a, columna_a)]
    while len(barco) < eslora:
        if orientacion == "O" and columna_a - (eslora - 1) >= 0:
            columna_a -= 1
        elif orientacion == "E" and columna_a + (eslora - 1) <= 9:
            columna_a += 1
        elif orientacion == "S" and fila_a + (eslora - 1) <= 9:
            fila_a += 1
        elif orientacion == "N" and fila_a - (eslora - 1) >= 0:
            fila_a -= 1
        else:
            fila_a = random.randint(0, 9)
            columna_a = random.randint(0, 9)
            orientacion = random.choice(["S", "O", "E", "N"])
            barco = [(fila_a, columna_a)]
            continue
        barco.append((fila_a, columna_a))
    return barco

# Función que coloca los barcos en el tablero 

def colocar_barco(barco, tablero):
    for fila, columna in barco:
        tablero[fila, columna] = "O"
    return tablero

# Función que chequea que la posición del barco generado no coincide con otro ya existente en el tablero

def check_superposicion(barco, tablero):
    for i in barco:
        if tablero[i] == "O":
            print("Ya hay un barco en esa posición, vamos a generar otro barco")
            return True
    return False

# Función que genera nº concreto de barcos, de unas dimensiones y los coloca en tablero (MÁQUINA/JUGADOR)
"""
Es una función que permite crear los barcos tanto de jugador como máquina en función de los atributos 
cantidad y eslora, y lo imprima en tablero.

Se basa en un bucle for que recorre la cantidad de barcos, y va asignando coordenadas válidas (dentro de tablero)
en función de su eslora. 

A su vez, con el while le decimos que mientras no se superpongan esos barcos, los incluya en el tablero. ""

"""

def generar_barcos(cantidad, eslora, tablero):

    for generar_barcos in range(cantidad):

        print("(MÁQUINA) Generando barco número ",generar_barcos,"...")
        barco = crear_barco_random(eslora)

        while check_superposicion(barco, tablero):
            barco = crear_barco_random(eslora)
        tablero = colocar_barco(barco, tablero)
    return tablero


#for generar_barco_jugador in range(4):
    
    # print("(JUGADOR) Generando barco número ",generar_barco_jugador,"...")
    # barco = crear_barco_random(2)
        
        #while check_superposicion(barco, tablero_jugador):
            # barco = crear_barco_random(2)
        #tablero_jugador = colocar_barco(barco, tablero_jugador)

# Generar, check superposición y colocar barcos en el tablero de la MÁQUINA
# for generar_barco_maquina in range(4):

#     print("(MÁQUINA) Generando barco número ",generar_barco_maquina,"...")
#     barco = bc.crear_barco_random(2)

#     while tab.check_superposicion(barco, tablero_maquina):
#         barco = bc.crear_barco_random(2)
#     tablero_maquina = bc.colocar_barco(barco, tablero_maquina)




# Función de disparar  
"""
Si el disparo (x,y) == (fila,columna) corresponde con una casilla "_" en el tablero, entonces es Agua.
    
Si el disparo corresponde con una casilla "O" entonces ha tocado otro barco, Tocado.
    
Si nada de esto : Ya se ha disparado ahí.
"""

def disparar(casilla, tablero):
    if tablero[casilla] == "_":
        print("Agua")
        tablero[casilla] = "A"
    elif tablero[casilla] == "O":
        print("Tocado")
        tablero[casilla] = "X"
    else:
        print("Ya has disparado aquí")
    return tablero



# Función para comprobar los barcos que han sido desruidos 

"""
Si no encontramos ninguna "O" en el tablero quiere decir que los barcos  están destruidos y se ha ganado 
"""
def check_barcos_destruidos(tablero):
    return "O" not in tablero



# Función para generar turnos JUGADOR y MÁQUINA

"""
En el turno del jugador se trabajara sobre el tablero de la máquina. Se le pide al jugador fila y columa == x,y
Esas coordenadas son el disparo, así ejecutamos la función disparo hacia el tab máquina. 

En el caso del turno de la máquina, es similar, salvo que las coordenadas son random.
"""

def turno_jugador(tablero_maquina):
    print("Tu turno")
    x = int(input("Introduce una fila del 0 al 9): "))
    y = int(input("Introduce una columna del 0 al 9: "))
    disparo = (x, y)
    disparar(disparo, tablero_maquina)
    print("Tablero de la máquina:")
    print(tablero_maquina)

def turno_maquina(tablero_jugador):  
    print("Turno de la máquina")
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    disparo = (x, y)
    disparar(disparo, tablero_jugador)  
    print("Tablero del jugador:")
    print(tablero_jugador)