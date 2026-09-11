nombres = []
telefonos = []
emails = []
direcciones = []


while True:
    menu = """

    ### ELIGE UNA OPCION ###
    1. Agregar un contacto.
    2. Busca un contacto.
    3. Eliminar un contacto.
    4. Ver contactos
    5. Salir
    """

    opcion_elegida = int(input(menu))

    if opcion_elegida == 1:
        nombre = input("Nombre del contacto: ")
        telefono = input("Telefono del contacto: ")
        email = input("Email del contacto: ")
        direccion = input("Direccion del contacto: ")
        nombres.append(nombre)
        telefonos.append(telefono)
        emails.append(email)
        direcciones.append(direccion)
        print(f"Contacto {nombre} guardado exitosamente")
    elif opcion_elegida == 2:
        nombre = input("Ingrese el nombre a buscar: ")
        if nombre in nombres:
            indice = nombres.index(nombre)
            print("="*10)
            print(f"Nombre: {nombres[indice]}")
            print(f"Telefono: {telefonos[indice]}")
            print(f"Email: {emails[indice]}")
            print(f"Dirección: {direcciones[indice]}")
            print("="*10)

        else:
            print("No se encuentra este contacto")
    elif opcion_elegida == 3:
        pass
    elif opcion_elegida == 4:
        for nombre, telefono, email, direccion in zip (nombres, telefonos, emails, direcciones):
            print(f"Nombre: {nombre}")
            print(f"Telefono: {telefono}")
            print(f"Email: {email}")
            print(f"Dirección: {direccion}")
    elif opcion_elegida == 5:
        print("Hasta aquí llegó el programa")
        break
    else:
        print("Opción invalida, intente de nuevo")