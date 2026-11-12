
import tkinter as tk
from tkinter import ttk


def obtener_entero(dato):
    try:
        return int(dato)
    except ValueError:
        raise ValueError("La edad debe ser un número entero válido.")


class RegistroVendedor:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = 0

    def asignar_edad(self, cantidad):
        if cantidad < 0 or cantidad > 120:
            raise ValueError(
                "La edad no puede ser negativa ni mayor a 120."
            )

        if cantidad < 18:
            raise ValueError(
                "El vendedor debe ser mayor de 18 años."
            )

        self.edad = cantidad

    def consultar_informacion(self):
        return (
            f"Nombre del vendedor = {self.nombre}\n"
            f"Apellidos del vendedor = {self.apellido}\n"
            f"Edad del vendedor = {self.edad}"
        )


class VentanaRegistro(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Registro de vendedores")

        base = ttk.Frame(self, padding=15)
        base.pack()

        # Sección izquierda: información personal
        datos = ttk.LabelFrame(
            base,
            text="Datos personales",
            padding=12
        )
        datos.grid(row=0, column=0, padx=8, pady=5, sticky="n")

        ttk.Label(datos, text="Nombre").grid(
            row=0, column=0, sticky="w", pady=5
        )

        self.nombre_txt = ttk.Entry(datos, width=25)
        self.nombre_txt.grid(row=0, column=1, pady=5, padx=5)

        ttk.Label(datos, text="Apellidos").grid(
            row=1, column=0, sticky="w", pady=5
        )

        self.apellido_txt = ttk.Entry(datos, width=25)
        self.apellido_txt.grid(row=1, column=1, pady=5, padx=5)

        ttk.Label(datos, text="Edad").grid(
            row=2, column=0, sticky="w", pady=5
        )

        self.edad_txt = ttk.Entry(datos, width=25)
        self.edad_txt.grid(row=2, column=1, pady=5, padx=5)

        ttk.Button(
            datos,
            text="Registrar vendedor",
            command=self.crear_registro
        ).grid(
            row=3, column=0, columnspan=2, pady=12
        )

        # Sección derecha: información del registro
        resultado = ttk.LabelFrame(
            base,
            text="Información del registro",
            padding=10
        )
        resultado.grid(row=0, column=1, padx=8, pady=5)

        self.mensaje = tk.Text(
            resultado,
            width=38,
            height=10,
            state="disabled"
        )
        self.mensaje.pack()

    def presentar(self, texto):
        self.mensaje.config(state="normal")
        self.mensaje.delete("1.0", tk.END)
        self.mensaje.insert(tk.END, texto)
        self.mensaje.config(state="disabled")

    def crear_registro(self):
        try:
            persona = RegistroVendedor(
                self.nombre_txt.get(),
                self.apellido_txt.get()
            )

            edad = obtener_entero(self.edad_txt.get())
            persona.asignar_edad(edad)

            texto = "Vendedor creado:\n\n"
            texto += persona.consultar_informacion()

            self.presentar(texto)

        except ValueError as problema:
            self.presentar(f"Error: {problema}")


if __name__ == "__main__":
    VentanaRegistro().mainloop()
