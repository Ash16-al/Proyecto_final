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

historial_compras = []

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
            menu()  # Volver al menú 
            return None, None
        elif decision == "seguir":
            return cantidad_boletos, total
        else:
            print("Opción inválida. Intenta de nuevo.")

#--------------------------------------------------------------------------------------------------------------------

# Lista de asientos disponibles
asientos_disponibles = {
    "A": ["1", "2", "3", "4", "5"],
    "B": ["1", "2", "3", "4", "5"],
    "C": ["1", "2", "3", "4", "5"],
    "D": ["1", "2", "3", "4", "5"]
}

# Función para seleccionar asientos
def seleccionar_asientos():
    print("\nAsientos disponibles:")
    for fila, asientos in asientos_disponibles.items():
        print(f"{fila}: {', '.join(asientos)}")
    
    asientos_seleccionados = input("\nElige tus asientos (ejemplo: A1, B2): ").upper()
    asientos_list = [asiento.strip() for asiento in asientos_seleccionados.split(",")]
    
    # Verificar disponibilidad y marcar como ocupado
    for asiento in asientos_list:
        fila, numero = asiento[0], asiento[1:]
        if fila in asientos_disponibles and numero in asientos_disponibles[fila]:
            asientos_disponibles[fila].remove(numero)
        else:
            print(f"Asiento {asiento} no disponible o inválido.")
            return seleccionar_asientos()  # Intentar de nuevo

    return asientos_seleccionados

#--------------------------------------------------------------------------------------------------------------------

# Datos personales
def obtener_datos_cliente():
    print("\nSe pedirán algunos datos personales para proseguir con la compra.")
    nombre = input("Ingresa tu nombre completo: ")

    telefono = input("Ingresa tu número de teléfono: ")
    while len(telefono) > 9 or not telefono.isdigit():
        print("El número de teléfono no es válido. Debe tener máximo 8 dígitos y solo números.")
        telefono = input("Ingresa tu número de teléfono: ")
    
    # Validar correo electrónico 
    correo = input("Ingresa tu correo electrónico: ")
    while "@" not in correo or "." not in correo:
        print("El correo electrónico no es válido. Intenta de nuevo.")
        correo = input("Ingresa tu correo electrónico: ")

    print("\nDatos del cliente ingresados:")
    print(f"Nombre: {nombre}")
    print(f"Teléfono: {telefono}")
    print(f"Correo electrónico: {correo}")

#--------------------------------------------------------------------------------------------------------------------

#Función para confirmar la compra

def compra_realizada(pelicula, cantidad, total, asientos):
    compra = {
        "pelicula": pelicula,
        "cantidad": cantidad,
        "total": total,
        "asientos": asientos
    }
    historial_compras.append(compra)

    print("\n✅ ¡Compra realizada con éxito! 🎬")
    print(f"Película: {pelicula}")
    print(f"Boletos: {cantidad}")
    print(f"Asientos: {asientos}")
    print(f"Total: ${total:.2f}")
    print("Gracias por tu compra. ¡Disfruta la función! 🍿")

# Función para ver compras realizadas
def ver_compras_realizadas():
    if not historial_compras:
        print("\n📭 No hay compras registradas.")
    else:
        print("\n📜 Historial de compras:")
        for i, compra in enumerate(historial_compras, 1):
            print(f"{i}. {compra['pelicula']} - {compra['cantidad']} boletos - Asientos: {compra['asientos']} - Total: ${compra['total']:.2f}")


#--------------------------------------------------------------------------------------------------------------------


def simulador_cine():
    pelicula = comprar_boletos()  # Primero, seleccionar película
    cantidad, total = pago_boletos()  # Luego, hacer el pago
    asientos = seleccionar_asientos()  # Después, seleccionar los asientos
    obtener_datos_cliente()  # Solicitar los datos del cliente
    compra_realizada(pelicula, cantidad, total, asientos)  # Confirmar la compra

#----------------------------------------------------------------------------------------------------------------------

#Menu interactivo para que pueda escoger el usuario

def menu():
    while True:
        print("\n🎟️ Bienvenido al Simulador de Ventas de Boletos 🎟️")
        print("1. Ver cartelera")
        print("2. Comprar boletos")
        print("3. Ver compras realizadas")
        print("4. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_cartelera()
        elif opcion == "2":
            simulador_cine()
        elif opcion == "3":
            ver_compras_realizadas()
        elif opcion == "4":
            print("Gracias por visitarnos. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

# Llamar al menú en lugar de ejecutar simulador_cine() directamente
menu()