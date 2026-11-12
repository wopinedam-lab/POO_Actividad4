
import math
import tkinter as tk
from tkinter import ttk


def leer_numero(cadena):
    try:
        return float(cadena)
    except ValueError:
        raise ValueError("Debe ingresar un número válido.")


class Procesador:

    @staticmethod
    def obtener_logaritmo(dato):
        if dato <= 0:
            raise ArithmeticError("El número debe ser positivo.")

        return math.log(dato)

    @staticmethod
    def obtener_raiz(dato):
        if dato <= 0:
            raise ArithmeticError("El número debe ser positivo.")

        return math.sqrt(dato)


class InterfazCalculos(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Operaciones matemáticas")

        marco = ttk.Frame(self, padding=15)
        marco.pack()

        # Encabezado
        ttk.Label(
            marco,
            text="Calculadora de operaciones",
            font=("Arial", 12, "bold")
        ).grid(row=0, column=0, columnspan=2, pady=10)

        # Panel izquierdo: entrada y resultado
        panel_entrada = ttk.LabelFrame(
            marco,
            text="Datos de entrada",
            padding=10
        )
        panel_entrada.grid(
            row=1, column=0, padx=8, pady=5, sticky="n"
        )

        ttk.Label(
            panel_entrada,
            text="Número:"
        ).pack(anchor="w", pady=4)

        self.numero_txt = ttk.Entry(
            panel_entrada,
            width=28
        )
        self.numero_txt.pack(pady=5)

        ttk.Label(
            panel_entrada,
            text="Resultado:"
        ).pack(anchor="w", pady=5)

        self.consola = tk.Text(
            panel_entrada,
            width=32,
            height=6,
            state="disabled"
        )
        self.consola.pack(pady=5)

        # Panel derecho: selección de operaciones
        panel_operaciones = ttk.LabelFrame(
            marco,
            text="Seleccionar operación",
            padding=12
        )
        panel_operaciones.grid(
            row=1, column=1, padx=8, pady=5, sticky="n"
        )

        ttk.Button(
            panel_operaciones,
            text="Calcular raíz cuadrada",
            command=lambda: self.procesar(
                Procesador.obtener_raiz, "√"
            )
        ).pack(fill="x", pady=10)

        ttk.Button(
            panel_operaciones,
            text="Calcular logaritmo",
            command=lambda: self.procesar(
                Procesador.obtener_logaritmo, "ln"
            )
        ).pack(fill="x", pady=10)

        # Información inferior
        ttk.Label(
            marco,
            text="Ingrese un valor y seleccione una operación."
        ).grid(
            row=2, column=0, columnspan=2, pady=10
        )

    def presentar_resultado(self, texto):
        self.consola.config(state="normal")
        self.consola.delete("1.0", tk.END)
        self.consola.insert(tk.END, texto)
        self.consola.config(state="disabled")

    def procesar(self, metodo, simbolo):
        try:
            valor = leer_numero(self.numero_txt.get())

            resultado = metodo(valor)

            mensaje = f"{simbolo}({valor}) = {resultado}"
            self.presentar_resultado(mensaje)

        except ArithmeticError as fallo:
            self.presentar_resultado(
                f"Excepción aritmética: {fallo}"
            )

        except ValueError as fallo:
            self.presentar_resultado(
                f"Entrada inválida: {fallo}"
            )


if __name__ == "__main__":
    InterfazCalculos().mainloop()
