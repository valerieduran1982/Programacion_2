
import tkinter as tk
from tkinter import messagebox


# ============================================================
# FUNCIONES QUE DEBES COMPLETAR
# ============================================================


def validar_stats(velocidad, tiro, pase, regate, defensa, fisico):
    """
    Recibe 6 valores numéricos (las estadísticas del jugador).
    Debe devolver True si TODOS están entre 0 y 99 (incluidos).
    Debe devolver False si al menos uno está fuera de ese rango.
    """
    # TODO: escribe tu código aquí
    pass


def calcular_overall(velocidad, tiro, pase, regate, defensa, fisico):
    """
    Recibe las 6 estadísticas del jugador.
    Debe devolver el promedio de las 6, redondeado a un número entero.
    """
    # TODO: escribe tu código aquí
    suma=velocidad+tiro+pase+regate+defensa+fisico
    promedio=suma/6
    return int(round(promedio))


def clasificar_jugador(overall):
    """
    Recibe el overall (número entero).
    Debe devolver un texto según estas reglas:
        overall < 60          -> "Bronce"
        60 <= overall < 70     -> "Plata"
        70 <= overall < 80     -> "Oro"
        80 <= overall < 90     -> "Leyenda"
        overall >= 90          -> "Ícono"
    """
    # TODO: escribe tu código aquí
    pass


def generar_tarjeta(nombre, overall, categoria):
    """
    Recibe el nombre del jugador, su overall y su categoría.
    Debe devolver un string con la tarjeta ya armada, por ejemplo:

        ⭐ TARJETA DE JUGADOR ⭐
        Nombre: Falcao
        Overall: 88
        Categoría: Leyenda

    (Puedes usar el formato que prefieras, pero debe incluir esos 3 datos)
    """
    # TODO: escribe tu código aquí
    pass


# ============================================================
# INTERFAZ GRÁFICA (ya está lista, no necesitas tocar esto)
# ============================================================


def on_generar():
    nombre = entry_nombre.get().strip()
    try:
        velocidad = int(entry_velocidad.get())
        tiro = int(entry_tiro.get())
        pase = int(entry_pase.get())
        regate = int(entry_regate.get())
        defensa = int(entry_defensa.get())
        fisico = int(entry_fisico.get())
    except ValueError:
        messagebox.showerror("Error", "Todas las estadísticas deben ser números.")
        return

    if not nombre:
        messagebox.showerror("Error", "Escribe el nombre del jugador.")
        return

    if not validar_stats(velocidad, tiro, pase, regate, defensa, fisico):
        messagebox.showerror("Error", "Las estadísticas deben estar entre 0 y 99.")
        return

    overall = calcular_overall(velocidad, tiro, pase, regate, defensa, fisico)
    categoria = clasificar_jugador(overall)
    tarjeta = generar_tarjeta(nombre, overall, categoria)

    resultado.config(state="normal")
    resultado.delete("1.0", tk.END)
    resultado.insert(
        tk.END, tarjeta if tarjeta else "⚠️ Las funciones aún no están completas."
    )
    resultado.config(state="disabled")


ventana = tk.Tk()
ventana.title("Generador de Tarjetas de Jugador")
ventana.geometry("380x560")
ventana.resizable(False, False)

campos = [
    ("Nombre", "entry_nombre"),
    ("Velocidad (0-99)", "entry_velocidad"),
    ("Tiro (0-99)", "entry_tiro"),
    ("Pase (0-99)", "entry_pase"),
    ("Regate (0-99)", "entry_regate"),
    ("Defensa (0-99)", "entry_defensa"),
    ("Físico (0-99)", "entry_fisico"),
]

entries = {}
for etiqueta, var_nombre in campos:
    tk.Label(ventana, text=etiqueta).pack(pady=(8, 0))
    entry = tk.Entry(ventana, width=30)
    entry.pack()
    entries[var_nombre] = entry

entry_nombre = entries["entry_nombre"]
entry_velocidad = entries["entry_velocidad"]
entry_tiro = entries["entry_tiro"]
entry_pase = entries["entry_pase"]
entry_regate = entries["entry_regate"]
entry_defensa = entries["entry_defensa"]
entry_fisico = entries["entry_fisico"]

tk.Button(
    ventana, text="Generar Tarjeta ⚽", command=on_generar, bg="#1e824c", fg="white"
).pack(pady=15)

resultado = tk.Text(ventana, height=8, width=40, state="disabled", bg="#f4f4f4")
resultado.pack(pady=10)

ventana.mainloop()
 