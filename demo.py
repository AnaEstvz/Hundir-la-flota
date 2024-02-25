import numpy as np
import random

import funciones as f
import time 

print(f"Vamos a jugar a hundir la flota. \n Se crearán dos tableros, el de la máquina y el del jugador \n En cada uno de los tableros se posicionarán unos barcos en coordenadas aleatorias \n La idea es ir introduciendo coordenadas y abatir los barcos del rival \n ¡Vamos allá!")

print("Se está creando el tablero...")
tablero_maquina = f.crear_tablero()
tablero_jugador = f.crear_tablero()

print("Antes de asignar barcos, te mostramos tu tablero vacío:")
print(tablero_jugador)
print("Antes de asignar barcos, te mostramos el tablero vacío de la máquina:")
print(tablero_maquina)

time.sleep(2)

tablero_maquina = f.generar_barcos(1,4,tablero_maquina)

tablero_jugador = f.generar_barcos(1,4,tablero_jugador)

time.sleep(2)
print("Una vez asignados los barcos, aquí está tu tablero:")

print(tablero_jugador)
print("Una vez asignados los barcos, aquí está el tablero de la máquina:")
print(tablero_maquina)

print("¡Empieza el juego!")

while True:
    f.turno_jugador(tablero_maquina)
    if f.check_barcos_destruidos(tablero_maquina):
        print("¡Has ganado!")
        break
    f.turno_maquina(tablero_jugador)
    if f.check_barcos_destruidos(tablero_jugador):
        print("¡Ha ganado la máquina!")
        break