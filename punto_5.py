
import tkinter as tk
from tkinter import ttk, filedialog


class GestorDocumentos:

    @staticmethod
    def cargar_contenido(direccion):
        with open(direccion, "r", encoding="utf-8") as documento:
            contenido = documento.read()

        return contenido


class AplicacionArchivos(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Visor de documentos")

        estructura = ttk.Frame(self, padding=12)
        estructura.pack()

        # Encabezado
        ttk.Label(
            estructura,
            text="LECTOR DE ARCHIVOS DE TEXTO",
            font=("Arial", 12, "bold")
        ).grid(row=0, column=0, columnspan=2, pady=10)

        # Área para visualizar el contenido
        zona_lectura = ttk.LabelFrame(
            estructura,
            text="Contenido del documento",
            padding=8
        )
        zona_lectura.grid(
            row=1, column=0, padx=7, pady=5
        )

        self.contenido = tk.Text(
            zona_lectura,
            width=65,
            height=16,
            state="disabled"
        )
        self.contenido.pack()

        # Panel de controles
        zona_control = ttk.LabelFrame(
            estructura,
            text="Opciones",
            padding=12
        )
        zona_control.grid(
            row=1, column=1, padx=7, pady=5, sticky="n"
        )

        ttk.Label(
            zona_control,
            text="Seleccione un documento\npara visualizar su contenido."
        ).pack(pady=8)

        ttk.Button(
            zona_control,
            text="Buscar archivo TXT",
            command=self.seleccionar_documento
        ).pack(fill="x", pady=8)

        ttk.Button(
            zona_control,
            text="Limpiar pantalla",
            command=lambda: self.actualizar("")
        ).pack(fill="x", pady=8)

        self.estado = ttk.Label(
            zona_control,
            text="Esperando archivo..."
        )
        self.estado.pack(pady=12)

    def actualizar(self, texto):
        self.contenido.config(state="normal")
        self.contenido.delete("1.0", tk.END)
        self.contenido.insert(tk.END, texto)
        self.contenido.config(state="disabled")

    def seleccionar_documento(self):
        archivo = filedialog.askopenfilename(
            filetypes=[("Archivos de texto", "*.txt")]
        )

        if not archivo:
            return

        try:
            texto = GestorDocumentos.cargar_contenido(archivo)

            self.actualizar(texto)
            self.estado.config(text="Archivo leído correctamente.")

        except (OSError, UnicodeDecodeError):
            self.actualizar("No se pudo leer el archivo.")
            self.estado.config(text="Error al abrir el documento.")


if __name__ == "__main__":
    AplicacionArchivos().mainloop()
