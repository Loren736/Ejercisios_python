import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
from datetime import datetime

# --- CONFIGURACIÓN ESTÉTICA (COLORES Y FUENTES) ---
COLOR_FONDO = "#F3F4F6"
COLOR_TARJETA = "#FFFFFF"
COLOR_PRIMARIO = "#4F46E5"  # Índigo
COLOR_EXITO = "#10B981"    # Esmeralda
COLOR_PELIGRO = "#EF4444"   # Rojo
COLOR_TEXTO = "#111827"
COLOR_TEXTO_GRIS = "#6B7280"

# --- LÓGICA DE BASE DE DATOS ---
def iniciar_db():
    with sqlite3.connect("presupuesto.db") as conexion:
        conexion.execute('''CREATE TABLE IF NOT EXISTS movimientos (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            tipo TEXT, monto REAL, fecha TEXT)''')

def registrar_en_db(tipo, monto):
    ahora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with sqlite3.connect("presupuesto.db") as conexion:
        conexion.execute("INSERT INTO movimientos (tipo, monto, fecha) VALUES (?, ?, ?)", (tipo, monto, ahora))

def obtener_saldo():
    with sqlite3.connect("presupuesto.db") as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT tipo, monto FROM movimientos")
        movimientos = cursor.fetchall()
        return sum(m if t == "Ingreso" else -m for t, m in movimientos)

def eliminar_registro_db(id_registro):
    with sqlite3.connect("presupuesto.db") as conexion:
        conexion.execute("DELETE FROM movimientos WHERE id = ?", (id_registro,))

# --- INTERFAZ GRÁFICA PROFESIONAL ---
class AppPresupuesto:
    def __init__(self, root):
        self.root = root
        self.root.title("MyWallet - Pro")
        self.root.geometry("450x600")
        self.root.configure(bg=COLOR_FONDO)

        # Contenedor principal con margen
        self.main_frame = tk.Frame(root, bg=COLOR_FONDO, padx=30, pady=30)
        self.main_frame.pack(expand=True, fill="both")

        # Encabezado
        tk.Label(self.main_frame, text="MI BALANCE", font=("Helvetica", 10, "bold"), 
                 bg=COLOR_FONDO, fg=COLOR_TEXTO_GRIS).pack(anchor="w")

        # Tarjeta de Saldo Principal
        self.card = tk.Frame(self.main_frame, bg=COLOR_TARJETA, padx=20, pady=25, 
                             highlightthickness=1, highlightbackground="#E5E7EB")
        self.card.pack(fill="x", pady=(5, 25))

        self.saldo_var = tk.StringVar(value=f"${obtener_saldo():,.2f}")
        self.lbl_saldo = tk.Label(self.card, textvariable=self.saldo_var, font=("Helvetica", 32, "bold"), 
                                  bg=COLOR_TARJETA, fg=COLOR_TEXTO)
        self.lbl_saldo.pack()

        # Entrada de Monto
        tk.Label(self.main_frame, text="Monto de operación", font=("Helvetica", 9), 
                 bg=COLOR_FONDO, fg=COLOR_TEXTO_GRIS).pack(anchor="w")
        
        self.entry_monto = tk.Entry(self.main_frame, font=("Helvetica", 18), justify='center', 
                                    bd=0, highlightthickness=1, highlightbackground="#D1D5DB")
        self.entry_monto.pack(fill="x", ipady=10, pady=(5, 25))

        # Botones de Acción
        self.crear_boton("➕ INGRESAR DINERO", COLOR_EXITO, self.ingresar)
        self.crear_boton("➖ REGISTRAR GASTO", COLOR_PELIGRO, self.gastar)
        
        # Separador visual
        tk.Frame(self.main_frame, height=1, bg="#D1D5DB").pack(fill="x", pady=20)

        self.crear_boton("📜 VER HISTORIAL", COLOR_PRIMARIO, self.mostrar_historial)

    def crear_boton(self, texto, color, comando):
        btn = tk.Button(self.main_frame, text=texto, font=("Helvetica", 10, "bold"), 
                        bg=color, fg="white", bd=0, height=2, cursor="hand2", 
                        activebackground=color, command=comando)
        btn.pack(fill="x", pady=5)

    def actualizar_pantalla(self):
        saldo = obtener_saldo()
        self.saldo_var.set(f"${saldo:,.2f}")
        self.entry_monto.delete(0, tk.END)

    def ingresar(self):
        try:
            monto = float(self.entry_monto.get().replace(',', '.'))
            if monto <= 0: raise ValueError
            registrar_en_db("Ingreso", monto)
            self.actualizar_pantalla()
        except ValueError:
            messagebox.showerror("Error", "Monto inválido. Ingrese solo números.")

    def gastar(self):
        try:
            monto = float(self.entry_monto.get().replace(',', '.'))
            if monto > obtener_saldo():
                messagebox.showwarning("Saldo", "No tienes fondos suficientes.")
                return
            if monto <= 0: raise ValueError
            registrar_en_db("Gasto", monto)
            self.actualizar_pantalla()
        except ValueError:
            messagebox.showerror("Error", "Monto inválido.")

    def mostrar_historial(self):
        ventana_h = tk.Toplevel(self.root)
        ventana_h.title("Historial de Movimientos")
        ventana_h.geometry("600x450")
        ventana_h.configure(bg=COLOR_TARJETA)

        # Estilo de la tabla
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", font=("Helvetica", 10), rowheight=25, background=COLOR_TARJETA)
        style.configure("Treeview.Heading", font=("Helvetica", 10, "bold"), background="#F9FAFB")

        # Crear Tabla
        columnas = ("ID", "Tipo", "Monto", "Fecha")
        tabla = ttk.Treeview(ventana_h, columns=columnas, show="headings")
        
        for col in columnas:
            tabla.heading(col, text=col)
            tabla.column(col, anchor="center")
        
        tabla.column("ID", width=50) # Columna ID pequeña

        def cargar_datos():
            for item in tabla.get_children(): tabla.delete(item)
            with sqlite3.connect("presupuesto.db") as con:
                cursor = con.cursor()
                cursor.execute("SELECT * FROM movimientos ORDER BY id DESC")
                for fila in cursor.fetchall():
                    # Formatear el monto en la tabla para que se vea profesional
                    fila_lista = list(fila)
                    fila_lista[2] = f"${fila_lista[2]:,.2f}"
                    tabla.insert("", tk.END, values=fila_lista)

        def eliminar_seleccionado():
            item = tabla.selection()
            if not item:
                messagebox.showwarning("Aviso", "Selecciona una fila para eliminar.")
                return
            
            valores = tabla.item(item)['values']
            id_reg = valores[0]
            
            if messagebox.askyesno("Confirmar", f"¿Eliminar el registro #{id_reg}?"):
                eliminar_registro_db(id_reg)
                cargar_datos()
                self.actualizar_pantalla()

        # Botón Eliminar dentro de historial
        btn_del = tk.Button(ventana_h, text="🗑️ ELIMINAR SELECCIONADO", bg=COLOR_PELIGRO, fg="white",
                            font=("Helvetica", 9, "bold"), bd=0, padx=10, pady=10, command=eliminar_seleccionado)
        
        cargar_datos()
        tabla.pack(expand=True, fill="both", padx=20, pady=(20, 10))
        btn_del.pack(fill="x", padx=20, pady=20)

if __name__ == "__main__":
    iniciar_db()
    root = tk.Tk()
    
    # Intento de mejorar la nitidez en pantallas modernas
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass
        
    app = AppPresupuesto(root)
    root.mainloop()