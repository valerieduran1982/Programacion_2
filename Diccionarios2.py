yo = {"nombre": "Valerie", "Edad": 18, "es_estudiante": True}
print(yo["nombre"])

yo["nombre"] = "Valerie Durán"
print(yo)

yo["Ciudad"] = "Barranquilla"
yo["Telefono"] = "+57 3245598257"
print(yo)

yo2 = {"rh": "o+", "profesión": "Cientifico de datos"}
yo.update(yo2)
print(yo)

eliminado = yo.pop("rh")
print(eliminado)

eliminado2 = yo.popitem()
print(eliminado2)