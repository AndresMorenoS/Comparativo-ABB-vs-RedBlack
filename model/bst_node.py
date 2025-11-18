"""
Nodo para Árbol Binario de Búsqueda sin balanceo
"""


class BSTNode:
    """Nodo del árbol binario de búsqueda"""
    
    def __init__(self, key):
        """
        Inicializa un nodo del ABB
        
        Args:
            key: Valor del nodo
        """
        self.key = key
        self.left = None
        self.right = None
