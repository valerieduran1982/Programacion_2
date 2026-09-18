nombres = []
telefonos = []
emails = []
direcciones = []

contactos = {}

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
        contactos[nombre]={"telefono": telefono, "email": email, "direccion": direccion}
        print(f"Contacto {nombre} guardado exitosamente")
    elif opcion_elegida == 2:
        nombre = input("Ingrese el nombre a buscar: ").lower()
        if nombre in contactos:
            print("="*10)
            print(contactos[nombre])
            print("="*10)

        else:
            print("No se encuentra este contacto")
    elif opcion_elegida == 3:
        nombre = input("Ingrese el nombre del contacto a eliminar: ").lower()
        if nombre in contactos:
            eliminados = contactos.pop(nombre)
            print(eliminados)
        else:
            print("No se encuentra este contacto")
    elif opcion_elegida == 4:
        for i, key in enumerate (contactos):
            print(i+1, "-", key)
    elif opcion_elegida == 5:
        print("Hasta aquí llegó el programa")
        break
    else:
        print("Opción invalida, intente de nuevo")