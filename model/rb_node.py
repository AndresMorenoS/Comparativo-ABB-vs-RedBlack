"""
Nodo para Árbol Red-Black con balanceo automático
"""


class Color:
    """Colores para nodos Red-Black"""
    RED = 0
    BLACK = 1


class RBNode:
    """Nodo del árbol Red-Black"""
    
    def __init__(self, key, color=Color.RED):
        """
        Inicializa un nodo del árbol Red-Black
        
        Args:
            key: Valor del nodo
            color: Color del nodo (RED por defecto)
        """
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None
