from pokemon import Pokemon

def main(): # función para ejecutar el "juego"
    eevee = Pokemon("Eevee", "Normal", 5, 55, 20) # se crean las instancias
    charmander = Pokemon("Charmander", "Fuego", 2, 22, 8)

    print(f"Estado de Eevee antes del ataque: {eevee.get_hp()}") #Imprime los puntos de vida de cada Pókemon
    print(f"Estado de Charmander antes del ataque: {charmander.get_hp()}")

    eevee.atacar(charmander) # se ataca

    print(f"Vida de Charmander despúes del ataque: {charmander.get_hp()}") # se muestra la vida luego del ataque

main()