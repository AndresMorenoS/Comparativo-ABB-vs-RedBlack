"""
Controlador para la comparación de rendimiento entre ABB y Red-Black Tree
"""
import time
import random
from model import BinarySearchTree, RedBlackTree


class PerformanceController:
    """Controlador para medir y comparar el rendimiento de los árboles"""
    
    def __init__(self):
        """Inicializa el controlador"""
        self.bst_times = {
            'insert': [],
            'search': [],
            'height': []
        }
        self.rbt_times = {
            'insert': [],
            'search': [],
            'height': []
        }
        self.data_sizes = []
    
    def generate_ordered_data(self, size):
        """
        Genera datos ordenados ascendentemente
        
        Args:
            size: Cantidad de elementos
            
        Returns:
            Lista de datos ordenados
        """
        return list(range(1, size + 1))
    
    def generate_random_data(self, size):
        """
        Genera datos aleatorios
        
        Args:
            size: Cantidad de elementos
            
        Returns:
            Lista de datos aleatorios
        """
        data = list(range(1, size + 1))
        random.shuffle(data)
        return data
    
    def generate_reverse_data(self, size):
        """
        Genera datos ordenados descendentemente (desordenados)
        
        Args:
            size: Cantidad de elementos
            
        Returns:
            Lista de datos en orden inverso
        """
        return list(range(size, 0, -1))
    
    def measure_insertion_time(self, tree, data):
        """
        Mide el tiempo de inserción de datos en un árbol
        
        Args:
            tree: Árbol (BST o RBT)
            data: Lista de datos a insertar
            
        Returns:
            Tiempo transcurrido en segundos
        """
        start_time = time.time()
        for value in data:
            tree.insert(value)
        end_time = time.time()
        return end_time - start_time
    
    def measure_search_time(self, tree, data):
        """
        Mide el tiempo de búsqueda de datos en un árbol
        
        Args:
            tree: Árbol (BST o RBT)
            data: Lista de datos a buscar
            
        Returns:
            Tiempo transcurrido en segundos
        """
        start_time = time.time()
        for value in data:
            tree.search(value)
        end_time = time.time()
        return end_time - start_time
    
    def compare_performance(self, data_sizes, data_type='random'):
        """
        Compara el rendimiento de BST y RBT con diferentes tamaños de datos
        
        Args:
            data_sizes: Lista de tamaños de datos a probar
            data_type: Tipo de datos ('random', 'ordered', 'reverse')
            
        Returns:
            Diccionario con los resultados de las pruebas
        """
        self.data_sizes = data_sizes
        self.bst_times = {
            'insert': [],
            'search': [],
            'height': []
        }
        self.rbt_times = {
            'insert': [],
            'search': [],
            'height': []
        }
        
        for size in data_sizes:
            # Generar datos según el tipo
            if data_type == 'random':
                data = self.generate_random_data(size)
            elif data_type == 'ordered':
                data = self.generate_ordered_data(size)
            else:  # reverse
                data = self.generate_reverse_data(size)
            
            # Pruebas con BST
            bst = BinarySearchTree()
            bst_insert_time = self.measure_insertion_time(bst, data)
            bst_search_time = self.measure_search_time(bst, data)
            bst_height = bst.height()
            
            self.bst_times['insert'].append(bst_insert_time)
            self.bst_times['search'].append(bst_search_time)
            self.bst_times['height'].append(bst_height)
            
            # Pruebas con RBT
            rbt = RedBlackTree()
            rbt_insert_time = self.measure_insertion_time(rbt, data)
            rbt_search_time = self.measure_search_time(rbt, data)
            rbt_height = rbt.height()
            
            self.rbt_times['insert'].append(rbt_insert_time)
            self.rbt_times['search'].append(rbt_search_time)
            self.rbt_times['height'].append(rbt_height)
            
            print(f"Tamaño {size}: BST altura={bst_height}, RBT altura={rbt_height}")
        
        return {
            'data_sizes': self.data_sizes,
            'bst': self.bst_times,
            'rbt': self.rbt_times,
            'data_type': data_type
        }
    
    def get_results(self):
        """
        Obtiene los resultados de las pruebas
        
        Returns:
            Diccionario con los resultados
        """
        return {
            'data_sizes': self.data_sizes,
            'bst': self.bst_times,
            'rbt': self.rbt_times
        }
