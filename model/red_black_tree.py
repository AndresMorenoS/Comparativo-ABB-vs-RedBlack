"""
Árbol Red-Black con balanceo automático
"""
from model.rb_node import RBNode, Color


class RedBlackTree:
    """Árbol Red-Black con balanceo automático"""
    
    def __init__(self):
        """Inicializa un árbol Red-Black vacío"""
        self.NIL = RBNode(None, Color.BLACK)  # Nodo centinela
        self.root = self.NIL
    
    def insert(self, key):
        """
        Inserta un nuevo nodo en el árbol con balanceo automático
        
        Args:
            key: Valor a insertar
        """
        new_node = RBNode(key, Color.RED)
        new_node.left = self.NIL
        new_node.right = self.NIL
        
        parent = None
        current = self.root
        
        # Buscar la posición para insertar
        while current != self.NIL:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right
        
        new_node.parent = parent
        
        # Insertar el nodo
        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node
        
        # Reparar el árbol para mantener las propiedades Red-Black
        self._fix_insert(new_node)
    
    def _fix_insert(self, node):
        """
        Repara el árbol después de una inserción para mantener propiedades Red-Black
        
        Args:
            node: Nodo recién insertado
        """
        while node.parent and node.parent.color == Color.RED:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                
                if uncle.color == Color.RED:
                    # Caso 1: El tío es rojo
                    node.parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        # Caso 2: El nodo es hijo derecho
                        node = node.parent
                        self._left_rotate(node)
                    
                    # Caso 3: El nodo es hijo izquierdo
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                
                if uncle.color == Color.RED:
                    # Caso 1: El tío es rojo
                    node.parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        # Caso 2: El nodo es hijo izquierdo
                        node = node.parent
                        self._right_rotate(node)
                    
                    # Caso 3: El nodo es hijo derecho
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    self._left_rotate(node.parent.parent)
        
        self.root.color = Color.BLACK
    
    def _left_rotate(self, node):
        """
        Realiza una rotación a la izquierda
        
        Args:
            node: Nodo sobre el cual rotar
        """
        right_child = node.right
        node.right = right_child.left
        
        if right_child.left != self.NIL:
            right_child.left.parent = node
        
        right_child.parent = node.parent
        
        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        
        right_child.left = node
        node.parent = right_child
    
    def _right_rotate(self, node):
        """
        Realiza una rotación a la derecha
        
        Args:
            node: Nodo sobre el cual rotar
        """
        left_child = node.left
        node.left = left_child.right
        
        if left_child.right != self.NIL:
            left_child.right.parent = node
        
        left_child.parent = node.parent
        
        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child
        
        left_child.right = node
        node.parent = left_child
    
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
        if node == self.NIL:
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
        if node != self.NIL:
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
        if node != self.NIL:
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
        if node != self.NIL:
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
        if node == self.NIL:
            return 0
        
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        
        return 1 + max(left_height, right_height)
