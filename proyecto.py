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