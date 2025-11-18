"""
Ejemplo básico de uso de los árboles BST y Red-Black Tree
"""
from model import BinarySearchTree, RedBlackTree


def demo_basic_operations():
    """Demuestra las operaciones básicas de ambos árboles"""
    
    print("="*70)
    print("DEMOSTRACIÓN DE OPERACIONES BÁSICAS")
    print("="*70)
    
    # Datos de ejemplo
    data = [50, 30, 70, 20, 40, 60, 80]
    
    # === Binary Search Tree ===
    print("\n1. ÁRBOL BINARIO DE BÚSQUEDA (ABB)")
    print("-" * 70)
    
    bst = BinarySearchTree()
    print(f"Insertando datos: {data}")
    for value in data:
        bst.insert(value)
    
    print(f"\nRecorrido Inorden:   {bst.inorder_traversal()}")
    print(f"Recorrido Preorden:  {bst.preorder_traversal()}")
    print(f"Recorrido Postorden: {bst.postorder_traversal()}")
    print(f"Altura del árbol:    {bst.height()}")
    
    # Búsquedas
    print("\nBúsquedas:")
    for value in [40, 90]:
        result = "encontrado" if bst.search(value) else "no encontrado"
        print(f"  {value}: {result}")
    
    # === Red-Black Tree ===
    print("\n2. RED-BLACK TREE")
    print("-" * 70)
    
    rbt = RedBlackTree()
    print(f"Insertando datos: {data}")
    for value in data:
        rbt.insert(value)
    
    print(f"\nRecorrido Inorden:   {rbt.inorder_traversal()}")
    print(f"Recorrido Preorden:  {rbt.preorder_traversal()}")
    print(f"Recorrido Postorden: {rbt.postorder_traversal()}")
    print(f"Altura del árbol:    {rbt.height()}")
    
    # Búsquedas
    print("\nBúsquedas:")
    for value in [40, 90]:
        result = "encontrado" if rbt.search(value) else "no encontrado"
        print(f"  {value}: {result}")


def demo_worst_case():
    """Demuestra el peor caso para BST vs Red-Black Tree"""
    
    print("\n\n" + "="*70)
    print("DEMOSTRACIÓN: PEOR CASO - DATOS ORDENADOS")
    print("="*70)
    
    ordered_data = list(range(1, 101))
    
    # BST con datos ordenados
    print("\n1. ABB con datos ordenados (1-100)")
    print("-" * 70)
    bst = BinarySearchTree()
    for value in ordered_data:
        bst.insert(value)
    
    print(f"Altura del árbol: {bst.height()}")
    print(f"Altura esperada (degenerado): {len(ordered_data)}")
    print("⚠️  El árbol degeneró en una lista enlazada!")
    
    # Red-Black Tree con datos ordenados
    print("\n2. Red-Black Tree con datos ordenados (1-100)")
    print("-" * 70)
    rbt = RedBlackTree()
    for value in ordered_data:
        rbt.insert(value)
    
    import math
    optimal_height = math.log2(len(ordered_data) + 1)
    max_height = 2 * optimal_height
    
    print(f"Altura del árbol: {rbt.height()}")
    print(f"Altura óptima (log₂n): {optimal_height:.2f}")
    print(f"Altura máxima permitida: {max_height:.2f}")
    print("✓ El árbol mantiene el balance!")
    
    # Comparación
    print("\n3. COMPARACIÓN")
    print("-" * 70)
    print(f"Mejora en altura: {bst.height() / rbt.height():.2f}x")
    print(f"ABB altura:  {bst.height()} (O(n) - lista)")
    print(f"RBT altura:  {rbt.height()} (O(log n) - balanceado)")


if __name__ == "__main__":
    demo_basic_operations()
    demo_worst_case()
    
    print("\n" + "="*70)
    print("DEMOSTRACIÓN COMPLETADA")
    print("="*70)
    print("\nPara ver el análisis completo de rendimiento, ejecuta:")
    print("  python main.py")
    print()
