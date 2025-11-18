"""
Tests para Binary Search Tree (ABB)
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model import BinarySearchTree


def test_bst_insertion():
    """Prueba la inserción en BST"""
    print("Test: Inserción en BST")
    bst = BinarySearchTree()
    values = [5, 3, 7, 1, 4, 6, 8]
    
    for val in values:
        bst.insert(val)
    
    # Verificar recorrido inorden (debe estar ordenado)
    inorder = bst.inorder_traversal()
    expected = sorted(values)
    
    assert inorder == expected, f"Error: {inorder} != {expected}"
    print("  ✓ Inserción correcta")
    print(f"  ✓ Inorden: {inorder}")


def test_bst_search():
    """Prueba la búsqueda en BST"""
    print("\nTest: Búsqueda en BST")
    bst = BinarySearchTree()
    values = [5, 3, 7, 1, 4, 6, 8]
    
    for val in values:
        bst.insert(val)
    
    # Buscar valores existentes
    for val in values:
        assert bst.search(val) == True, f"Error: {val} no encontrado"
    
    # Buscar valores no existentes
    assert bst.search(10) == False, "Error: 10 no debería existir"
    assert bst.search(0) == False, "Error: 0 no debería existir"
    
    print("  ✓ Búsqueda correcta para valores existentes")
    print("  ✓ Búsqueda correcta para valores no existentes")


def test_bst_traversals():
    """Prueba los recorridos del BST"""
    print("\nTest: Recorridos en BST")
    bst = BinarySearchTree()
    values = [5, 3, 7, 1, 4, 6, 8]
    
    for val in values:
        bst.insert(val)
    
    inorder = bst.inorder_traversal()
    preorder = bst.preorder_traversal()
    postorder = bst.postorder_traversal()
    
    print(f"  Inorden:   {inorder}")
    print(f"  Preorden:  {preorder}")
    print(f"  Postorden: {postorder}")
    
    assert inorder == [1, 3, 4, 5, 6, 7, 8], "Error en recorrido inorden"
    assert preorder == [5, 3, 1, 4, 7, 6, 8], "Error en recorrido preorden"
    assert postorder == [1, 4, 3, 6, 8, 7, 5], "Error en recorrido postorden"
    
    print("  ✓ Todos los recorridos correctos")


def test_bst_height():
    """Prueba el cálculo de altura del BST"""
    print("\nTest: Altura del BST")
    
    # Árbol balanceado
    bst1 = BinarySearchTree()
    for val in [5, 3, 7, 1, 4, 6, 8]:
        bst1.insert(val)
    
    height1 = bst1.height()
    print(f"  Altura árbol balanceado: {height1}")
    assert height1 == 3, f"Error: altura {height1} != 3"
    
    # Árbol degenerado (lista)
    bst2 = BinarySearchTree()
    for val in [1, 2, 3, 4, 5]:
        bst2.insert(val)
    
    height2 = bst2.height()
    print(f"  Altura árbol degenerado: {height2}")
    assert height2 == 5, f"Error: altura {height2} != 5"
    
    print("  ✓ Cálculo de altura correcto")


def test_bst_empty():
    """Prueba operaciones en árbol vacío"""
    print("\nTest: Árbol BST vacío")
    bst = BinarySearchTree()
    
    assert bst.search(5) == False, "Error: búsqueda en árbol vacío"
    assert bst.height() == 0, "Error: altura de árbol vacío"
    assert bst.inorder_traversal() == [], "Error: recorrido de árbol vacío"
    
    print("  ✓ Operaciones en árbol vacío correctas")


def run_all_tests():
    """Ejecuta todas las pruebas"""
    print("="*60)
    print("PRUEBAS DEL ÁRBOL BINARIO DE BÚSQUEDA (ABB)")
    print("="*60)
    
    test_bst_insertion()
    test_bst_search()
    test_bst_traversals()
    test_bst_height()
    test_bst_empty()
    
    print("\n" + "="*60)
    print("TODAS LAS PRUEBAS DEL BST PASARON CORRECTAMENTE ✓")
    print("="*60)


if __name__ == "__main__":
    run_all_tests()
