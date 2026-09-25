def temperatura():
    """
    Función que solicita al usuario ingresar la temperatura en grados Kelvin y la convierte a grados Fahrenheit.
    """
    try:
        kelvin = float(input("Ingrese la temperatura en grados Kelvin: "))
        celsius = kelvin - 273.15
        fahrenheit = (celsius * 9/5) + 32
        print(f"{kelvin}K son {fahrenheit}°F")
    except ValueError:
        print("Por favor, ingrese un valor numérico válido.")

def conversor(temperatura:float)->float:
    resultado= (temperatura - 273.15) * 9/5 + 32
    return round(resultado, 2)
print(conversor(15))
print(conversor(20))
    