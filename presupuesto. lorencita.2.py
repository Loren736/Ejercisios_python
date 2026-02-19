import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
from datetime import datetime

# --- CONFIGURACIÓN DE LA BASE DE DATOS ---
def iniciar_db():
    conexion = sqlite3.connect("presupuesto.db")
    cursor = conexion.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS movimientos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        tipo TEXT,
                        monto REAL,
                        fecha TEXT)''')
    conexion.commit()
    conexion.close()

def registrar_en_db(tipo, monto):
    conexion = sqlite3.connect("presupuesto.db")
    cursor = conexion.cursor()
    ahora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    cursor.execute("INSERT INTO movimientos (tipo, monto, fecha) VALUES (?, ?, ?)", (tipo, monto, ahora))
    conexion.commit()
    conexion.close()

def obtener_saldo():
    conexion = sqlite3.connect("presupuesto.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT tipo, monto FROM movimientos")
    movimientos = cursor.fetchall()
    conexion.close()
    
    saldo = 0.0
    for tipo, monto in movimientos:
        if tipo == "Ingreso":
            saldo += monto
        else:
            saldo -= monto
    return saldo

def borrar_historial_db():
    conexion = sqlite3.connect("presupuesto.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM movimientos") # Borra todos los datos
    conexion.commit()
    conexion.close()

# --- INTERFAZ GRÁFICA ---
class AppPresupuesto:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Presupuesto Pro")
        self.root.geometry("400x600") # Un poco más alto para el nuevo botón

        self.saldo_var = tk.StringVar(value=f"Saldo: ${obtener_saldo():.2f}")

        # UI - Diseño Principal
        tk.Label(root, text="MI BILLETERA", font=("Arial", 14, "bold"), fg="gray").pack(pady=10)
        self.label_saldo = tk.Label(root, textvariable=self.saldo_var, font=("Arial", 22, "bold"), pady=10)
        self.label_saldo.pack()

        tk.Label(root, text="Monto a operar:", font=("Arial", 10)).pack(pady=5)
        self.entry_monto = tk.Entry(root, font=("Arial", 14), justify='center')
        self.entry_monto.pack(pady=5)

        # Botones Principales
        tk.Button(root, text="➕ Ingresar Dinero", bg="#28a745", fg="white", font=("Arial", 10, "bold"), 
                  width=25, height=2, command=self.ingresar).pack(pady=10)
        
        tk.Button(root, text="➖ Registrar Gasto", bg="#dc3545", fg="white", font=("Arial", 10, "bold"), 
                  width=25, height=2, command=self.gastar).pack(pady=10)
        
        tk.Button(root, text="📜 Ver Historial", bg="#007bff", fg="white", font=("Arial", 10, "bold"), 
                  width=25, height=2, command=self.mostrar_historial).pack(pady=10)

        # Botón para Borrar Historial (Diferente estilo para advertir peligro)
        tk.Button(root, text="🗑️ Borrar Todo el Historial", bg="#353b41", fg="white", font=("Arial", 9), 
                  width=25, command=self.confirmar_borrado).pack(pady=20)

    def actualizar_pantalla(self):
        self.saldo_var.set(f"Saldo: ${obtener_saldo():.2f}")
        self.entry_monto.delete(0, tk.END)

    def ingresar(self):
        try:
            monto = float(self.entry_monto.get())
            if monto <= 0: raise ValueError
            registrar_en_db("Ingreso", monto)
            self.actualizar_pantalla()
        except ValueError:
            messagebox.showerror("Error", "Introduce un número válido.")

    def gastar(self):
        try:
            monto = float(self.entry_monto.get())
            saldo_actual = obtener_saldo()
            if monto > saldo_actual:
                messagebox.showwarning("Saldo Insuficiente", "No tienes fondos suficientes.")
            elif monto <= 0:
                raise ValueError
            else:
                registrar_en_db("Gasto", monto)
                self.actualizar_pantalla()
        except ValueError:
            messagebox.showerror("Error", "Introduce un número válido.")

    def confirmar_borrado(self):
        # Ventana de confirmación
        respuesta = messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas borrar TODO el historial?\nEsta acción no se puede deshacer.")
        if respuesta:
            borrar_historial_db()
            self.actualizar_pantalla()
            messagebox.showinfo("Borrado", "El historial ha sido eliminado y el saldo se ha reiniciado.")

    def mostrar_historial(self):
        ventana_h = tk.Toplevel(self.root)
        ventana_h.title("Historial Detallado")
        ventana_h.geometry("600x400")

        columnas = ("ID", "Tipo", "Monto", "Fecha y Hora")
        tabla = ttk.Treeview(ventana_h, columns=columnas, show="headings")
        
        tabla.heading("ID", text="ID")
        tabla.column("ID", width=50, anchor="center")
        tabla.heading("Tipo", text="Tipo")
        tabla.column("Tipo", width=100, anchor="center")
        tabla.heading("Monto", text="Monto")
        tabla.column("Monto", width=100, anchor="center")
        tabla.heading("Fecha y Hora", text="Fecha y Hora Exacta")
        tabla.column("Fecha y Hora", width=200, anchor="center")

        conexion = sqlite3.connect("presupuesto.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM movimientos ORDER BY id DESC")
        for fila in cursor.fetchall():
            tabla.insert("", tk.END, values=fila)
        conexion.close()

        tabla.pack(expand=True, fill="both", padx=10, pady=10)

# --- EJECUCIÓN ---
if __name__ == "__main__":
    iniciar_db()
    root = tk.Tk()
    app = AppPresupuesto(root)
    root.mainloop()