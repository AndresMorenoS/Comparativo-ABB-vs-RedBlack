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
        Inserta un nuevo nodo en el árbol
        
        Args:
            key: Valor a insertar
        """
        if self.root is None:
            self.root = BSTNode(key)
        else:
            self._insert_recursive(self.root, key)
    
    def _insert_recursive(self, node, key):
        """
        Inserta recursivamente un nodo en el árbol
        
        Args:
            node: Nodo actual
            key: Valor a insertar
        """
        if key < node.key:
            if node.left is None:
                node.left = BSTNode(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = BSTNode(key)
            else:
                self._insert_recursive(node.right, key)
    
    def search(self, key):
        """
        Busca un valor en el árbol
        
        Args:
            key: Valor a buscar
            
        Returns:
            True si el valor existe, False en caso contrario
        """
        return self._search_recursive(self.root, key)
    
    def _search_recursive(self, node, key):
        """
        Busca recursivamente un valor en el árbol
        
        Args:
            node: Nodo actual
            key: Valor a buscar
            
        Returns:
            True si el valor existe, False en caso contrario
        """
        if node is None:
            return False
        
        if key == node.key:
            return True
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)
    
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
        Calcula la altura del árbol
        
        Returns:
            Altura del árbol
        """
        return self._height_recursive(self.root)
    
    def _height_recursive(self, node):
        """
        Calcula recursivamente la altura del árbol
        
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
