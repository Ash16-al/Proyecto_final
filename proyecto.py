# Simulador de Ventas de Boletos de Cine

# Descripción: Un sistema donde los usuarios pueden comprar boletos para una película.
# Requisitos:
# Mostrar cartelera con películas disponibles.
# Permitir al usuario elegir una película y asientos.
# Calcular el precio total del boleto y confirmar la compra.

# Menú:
# Ver cartelera.
# Comprar boletos.
# Ver compras realizadas.
# Salir.

cartelera = ["Spider-Man: Far from home", "Toy story 4", "Frozen 2", "Godzilla 2: King of the monsters"]

# Mostrar la cartelera de películas disponibles
def mostrar_cartelera():
    print("🎬 Cartelera de Cine 🎬")
    for i, pelicula in enumerate(cartelera, 1):
        print(f"{i}. {pelicula}")

# -----------------------------------------------------------------------------------------------------------------

# Función para comprar boletos
def comprar_boletos():
    mostrar_cartelera()
    eleccion = int(input("Elige el número de la película que deseas ver: "))
    
    if 1 <= eleccion <= len(cartelera):
        pelicula_seleccionada = cartelera[eleccion - 1]
        print(f"\nHas seleccionado la película: {pelicula_seleccionada}")
        return pelicula_seleccionada
    else:
        print("Opción inválida. Intenta de nuevo.")
        return comprar_boletos()

#-------------------------------------------------------------------------------------------------------------------

# Función para realizar el pago
def pago_boletos():
    precio_boletos = 5.0
    cantidad_boletos = int(input("¿Cuántos boletos deseas comprar? "))
    total = cantidad_boletos * precio_boletos
    print(f"\nEl total de la compra es: ${total:.2f}")

    # Confirmación para continuar o cancelar
    while True:
        decision = input("Si deseas cancelar la compra, escribe 'cancelar'. Si deseas continuar, escribe 'seguir': ").lower()
        if decision == "cancelar":
            print("Compra cancelada. Volviendo al menú principal.")
            exit()  # Finaliza el programa
        elif decision == "seguir":
            return cantidad_boletos, total
        else:
            print("Opción inválida. Intenta de nuevo.")