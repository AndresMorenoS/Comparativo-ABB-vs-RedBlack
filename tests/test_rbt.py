"""
Tests para Red-Black Tree
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model import RedBlackTree, Color


def test_rbt_insertion():
    """Prueba la inserción en Red-Black Tree"""
    print("Test: Inserción en Red-Black Tree")
    rbt = RedBlackTree()
    values = [7, 3, 18, 10, 22, 8, 11, 26]
    
    for val in values:
        rbt.insert(val)
    
    # Verificar recorrido inorden (debe estar ordenado)
    inorder = rbt.inorder_traversal()
    expected = sorted(values)
    
    assert inorder == expected, f"Error: {inorder} != {expected}"
    print("  ✓ Inserción correcta")
    print(f"  ✓ Inorden: {inorder}")


def test_rbt_search():
    """Prueba la búsqueda en Red-Black Tree"""
    print("\nTest: Búsqueda en Red-Black Tree")
    rbt = RedBlackTree()
    values = [7, 3, 18, 10, 22, 8, 11, 26]
    
    for val in values:
        rbt.insert(val)
    
    # Buscar valores existentes
    for val in values:
        assert rbt.search(val) == True, f"Error: {val} no encontrado"
    
    # Buscar valores no existentes
    assert rbt.search(100) == False, "Error: 100 no debería existir"
    assert rbt.search(0) == False, "Error: 0 no debería existir"
    
    print("  ✓ Búsqueda correcta para valores existentes")
    print("  ✓ Búsqueda correcta para valores no existentes")


def test_rbt_traversals():
    """Prueba los recorridos del Red-Black Tree"""
    print("\nTest: Recorridos en Red-Black Tree")
    rbt = RedBlackTree()
    values = [7, 3, 18, 10, 22, 8, 11, 26]
    
    for val in values:
        rbt.insert(val)
    
    inorder = rbt.inorder_traversal()
    preorder = rbt.preorder_traversal()
    postorder = rbt.postorder_traversal()
    
    print(f"  Inorden:   {inorder}")
    print(f"  Preorden:  {preorder}")
    print(f"  Postorden: {postorder}")
    
    # Inorden debe estar ordenado
    assert inorder == sorted(values), "Error en recorrido inorden"
    
    # Verificar que todos los valores están presentes
    assert len(preorder) == len(values), "Error: faltan valores en preorden"
    assert len(postorder) == len(values), "Error: faltan valores en postorden"
    
    print("  ✓ Todos los recorridos correctos")


def test_rbt_height():
    """Prueba el cálculo de altura del Red-Black Tree"""
    print("\nTest: Altura del Red-Black Tree")
    
    # Árbol con varios elementos
    rbt = RedBlackTree()
    for val in [7, 3, 18, 10, 22, 8, 11, 26, 2, 6, 13]:
        rbt.insert(val)
    
    height = rbt.height()
    n = 11  # número de elementos
    
    # La altura de un RBT debe ser <= 2*log2(n+1)
    import math
    max_height = 2 * math.log2(n + 1)
    
    print(f"  Altura del árbol: {height}")
    print(f"  Altura máxima teórica: {max_height:.2f}")
    
    assert height <= max_height, f"Error: altura {height} > {max_height}"
    
    print("  ✓ Altura dentro del límite teórico")


def test_rbt_ordered_insertion():
    """Prueba inserción ordenada (peor caso para BST)"""
    print("\nTest: Inserción ordenada en Red-Black Tree")
    
    rbt = RedBlackTree()
    n = 100
    
    # Insertar datos ordenados
    for i in range(1, n + 1):
        rbt.insert(i)
    
    height = rbt.height()
    
    # Verificar que no degenera en lista
    import math
    max_height = 2 * math.log2(n + 1)
    
    print(f"  Elementos insertados: {n}")
    print(f"  Altura del árbol: {height}")
    print(f"  Altura máxima teórica: {max_height:.2f}")
    
    assert height <= max_height, f"Error: altura {height} > {max_height}"
    assert height < n, "Error: el árbol degeneró en lista"
    
    # Verificar que el recorrido inorden está ordenado
    inorder = rbt.inorder_traversal()
    assert inorder == list(range(1, n + 1)), "Error: recorrido inorden incorrecto"
    
    print("  ✓ El árbol mantiene balance con datos ordenados")


def test_rbt_balance():
    """Prueba que el árbol mantiene el balance"""
    print("\nTest: Balance del Red-Black Tree")
    
    rbt = RedBlackTree()
    values = [50, 25, 75, 10, 30, 60, 80, 5, 15, 27, 55]
    
    for val in values:
        rbt.insert(val)
    
    height = rbt.height()
    n = len(values)
    
    import math
    optimal_height = math.log2(n + 1)
    max_height = 2 * math.log2(n + 1)
    
    print(f"  Elementos: {n}")
    print(f"  Altura óptima: {optimal_height:.2f}")
    print(f"  Altura actual: {height}")
    print(f"  Altura máxima permitida: {max_height:.2f}")
    
    assert height <= max_height, "Error: violación de altura máxima"
    
    print("  ✓ El árbol mantiene el balance correcto")


def test_rbt_empty():
    """Prueba operaciones en árbol vacío"""
    print("\nTest: Árbol Red-Black vacío")
    rbt = RedBlackTree()
    
    assert rbt.search(5) == False, "Error: búsqueda en árbol vacío"
    assert rbt.height() == 0, "Error: altura de árbol vacío"
    assert rbt.inorder_traversal() == [], "Error: recorrido de árbol vacío"
    
    print("  ✓ Operaciones en árbol vacío correctas")


def run_all_tests():
    """Ejecuta todas las pruebas"""
    print("="*60)
    print("PRUEBAS DEL ÁRBOL RED-BLACK")
    print("="*60)
    
    test_rbt_insertion()
    test_rbt_search()
    test_rbt_traversals()
    test_rbt_height()
    test_rbt_ordered_insertion()
    test_rbt_balance()
    test_rbt_empty()
    
    print("\n" + "="*60)
    print("TODAS LAS PRUEBAS DEL RED-BLACK TREE PASARON CORRECTAMENTE ✓")
    print("="*60)


if __name__ == "__main__":
    run_all_tests()
