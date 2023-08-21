import tkinter as tk
from tkinter import ttk


ventana = tk.Tk()
ventana.title("Ley De Ohm")
ventana.geometry("500x300")

nb = ttk.Notebook(ventana)
nb.pack(fill='both', expand='yes')

p1 = ttk.Frame(nb)
p2 = ttk.Frame(nb)
p3 = ttk.Frame(nb)
nb.add(p1, text="Voltaje")
nb.add(p2, text="Amperaje")
nb.add(p3, text="Resistencia")

def calcular_voltaje():
    try:
        primer_valor = float(texto_primer_valor_voltaje.get())
        segundo_valor = float(texto_segundo_valor_resistencia.get())

        if segundo_valor != 0:
            resultadop1 = primer_valor * segundo_valor
            resultado_label_voltaje.config(text="Resultado: " + str(resultadop1))
        else:
            resultado_label_voltaje.config(text="No es posible dividir por 0")

    except ValueError:
        resultado_label_voltaje.config(text="Por favor, ingrese solo números válidos")

def calcular_amperaje():
    try:
        primer_valor = float(texto_primer_valor_amperaje.get())
        segundo_valor = float(texto_segundo_valor_resistencia_amperaje.get())

        if segundo_valor != 0:
            resultado = primer_valor / segundo_valor
            resultado_label_amperaje.config(text="Resultado: " + str(resultado))
        else:
            resultado_label_amperaje.config(text="No es posible dividir por 0")

    except ValueError:
        resultado_label_amperaje.config(text="Por favor, ingrese solo números válidos")

def calcular_resistencia():
    try:
        primer_valor = float(texto_primer_valor_voltaje_resistencia.get())
        segundo_valor = float(texto_segundo_valor_amperes_resistencia.get())

        if segundo_valor != 0:
            resultado = primer_valor / segundo_valor
            resultado_label_resistencia.config(text="Resultado: " + str(resultado))
        else:
            resultado_label_resistencia.config(text="No es posible dividir por 0")

    except ValueError:
        resultado_label_resistencia.config(text="Por favor, ingrese solo números válidos")



# Pestaña 1
ttk.Label(p1, text="Voltaje", foreground="Red").place(x=200, y=20)

ttk.Label(p1, text="Ingrese El Primer Valor En Amperes: ").place(x=10, y=50)
texto_primer_valor_voltaje = tk.Entry(p1)
texto_primer_valor_voltaje.place(x=200, y=50)

ttk.Label(p1, text="Ingrese El Segundo Valor En Ohms: ").place(x=10, y=100)
texto_segundo_valor_resistencia = tk.Entry(p1)
texto_segundo_valor_resistencia.place(x=200, y=100)

resultado_label_voltaje = tk.Label(p1, text="")
resultado_label_voltaje.pack()

ttk.Button(p1, text="Calcular", command=calcular_voltaje).place(x=200, y=200)

# Pestaña 2
ttk.Label(p2, text="Amperaje", foreground="Red").place(x=200, y=20)

ttk.Label(p2, text="Ingrese El Primer Valor En Voltios: ").place(x=10, y=50)
texto_primer_valor_amperaje = tk.Entry(p2)
texto_primer_valor_amperaje.place(x=200, y=50)

ttk.Label(p2, text="Ingrese El Segundo Valor En Ohms: ").place(x=10, y=100)
texto_segundo_valor_resistencia_amperaje = tk.Entry(p2)
texto_segundo_valor_resistencia_amperaje.place(x=200, y=100)

resultado_label_amperaje = tk.Label(p2, text="")
resultado_label_amperaje.pack()

ttk.Button(p2, text="Calcular", command=calcular_amperaje).place(x=200, y=200)

# Pestaña 3
ttk.Label(p3, text="Resistencia", foreground="Red").place(x=200, y=20)

ttk.Label(p3, text="Ingrese El Primer Valor En Voltaje: ").place(x=10, y=50)
texto_primer_valor_voltaje_resistencia = tk.Entry(p3)
texto_primer_valor_voltaje_resistencia.place(x=200, y=50)

ttk.Label(p3, text="Ingrese El Segundo Valor En Amperes: ").place(x=10, y=100)
texto_segundo_valor_amperes_resistencia = tk.Entry(p3)
texto_segundo_valor_amperes_resistencia.place(x=200, y=100)

resultado_label_resistencia = tk.Label(p3, text="")
resultado_label_resistencia.pack()

ttk.Button(p3, text="Calcular", command=calcular_resistencia).place(x=200, y=200)

ventana.mainloop()
