
import tkinter as tk
from tkinter import ttk


def convertir_entero(dato):
    try:
        return int(dato)
    except ValueError:
        raise ValueError("El tamaño debe ser un número entero válido.")


class CapacidadSuperada(Exception):
    pass


class Integrante:
    def __init__(self, nombres, apellidos):
        self.nombres = nombres
        self.apellidos = apellidos


class GrupoProgramacion:

    def __init__(self, identificacion, institucion, lenguaje, capacidad):
        if capacidad < 2 or capacidad > 3:
            raise ValueError(
                "El equipo debe tener entre 2 y 3 programadores."
            )

        self.identificacion = identificacion
        self.institucion = institucion
        self.lenguaje = lenguaje
        self.capacidad = capacidad
        self.integrantes = []

    def completo(self):
        return len(self.integrantes) == self.capacidad

    @staticmethod
    def comprobar_dato(texto, tipo):
        if texto.strip() == "":
            raise ValueError(f"El {tipo} no puede estar vacío.")

        if any(letra.isdigit() for letra in texto):
            raise ValueError(f"El {tipo} no puede tener dígitos.")

        if len(texto) >= 20:
            raise ValueError(
                f"El {tipo} debe tener menos de 20 caracteres."
            )

    def registrar_integrante(self, nombres, apellidos):
        if self.completo():
            raise CapacidadSuperada("El equipo está lleno.")

        self.comprobar_dato(nombres, "nombre")
        self.comprobar_dato(apellidos, "apellido")

        nuevo = Integrante(nombres, apellidos)
        self.integrantes.append(nuevo)

    def obtener_resumen(self):
        informacion = [
            f"Equipo: {self.identificacion} | Universidad: {self.institucion} | Lenguaje: {self.lenguaje}",
            f"Programadores ({len(self.integrantes)}/{self.capacidad}):"
        ]

        for persona in self.integrantes:
            informacion.append(
                f"  - {persona.nombres} {persona.apellidos}"
            )

        return "\n".join(informacion)


class InterfazMaraton(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Registro de maratón de programación")
        self.grupo = None

        principal = ttk.Frame(self, padding=12)
        principal.pack()

        ttk.Label(
            principal,
            text="GESTIÓN DE EQUIPOS",
            font=("Arial", 12, "bold")
        ).grid(row=0, column=0, columnspan=2, pady=10)

        # Panel de información del equipo
        panel_equipo = ttk.LabelFrame(
            principal,
            text="Información del equipo",
            padding=10
        )
        panel_equipo.grid(
            row=1, column=0, padx=7, pady=5, sticky="n"
        )

        self.nombre_grupo = self.crear_campo(
            panel_equipo, "Nombre del equipo:", 0
        )

        self.institucion = self.crear_campo(
            panel_equipo, "Universidad:", 1
        )

        self.lenguaje = self.crear_campo(
            panel_equipo, "Lenguaje:", 2
        )

        self.capacidad = self.crear_campo(
            panel_equipo, "Tamaño (2 o 3):", 3
        )

        ttk.Button(
            panel_equipo,
            text="Registrar equipo",
            command=self.registrar_equipo
        ).grid(row=4, column=0, columnspan=2, pady=10)

        # Panel para los programadores
        panel_personas = ttk.LabelFrame(
            principal,
            text="Agregar integrantes",
            padding=10
        )
        panel_personas.grid(
            row=1, column=1, padx=7, pady=5, sticky="n"
        )

        self.nombre_persona = self.crear_campo(
            panel_personas, "Nombre:", 0
        )

        self.apellido_persona = self.crear_campo(
            panel_personas, "Apellidos:", 1
        )

        ttk.Button(
            panel_personas,
            text="Añadir integrante",
            command=self.registrar_persona
        ).grid(row=2, column=0, columnspan=2, pady=10)

        # Panel de información final
        panel_resumen = ttk.LabelFrame(
            principal,
            text="Resumen del equipo",
            padding=10
        )
        panel_resumen.grid(
            row=2, column=0, columnspan=2, padx=7, pady=8
        )

        self.consola = tk.Text(
            panel_resumen,
            width=72,
            height=9,
            state="disabled"
        )
        self.consola.pack()

    def crear_campo(self, contenedor, texto, posicion):
        ttk.Label(
            contenedor,
            text=texto
        ).grid(row=posicion, column=0, sticky="w", pady=4)

        entrada = ttk.Entry(contenedor, width=23)
        entrada.grid(row=posicion, column=1, padx=5, pady=4)

        return entrada

    def mostrar(self, contenido):
        self.consola.config(state="normal")
        self.consola.delete("1.0", tk.END)
        self.consola.insert(tk.END, contenido)
        self.consola.config(state="disabled")

    def registrar_equipo(self):
        try:
            self.grupo = GrupoProgramacion(
                self.nombre_grupo.get(),
                self.institucion.get(),
                self.lenguaje.get(),
                convertir_entero(self.capacidad.get())
            )

            self.mostrar(
                "Equipo creado.\n\n" + self.grupo.obtener_resumen()
            )

        except ValueError as error:
            self.mostrar(f"Error: {error}")

    def registrar_persona(self):
        if self.grupo is None:
            self.mostrar("Primero debe crear el equipo.")
            return

        try:
            self.grupo.registrar_integrante(
                self.nombre_persona.get(),
                self.apellido_persona.get()
            )

            self.mostrar(self.grupo.obtener_resumen())

        except (ValueError, CapacidadSuperada) as error:
            self.mostrar(
                f"Error: {error}\n\n" +
                self.grupo.obtener_resumen()
            )


if __name__ == "__main__":
    InterfazMaraton().mainloop()
