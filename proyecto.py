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