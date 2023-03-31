import random


def monty_hall(cambiarPuerta):
    """ 
    
    Simula el problema de monty hall, donde el jugador debe elegir una de las tres puertas.
    Detras de una de las cuales hay un coche. 
        
    Parametro:
       
    cambiarPuerta: Boolean
    
    True: si el jugador decide cambiar la puerta despues de que el presentador abra una de las otras dos puertas.
    False: si el jugador decide quedarse con la puerta original.
    
    Returns: Boolean
    
    True si el jugador gano el auto
    False si no lo hizo
    
    
    //TO-DO LIST
    [ ] - Arreglar las graficas (No me conoce el import matplotlib)
    [ ] - Hacer el informe
    [ ] - 
        
    """
    print("Se arma el escenario")
       
    #Crear las tres puertas
    puertas = [0,0,0]
    print("Se ponen las puertas vacias para ubicar las cabras y el auto.")
    #Colocar el coche random
    coche = random.randint(0,2)
    print("Se coloca el auto en la puerta numero ", coche+1)
    print("En el sistema se guarda puertas[",coche,"] = 1")

    puertas[coche] = 1
    print("Se coloca las cabras en las otras puertas")

    
    #Jugador elige puerta aleatoria
    eleccionDelJugador = random.randint(0,2)
    print("Empieza el juego!")
    print("El jugador elige la puerta numero ", eleccionDelJugador+1)
    
    #El presentador debe abrir una puerta con una cabra que no haya sido elegida
    for i in range(3):
        if i != eleccionDelJugador and puertas[i] != 1:
            presentadorAbre = i
            print("El presentador abre la puerta numero ", i+1)
            break
    
    # Si el jugador cambia de puerta, elige la otra puerta que no ha sido elegida ni abierta
    if cambiarPuerta:
        for i in range(3):
            if i != eleccionDelJugador and i != presentadorAbre:
                eleccionDelJugador = i
                print("El jugador cambia a la puerta numero ", i+1)
                break
    
    # Devolver True si el jugador gana el coche, False sino lo hizo
    print("¿El jugador se gano el auto? ", puertas[eleccionDelJugador] == 1)
    return puertas[eleccionDelJugador] == 1



###
### Ejecutar la funci´on 1.000, 10.000 y 100.000 veces para la estrategia de cambio de puerta y cuente
### la cantidad de veces que el juego resulta en que el participante gana el auto. Repita esta parte para
### la estrategia donde no se cambia la puerta.
###


num_intentos = 1000
num_exitos = 0

print("Simulo veces ", num_intentos," veces.")

for i in range(num_intentos):
    if monty_hall(True):
        num_exitos += 1
        
frecuenciaVictorias = num_exitos / num_intentos
###
###   Calcular las frecuencias relativas del evento “el participante gana el auto” en cada una de las dos
###   estrategias a partir de los resultados de la parte anterior.
###   HECHO EN CADA EXPERIMENTO.

print("Frecuencias relativas:")
print("frecuenciaVictorias: ", frecuenciaVictorias)
print("Con la estrategia de cambiar de puerta, el jugador gano el coche en ", num_exitos, "de", num_intentos, "intentos.")
print("El porcentaje de ganar el auto es de ", round((num_exitos/num_intentos)*100,2), " %.")


num_intentos1 = 10000
num_exitos1 = 0

print("Simulo veces ", num_intentos1," veces.")


for i in range(num_intentos1):
    if monty_hall(True):
        num_exitos1 += 1
        
frecuenciaVictorias1 = num_exitos1 / num_intentos1
print("Frecuencias relativas:")
print("frecuenciaVictorias1: ", frecuenciaVictorias1)
print("Con la estrategia de cambiar de puerta, el jugador gano el coche en ", num_exitos1, "de", num_intentos1, "intentos.")
print("El porcentaje de ganar el auto es de ", round((num_exitos1/num_intentos1)*100,2), " %.")



num_intentos2 = 100000
num_exitos2 = 0

print("Simulo veces ", num_intentos2," veces.")

for i in range(num_intentos2):
    if monty_hall(True):
        num_exitos2 += 1
        
frecuenciaVictorias2 = num_exitos2 / num_intentos2
print("Frecuencias relativas:")
print("frecuenciaVictorias2: ", frecuenciaVictorias2)
print("Con la estrategia de cambiar de puerta, el jugador gano el coche en ", num_exitos2, "de", num_intentos2, "intentos.")
print("El porcentaje de ganar el auto es de ", round((num_exitos2/num_intentos2)*100,2), " %.")



print("PARTE 4")
print("Cantidad de intentos ",num_intentos)
print("El porcentaje de ganar el auto es de ", round((num_exitos/num_intentos)*100,2), " %.")

print("Cantidad de intentos ",num_intentos1)
print("El porcentaje de ganar el auto es de ", round((num_exitos1/num_intentos1)*100,2), " %.")

print("Cantidad de intentos ",num_intentos2)
print("El porcentaje de ganar el auto es de ", round((num_exitos2/num_intentos2)*100,2), " %.")




    
    