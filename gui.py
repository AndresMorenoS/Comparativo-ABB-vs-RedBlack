"""
Interfaz Gráfica Completa - ABB vs Red-Black Tree
"""
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from controller import PerformanceController
from model import BinarySearchTree, RedBlackTree


class TreeComparisonGUI:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Comparativo: ABB vs Red-Black Tree")
        self.root.geometry("1200x800")
        
        self.controller = PerformanceController()
        self.data_type_var = tk.StringVar(value="random")
        self.size_var = tk.StringVar(value="100,300,500,800,1000")
        self.manual_data_var = tk.StringVar(value="50,30,70,20,40,60,80")
        self.results = None
        
        self.setup_ui()
        
    def setup_ui(self):
        config_frame = ttk.LabelFrame(self.root, text="⚙️ Configuración", padding=10)
        config_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Label(config_frame, text="Tipo de datos:").grid(row=0, column=0, sticky=tk.W, padx=5)
        ttk.Radiobutton(config_frame, text="Aleatorios", 
                       variable=self.data_type_var, value="random").grid(row=0, column=1, sticky=tk.W)
        ttk.Radiobutton(config_frame, text="Ordenados", 
                       variable=self.data_type_var, value="ordered").grid(row=0, column=2, sticky=tk.W)
        ttk.Radiobutton(config_frame, text="Inversos", 
                       variable=self.data_type_var, value="reverse").grid(row=0, column=3, sticky=tk.W)
        
        ttk.Label(config_frame, text="Tamaños (separados por comas):").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        size_entry = ttk.Entry(config_frame, textvariable=self.size_var, width=40)
        size_entry.grid(row=1, column=1, columnspan=3, sticky=tk.W, pady=5)
        
        ttk.Button(config_frame, text="🚀 Ejecutar Comparativo", 
                  command=self.run_comparison).grid(row=2, column=0, columnspan=2, pady=10)
        
        self.progress = ttk.Progressbar(config_frame, mode='indeterminate')
        self.progress.grid(row=2, column=2, columnspan=2, sticky=tk.EW, padx=5)
        
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.demo_frame = ttk.Frame(notebook)
        notebook.add(self.demo_frame, text="📊 Demostración Visual")
        self.setup_demo_tab()
        
        self.results_frame = ttk.Frame(notebook)
        notebook.add(self.results_frame, text="📈 Resultados Comparativo")
        self.setup_results_tab()
        
        self.manual_frame = ttk.Frame(notebook)
        notebook.add(self.manual_frame, text="🔧 Operaciones Manuales")
        self.setup_manual_tab()
        
        self.info_frame = ttk.Frame(notebook)
        notebook.add(self.info_frame, text="ℹ️ Información")
        self.setup_info_tab()
        
        self.status_label = ttk.Label(self.root, text="Listo", relief=tk.SUNKEN, anchor=tk.W)
        self.status_label.pack(fill=tk.X, side=tk.BOTTOM)
        
    def setup_demo_tab(self):
        control_panel = ttk.Frame(self.demo_frame)
        control_panel.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Label(control_panel, text="Datos de ejemplo (separados por comas):").pack(side=tk.LEFT, padx=5)
        ttk.Entry(control_panel, textvariable=self.manual_data_var, width=40).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_panel, text="Visualizar Árboles", 
                  command=self.visualize_trees).pack(side=tk.LEFT, padx=5)
        
        self.demo_canvas_frame = ttk.Frame(self.demo_frame)
        self.demo_canvas_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
    def setup_results_tab(self):
        stats_frame = ttk.LabelFrame(self.results_frame, text="Estadísticas", padding=10)
        stats_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.stats_text = scrolledtext.ScrolledText(stats_frame, height=10, wrap=tk.WORD)
        self.stats_text.pack(fill=tk.BOTH, expand=True)
        
        self.graphs_frame = ttk.Frame(self.results_frame)
        self.graphs_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
    def setup_manual_tab(self):
        left_frame = ttk.LabelFrame(self.manual_frame, text="ABB (sin balanceo)", padding=10)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.bst_text = scrolledtext.ScrolledText(left_frame, height=15, wrap=tk.WORD)
        self.bst_text.pack(fill=tk.BOTH, expand=True)
        
        right_frame = ttk.LabelFrame(self.manual_frame, text="Red-Black Tree", padding=10)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.rbt_text = scrolledtext.ScrolledText(right_frame, height=15, wrap=tk.WORD)
        self.rbt_text.pack(fill=tk.BOTH, expand=True)
        
        control_frame = ttk.Frame(self.manual_frame)
        control_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Label(control_frame, text="Valor:").pack(side=tk.LEFT, padx=5)
        self.value_entry = ttk.Entry(control_frame, width=10)
        self.value_entry.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(control_frame, text="Insertar", 
                  command=self.manual_insert).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Buscar", 
                  command=self.manual_search).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Eliminar", 
                  command=self.manual_delete).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Limpiar", 
                  command=self.manual_clear).pack(side=tk.LEFT, padx=5)
        
        self.manual_bst = BinarySearchTree()
        self.manual_rbt = RedBlackTree()
        
    def setup_info_tab(self):
        info_text = scrolledtext.ScrolledText(self.info_frame, wrap=tk.WORD, padx=10, pady=10)
        info_text.pack(fill=tk.BOTH, expand=True)
        
        info_content = """
╔══════════════════════════════════════════════════════════════════════╗
║         COMPARATIVO: ABB vs Red-Black Tree                           ║
╚══════════════════════════════════════════════════════════════════════╝

📚 DESCRIPCIÓN:
Este proyecto compara dos estructuras de datos de árbol:

1. ABB (Árbol Binario de Búsqueda):
   - Estructura sin balanceo automático
   - Puede degenerar en lista enlazada en el peor caso
   - Complejidad: O(log n) promedio, O(n) peor caso

2. Red-Black Tree:
   - Árbol auto-balanceado
   - Garantiza operaciones O(log n) en todos los casos
   - Usa rotaciones y recoloreo de nodos

📊 COMPLEJIDAD TEMPORAL:

Operación       ABB (Promedio)    ABB (Peor)    Red-Black
─────────────────────────────────────────────────────────────
Inserción       O(log n)          O(n)          O(log n)
Búsqueda        O(log n)          O(n)          O(log n)
Altura          ~log₂(n)          n             ≤ 2*log₂(n+1)

✅ CASOS DE USO:

ABB:
  ✓ Implementación simple
  ✓ Bueno para datos aleatorios
  ✗ Degenera con datos ordenados

Red-Black Tree:
  ✓ Rendimiento garantizado O(log n)
  ✓ Mantiene balance automático
  ✓ Ideal para sistemas críticos

🔍 PROPIEDADES RED-BLACK:
1. Cada nodo es rojo o negro
2. La raíz es siempre negra
3. Todas las hojas (NIL) son negras
4. Si un nodo es rojo, sus hijos son negros
5. Todos los caminos raíz→hojas tienen igual cantidad de nodos negros

👥 Autores: Andrés Moreno & Valentina Burgos
        """
        
        info_text.insert(1.0, info_content)
        info_text.config(state=tk.DISABLED)
        
    def run_comparison(self):
        try:
            sizes = [int(x.strip()) for x in self.size_var.get().split(',')]
            if not sizes:
                raise ValueError("Debes ingresar al menos un tamaño")
        except ValueError as e:
            messagebox.showerror("Error", f"Tamaños inválidos: {e}")
            return
        
        self.status_label.config(text="Ejecutando comparativo...")
        self.progress.start()
        
        thread = threading.Thread(target=self._run_comparison_thread, args=(sizes,))
        thread.start()
        
    def _run_comparison_thread(self, sizes):
        try:
            data_type = self.data_type_var.get()
            self.results = self.controller.compare_performance(sizes, data_type)
            self.root.after(0, self._update_results_ui)
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Error", str(e)))
        finally:
            self.root.after(0, self._finish_comparison)
            
    def _update_results_ui(self):
        self.stats_text.delete(1.0, tk.END)
        
        stats = "═" * 70 + "\n"
        stats += f"RESULTADOS - Tipo de datos: {self.results['data_type']}\n"
        stats += "═" * 70 + "\n\n"
        
        for i, size in enumerate(self.results['data_sizes']):
            stats += f"Tamaño: {size}\n"
            stats += f"  BST:\n"
            stats += f"    Inserción: {self.results['bst']['insert'][i]:.6f} s\n"
            stats += f"    Búsqueda:  {self.results['bst']['search'][i]:.6f} s\n"
            stats += f"    Altura:    {self.results['bst']['height'][i]}\n"
            stats += f"  RBT:\n"
            stats += f"    Inserción: {self.results['rbt']['insert'][i]:.6f} s\n"
            stats += f"    Búsqueda:  {self.results['rbt']['search'][i]:.6f} s\n"
            stats += f"    Altura:    {self.results['rbt']['height'][i]}\n\n"
        
        self.stats_text.insert(1.0, stats)
        self.plot_comparison_graphs()
        
    def _finish_comparison(self):
        self.progress.stop()
        self.status_label.config(text="Comparativo completado")
        
    def plot_comparison_graphs(self):
        for widget in self.graphs_frame.winfo_children():
            widget.destroy()
        
        fig = Figure(figsize=(12, 8))
        data_sizes = self.results['data_sizes']
        
        ax1 = fig.add_subplot(2, 2, 1)
        ax1.plot(data_sizes, self.results['bst']['insert'], 'r-o', label='BST', linewidth=2)
        ax1.plot(data_sizes, self.results['rbt']['insert'], 'b-s', label='RBT', linewidth=2)
        ax1.set_xlabel('Cantidad de elementos')
        ax1.set_ylabel('Tiempo (s)')
        ax1.set_title('Tiempo de Inserción')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        ax2 = fig.add_subplot(2, 2, 2)
        ax2.plot(data_sizes, self.results['bst']['search'], 'r-o', label='BST', linewidth=2)
        ax2.plot(data_sizes, self.results['rbt']['search'], 'b-s', label='RBT', linewidth=2)
        ax2.set_xlabel('Cantidad de elementos')
        ax2.set_ylabel('Tiempo (s)')
        ax2.set_title('Tiempo de Búsqueda')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        ax3 = fig.add_subplot(2, 2, 3)
        optimal_heights = [np.log2(n + 1) for n in data_sizes]
        ax3.plot(data_sizes, self.results['bst']['height'], 'r-o', label='BST', linewidth=2)
        ax3.plot(data_sizes, self.results['rbt']['height'], 'b-s', label='RBT', linewidth=2)
        ax3.plot(data_sizes, optimal_heights, 'g--', label='Óptimo (log₂n)', linewidth=2, alpha=0.7)
        ax3.set_xlabel('Cantidad de elementos')
        ax3.set_ylabel('Altura')
        ax3.set_title('Altura del Árbol')
        ax3.legend()
        ax3.grid(True, alpha=0.3)
        
        ax4 = fig.add_subplot(2, 2, 4)
        improvements = []
        for i in range(len(data_sizes)):
            if self.results['bst']['insert'][i] > 0:
                imp = ((self.results['bst']['insert'][i] - self.results['rbt']['insert'][i]) 
                      / self.results['bst']['insert'][i] * 100)
                improvements.append(imp)
            else:
                improvements.append(0)
        
        ax4.bar(range(len(data_sizes)), improvements, color='green', alpha=0.7)
        ax4.set_xlabel('Índice de tamaño')
        ax4.set_ylabel('Mejora (%)')
        ax4.set_title('Mejora de RBT sobre BST (Inserción)')
        ax4.set_xticks(range(len(data_sizes)))
        ax4.set_xticklabels([str(s) for s in data_sizes])
        ax4.grid(True, alpha=0.3, axis='y')
        
        fig.tight_layout()
        
        canvas = FigureCanvasTkAgg(fig, master=self.graphs_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
    def visualize_trees(self):
        try:
            data = [int(x.strip()) for x in self.manual_data_var.get().split(',')]
            if not data:
                raise ValueError("Debes ingresar al menos un valor")
        except ValueError as e:
            messagebox.showerror("Error", f"Datos inválidos: {e}")
            return
        
        bst = BinarySearchTree()
        rbt = RedBlackTree()
        
        for value in data:
            bst.insert(value)
            rbt.insert(value)
        
        for widget in self.demo_canvas_frame.winfo_children():
            widget.destroy()
        
        fig = Figure(figsize=(12, 6))
        
        ax1 = fig.add_subplot(1, 2, 1)
        ax1.axis('off')
        info_bst = f"""ABB (Árbol Binario de Búsqueda)

Datos insertados: {data}

Recorrido Inorden:
{bst.inorder_traversal()}

Recorrido Preorden:
{bst.preorder_traversal()}

Altura: {bst.height()}"""
        ax1.text(0.1, 0.5, info_bst, fontsize=11, family='monospace', verticalalignment='center')
        ax1.set_title('BST (sin balanceo)', fontsize=14, fontweight='bold')
        
        ax2 = fig.add_subplot(1, 2, 2)
        ax2.axis('off')
        info_rbt = f"""Red-Black Tree

Datos insertados: {data}

Recorrido Inorden:
{rbt.inorder_traversal()}

Recorrido Preorden:
{rbt.preorder_traversal()}

Altura: {rbt.height()}"""
        ax2.text(0.1, 0.5, info_rbt, fontsize=11, family='monospace', verticalalignment='center')
        ax2.set_title('Red-Black Tree (balanceado)', fontsize=14, fontweight='bold')
        
        fig.tight_layout()
        
        canvas = FigureCanvasTkAgg(fig, master=self.demo_canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        self.status_label.config(text=f"Árboles visualizados con {len(data)} elementos")
        
    def manual_insert(self):
        try:
            value = int(self.value_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Debes ingresar un número válido")
            return
        
        self.manual_bst.insert(value)
        self.manual_rbt.insert(value)
        
        self.update_manual_trees()
        self.value_entry.delete(0, tk.END)
        self.status_label.config(text=f"Valor {value} insertado en ambos árboles")
        
    def manual_search(self):
        try:
            value = int(self.value_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Debes ingresar un número válido")
            return
        
        bst_found = self.manual_bst.search(value)
        rbt_found = self.manual_rbt.search(value)
        
        result = f"Búsqueda de {value}:\n"
        result += f"  BST: {'✓ Encontrado' if bst_found else '✗ No encontrado'}\n"
        result += f"  RBT: {'✓ Encontrado' if rbt_found else '✗ No encontrado'}"
        
        messagebox.showinfo("Resultado de Búsqueda", result)
        
    def manual_delete(self):
        try:
            value = int(self.value_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Debes ingresar un número válido")
            return
        
        bst_deleted = self.manual_bst.delete(value)
        rbt_deleted = self.manual_rbt.delete(value)
        
        # Update display regardless of result
        self.update_manual_trees()
        self.value_entry.delete(0, tk.END)
        
        if bst_deleted and rbt_deleted:
            # Both trees had the value and deleted it
            result = f"✓ Valor {value} eliminado correctamente de ambos árboles"
            messagebox.showinfo("Eliminación Exitosa", result)
            self.status_label.config(text=f"Valor {value} eliminado de ambos árboles")
        elif not bst_deleted and not rbt_deleted:
            # Value not found in either tree
            messagebox.showwarning("Advertencia", f"El valor {value} no se encuentra en ninguno de los árboles")
            self.status_label.config(text=f"Valor {value} no encontrado")
        else:
            # Inconsistent state - should not happen in normal usage
            result = f"Eliminación de {value}:\n"
            result += f"  BST: {'✓ Eliminado' if bst_deleted else '✗ No encontrado'}\n"
            result += f"  RBT: {'✓ Eliminado' if rbt_deleted else '✗ No encontrado'}\n\n"
            result += "⚠️ Advertencia: Los árboles tienen estados diferentes"
            messagebox.showinfo("Resultado de Eliminación", result)
            self.status_label.config(text=f"Operación completada con inconsistencias")
        
    def manual_clear(self):
        self.manual_bst = BinarySearchTree()
        self.manual_rbt = RedBlackTree()
        self.update_manual_trees()
        self.status_label.config(text="Árboles limpiados")
        
    def update_manual_trees(self):
        self.bst_text.delete(1.0, tk.END)
        bst_info = f"""Inorden:   {self.manual_bst.inorder_traversal()}
Preorden:  {self.manual_bst.preorder_traversal()}
Postorden: {self.manual_bst.postorder_traversal()}
Altura:    {self.manual_bst.height()}"""
        self.bst_text.insert(1.0, bst_info)
        
        self.rbt_text.delete(1.0, tk.END)
        rbt_info = f"""Inorden:   {self.manual_rbt.inorder_traversal()}
Preorden:  {self.manual_rbt.preorder_traversal()}
Postorden: {self.manual_rbt.postorder_traversal()}
Altura:    {self.manual_rbt.height()}"""
        self.rbt_text.insert(1.0, rbt_info)


if __name__ == "__main__":
    root = tk.Tk()
    app = TreeComparisonGUI(root)
    root.mainloop()