"""
Árbol Binario de Búsqueda sin balanceo (ABB)
"""
from model.bst_node import BSTNode


class BinarySearchTree:
    """Árbol Binario de Búsqueda sin balanceo"""
    
    def __init__(self):
        """Inicializa un ABB vacío"""
        self.root = None
    
    def insert(self, key):
        """
        Inserta un nuevo nodo en el árbol (iterativo para evitar stack overflow)
        
        Args:
            key: Valor a insertar
        """
        if self.root is None:
            self.root = BSTNode(key)
            return
        
        current = self.root
        while True:
            if key < current.key:
                if current.left is None:
                    current.left = BSTNode(key)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = BSTNode(key)
                    return
                current = current.right
    
    def search(self, key):
        """
        Busca un valor en el árbol (iterativo para evitar stack overflow)
        
        Args:
            key: Valor a buscar
            
        Returns:
            True si el valor existe, False en caso contrario
        """
        current = self.root
        while current is not None:
            if key == current.key:
                return True
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return False
    
    def inorder_traversal(self):
        """
        Realiza un recorrido inorden del árbol
        
        Returns:
            Lista con los valores en orden
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        """
        Recorrido inorden recursivo
        
        Args:
            node: Nodo actual
            result: Lista para almacenar los resultados
        """
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)
    
    def preorder_traversal(self):
        """
        Realiza un recorrido preorden del árbol
        
        Returns:
            Lista con los valores en preorden
        """
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node, result):
        """
        Recorrido preorden recursivo
        
        Args:
            node: Nodo actual
            result: Lista para almacenar los resultados
        """
        if node is not None:
            result.append(node.key)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def postorder_traversal(self):
        """
        Realiza un recorrido postorden del árbol
        
        Returns:
            Lista con los valores en postorden
        """
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, node, result):
        """
        Recorrido postorden recursivo
        
        Args:
            node: Nodo actual
            result: Lista para almacenar los resultados
        """
        if node is not None:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.key)
    
    def height(self):
        """
        Calcula la altura del árbol (iterativo para evitar stack overflow)
        
        Returns:
            Altura del árbol
        """
        if self.root is None:
            return 0
        
        # Usar BFS con nivel tracking
        from collections import deque
        queue = deque([(self.root, 1)])
        max_height = 0
        
        while queue:
            node, level = queue.popleft()
            max_height = max(max_height, level)
            
            if node.left is not None:
                queue.append((node.left, level + 1))
            if node.right is not None:
                queue.append((node.right, level + 1))
        
        return max_height
    
    def _height_recursive(self, node):
        """
        Calcula recursivamente la altura del árbol (obsoleto, usar height())
        
        Args:
            node: Nodo actual
            
        Returns:
            Altura desde el nodo actual
        """
        if node is None:
            return 0
        
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        
        return 1 + max(left_height, right_height)
