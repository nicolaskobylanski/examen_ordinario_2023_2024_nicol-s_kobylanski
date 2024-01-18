def jugar_partida():
    """
    Función que contiene el juego
    """
    tiempo_carlsen = 180  
    tiempo_nakamura = 180
    tiempo_movimiento = 10  

    turno_actual = "Carlsen"

    # Bucle principal del juego
    while True:
        print(f"\nTurno de {turno_actual}")
        print(f"Tiempo de Carlsen: {tiempo_carlsen} segundos")
        print(f"Tiempo de Nakamura: {tiempo_nakamura} segundos")

        movimiento = input("Ingrese el jugador que realizará el movimiento (Carlsen/Hikaru/Salir): ")

        # Condiciones de juego
        if movimiento.lower() == "salir":
            print(f"{turno_actual} ha abandonado la partida. ¡{turno_actual} pierde!")
            break

        if movimiento.lower() != turno_actual.lower():
            print("Movimiento incorrecto. Intente de nuevo.")
            continue

        if turno_actual == "Carlsen":
            tiempo_carlsen -= tiempo_movimiento
            if tiempo_carlsen <= 60:
                tiempo_movimiento = 5
        else:
            tiempo_nakamura -= tiempo_movimiento
            if tiempo_nakamura <= 60:
                tiempo_movimiento = 5

        if tiempo_carlsen <= 0:
            print("¡Tiempo agotado! Hikaru Nakamura gana la partida.")
            break
        elif tiempo_nakamura <= 0:
            print("¡Tiempo agotado! Magnus Carlsen gana la partida.")
            break

        turno_actual = "Hikaru" if turno_actual == "Carlsen" else "Carlsen"

if __name__ == "__main__":
    jugar_partida()
