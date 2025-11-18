"""
Vista para generar gráficas de comparación de rendimiento
"""
import matplotlib.pyplot as plt
import numpy as np


class PerformanceView:
    """Vista para visualizar el rendimiento de los árboles"""
    
    def __init__(self):
        """Inicializa la vista"""
        self.figures = []
    
    def plot_insertion_time(self, results, save_path='insertion_comparison.png'):
        """
        Genera gráfica de comparación de tiempos de inserción
        
        Args:
            results: Resultados de las pruebas
            save_path: Ruta donde guardar la gráfica
        """
        data_sizes = results['data_sizes']
        bst_times = results['bst']['insert']
        rbt_times = results['rbt']['insert']
        data_type = results.get('data_type', 'unknown')
        
        plt.figure(figsize=(10, 6))
        plt.plot(data_sizes, bst_times, 'r-o', label='BST (sin balanceo)', linewidth=2, markersize=8)
        plt.plot(data_sizes, rbt_times, 'b-s', label='Red-Black Tree', linewidth=2, markersize=8)
        
        plt.xlabel('Cantidad de elementos', fontsize=12)
        plt.ylabel('Tiempo (segundos)', fontsize=12)
        plt.title(f'Comparación de Tiempos de Inserción - Datos {data_type}', fontsize=14)
        plt.legend(fontsize=11)
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Gráfica guardada en: {save_path}")
        plt.close()
    
    def plot_search_time(self, results, save_path='search_comparison.png'):
        """
        Genera gráfica de comparación de tiempos de búsqueda
        
        Args:
            results: Resultados de las pruebas
            save_path: Ruta donde guardar la gráfica
        """
        data_sizes = results['data_sizes']
        bst_times = results['bst']['search']
        rbt_times = results['rbt']['search']
        data_type = results.get('data_type', 'unknown')
        
        plt.figure(figsize=(10, 6))
        plt.plot(data_sizes, bst_times, 'r-o', label='BST (sin balanceo)', linewidth=2, markersize=8)
        plt.plot(data_sizes, rbt_times, 'b-s', label='Red-Black Tree', linewidth=2, markersize=8)
        
        plt.xlabel('Cantidad de elementos', fontsize=12)
        plt.ylabel('Tiempo (segundos)', fontsize=12)
        plt.title(f'Comparación de Tiempos de Búsqueda - Datos {data_type}', fontsize=14)
        plt.legend(fontsize=11)
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Gráfica guardada en: {save_path}")
        plt.close()
    
    def plot_tree_height(self, results, save_path='height_comparison.png'):
        """
        Genera gráfica de comparación de alturas de árboles
        
        Args:
            results: Resultados de las pruebas
            save_path: Ruta donde guardar la gráfica
        """
        data_sizes = results['data_sizes']
        bst_heights = results['bst']['height']
        rbt_heights = results['rbt']['height']
        data_type = results.get('data_type', 'unknown')
        
        # Calcular altura teórica óptima (log2)
        optimal_heights = [np.log2(n + 1) for n in data_sizes]
        
        plt.figure(figsize=(10, 6))
        plt.plot(data_sizes, bst_heights, 'r-o', label='BST (sin balanceo)', linewidth=2, markersize=8)
        plt.plot(data_sizes, rbt_heights, 'b-s', label='Red-Black Tree', linewidth=2, markersize=8)
        plt.plot(data_sizes, optimal_heights, 'g--', label='Altura óptima (log₂n)', linewidth=2, alpha=0.7)
        
        plt.xlabel('Cantidad de elementos', fontsize=12)
        plt.ylabel('Altura del árbol', fontsize=12)
        plt.title(f'Comparación de Alturas de Árboles - Datos {data_type}', fontsize=14)
        plt.legend(fontsize=11)
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Gráfica guardada en: {save_path}")
        plt.close()
    
    def plot_all_comparisons(self, results, prefix=''):
        """
        Genera todas las gráficas de comparación
        
        Args:
            results: Resultados de las pruebas
            prefix: Prefijo para los nombres de archivos
        """
        data_type = results.get('data_type', 'unknown')
        
        self.plot_insertion_time(results, f'{prefix}insertion_{data_type}.png')
        self.plot_search_time(results, f'{prefix}search_{data_type}.png')
        self.plot_tree_height(results, f'{prefix}height_{data_type}.png')
        
        print(f"\nTodas las gráficas generadas para datos tipo: {data_type}")
    
    def plot_combined_comparison(self, results_list, save_path='combined_comparison.png'):
        """
        Genera una gráfica combinada con múltiples tipos de datos
        
        Args:
            results_list: Lista de resultados de diferentes tipos de datos
            save_path: Ruta donde guardar la gráfica
        """
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        
        # Colores y marcadores para diferentes tipos de datos
        colors = ['red', 'blue', 'green']
        markers = ['o', 's', '^']
        
        for idx, results in enumerate(results_list):
            data_type = results.get('data_type', f'Type {idx}')
            data_sizes = results['data_sizes']
            
            # Tiempo de inserción BST
            axes[0, 0].plot(data_sizes, results['bst']['insert'], 
                          color=colors[idx], marker=markers[idx], 
                          label=f'BST - {data_type}', linewidth=2)
            
            # Tiempo de inserción RBT
            axes[0, 1].plot(data_sizes, results['rbt']['insert'], 
                          color=colors[idx], marker=markers[idx], 
                          label=f'RBT - {data_type}', linewidth=2)
            
            # Altura BST
            axes[1, 0].plot(data_sizes, results['bst']['height'], 
                          color=colors[idx], marker=markers[idx], 
                          label=f'BST - {data_type}', linewidth=2)
            
            # Altura RBT
            axes[1, 1].plot(data_sizes, results['rbt']['height'], 
                          color=colors[idx], marker=markers[idx], 
                          label=f'RBT - {data_type}', linewidth=2)
        
        # Configurar subgráficas
        axes[0, 0].set_title('Tiempo de Inserción - BST', fontsize=12)
        axes[0, 0].set_xlabel('Cantidad de elementos')
        axes[0, 0].set_ylabel('Tiempo (s)')
        axes[0, 0].legend()
        axes[0, 0].grid(True, alpha=0.3)
        
        axes[0, 1].set_title('Tiempo de Inserción - RBT', fontsize=12)
        axes[0, 1].set_xlabel('Cantidad de elementos')
        axes[0, 1].set_ylabel('Tiempo (s)')
        axes[0, 1].legend()
        axes[0, 1].grid(True, alpha=0.3)
        
        axes[1, 0].set_title('Altura del Árbol - BST', fontsize=12)
        axes[1, 0].set_xlabel('Cantidad de elementos')
        axes[1, 0].set_ylabel('Altura')
        axes[1, 0].legend()
        axes[1, 0].grid(True, alpha=0.3)
        
        axes[1, 1].set_title('Altura del Árbol - RBT', fontsize=12)
        axes[1, 1].set_xlabel('Cantidad de elementos')
        axes[1, 1].set_ylabel('Altura')
        axes[1, 1].legend()
        axes[1, 1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Gráfica combinada guardada en: {save_path}")
        plt.close()
    
    def print_statistics(self, results):
        """
        Imprime estadísticas de los resultados
        
        Args:
            results: Resultados de las pruebas
        """
        data_type = results.get('data_type', 'unknown')
        print(f"\n{'='*60}")
        print(f"ESTADÍSTICAS - Datos tipo: {data_type}")
        print(f"{'='*60}")
        
        for i, size in enumerate(results['data_sizes']):
            print(f"\nTamaño de datos: {size}")
            print(f"  BST:")
            print(f"    - Inserción: {results['bst']['insert'][i]:.6f} s")
            print(f"    - Búsqueda:  {results['bst']['search'][i]:.6f} s")
            print(f"    - Altura:    {results['bst']['height'][i]}")
            print(f"  RBT:")
            print(f"    - Inserción: {results['rbt']['insert'][i]:.6f} s")
            print(f"    - Búsqueda:  {results['rbt']['search'][i]:.6f} s")
            print(f"    - Altura:    {results['rbt']['height'][i]}")
            
            # Calcular mejoras
            if results['bst']['insert'][i] > 0:
                insert_improvement = ((results['bst']['insert'][i] - results['rbt']['insert'][i]) 
                                     / results['bst']['insert'][i] * 100)
                print(f"  Mejora RBT en inserción: {insert_improvement:.2f}%")
            
            if results['bst']['search'][i] > 0:
                search_improvement = ((results['bst']['search'][i] - results['rbt']['search'][i]) 
                                     / results['bst']['search'][i] * 100)
                print(f"  Mejora RBT en búsqueda: {search_improvement:.2f}%")
