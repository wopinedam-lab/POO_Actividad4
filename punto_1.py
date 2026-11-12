
import tkinter as tk
from tkinter import ttk


class ManejadorErrores:

    @staticmethod
    def division(numerador, denominador):
        mensajes = []

        try:
            mensajes.append("Ingresando al primer try")

            resultado = int(int(numerador) / int(denominador))

            mensajes.extend([
                f"Resultado de la división: {resultado}",
                "Después de la división"
            ])

        except ValueError:
            mensajes.append("Error: Debe ingresar números enteros válidos.")

        except ZeroDivisionError:
            mensajes.append("División por cero (Capturado)")

        finally:
            mensajes.append("Ingresando al primer finally")

        return mensajes

    @staticmethod
    def error_objeto():
        mensajes = []

        try:
            mensajes.append("Ingresando al segundo try")

            dato = None
            dato.upper()

            mensajes.append("Imprimiendo objeto")

        except ZeroDivisionError:
            mensajes.append("División por cero")

        except Exception:
            mensajes.append("Ocurrió una excepción (Capturado)")

        finally:
            mensajes.append("Ingresando al segundo finally")

        return mensajes

    @staticmethod
    def indice_texto():
        palabra = "Programación"

        try:
            caracter = palabra[14]
            return f"El carácter es: {caracter}"

        except IndexError:
            return "Índice de string por fuera del límite"

    @staticmethod
    def convertir_numero():
        mensajes = []

        try:
            valor = int("Número")
            mensajes.append(f"El número es: {valor}")

        except ValueError:
            mensajes.append("Excepción de formato de número (Capturado)")

        finally:
            mensajes.append("Ingresando al finally")

        return "\n".join(mensajes)


class Aplicacion(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Excepciones")

        principal = ttk.Frame(self, padding=12)
        principal.pack()

        # Título de la ventana
        ttk.Label(
            principal,
            text="Prueba de excepciones"
        ).grid(row=0, column=0, columnspan=2, pady=8)

        # Campos para ingresar los datos
        ttk.Label(
            principal,
            text="Numerador:"
        ).grid(row=1, column=0, sticky="w", pady=5)

        self.entrada_num = ttk.Entry(principal, width=28)
        self.entrada_num.grid(row=1, column=1, pady=5, padx=8)

        ttk.Label(
            principal,
            text="Denominador:"
        ).grid(row=2, column=0, sticky="w", pady=5)

        self.entrada_den = ttk.Entry(principal, width=28)
        self.entrada_den.grid(row=2, column=1, pady=5, padx=8)

        # Botones de pruebas independientes
        zona_botones = ttk.Frame(principal)
        zona_botones.grid(row=3, column=0, columnspan=2, pady=10)

        ttk.Button(
            zona_botones,
            text="Límite de string",
            command=lambda: self.mostrar(
                ManejadorErrores.indice_texto()
            )
        ).grid(row=0, column=0, padx=4)

        ttk.Button(
            zona_botones,
            text="Formato numérico",
            command=lambda: self.mostrar(
                ManejadorErrores.convertir_numero()
            )
        ).grid(row=0, column=1, padx=4)

        ttk.Button(
            zona_botones,
            text="Ejecutar excepciones",
            command=self.ejecutar_pruebas
        ).grid(row=0, column=2, padx=4)

        # Área donde aparecen los resultados
        ttk.Label(
            principal,
            text="Resultados:"
        ).grid(row=4, column=0, sticky="w", pady=4)

        self.resultado = tk.Text(
            principal,
            width=65,
            height=11,
            state="disabled"
        )
        self.resultado.grid(
            row=5, column=0, columnspan=2, pady=5
        )

    def mostrar(self, contenido):
        self.resultado.config(state="normal")
        self.resultado.delete("1.0", tk.END)
        self.resultado.insert(tk.END, contenido)
        self.resultado.config(state="disabled")

    def ejecutar_pruebas(self):
        datos = ManejadorErrores.division(
            self.entrada_num.get(),
            self.entrada_den.get()
        )

        datos.extend(
            [""] + ManejadorErrores.error_objeto()
        )

        self.mostrar("\n".join(datos))


if __name__ == "__main__":
    Aplicacion().mainloop()
