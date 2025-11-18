"""
Aplicación principal para comparar ABB vs Red-Black Tree
Arquitectura MVC (Model-View-Controller)
"""
from controller import PerformanceController
from view import PerformanceView


def main():
    """Función principal de la aplicación"""
    
    print("="*70)
    print("COMPARATIVO: Árbol Binario de Búsqueda vs Red-Black Tree")
    print("="*70)
    print("\nEste programa compara el rendimiento de:")
    print("  1. ABB (Árbol Binario de Búsqueda sin balanceo)")
    print("  2. Red-Black Tree (con balanceo automático)")
    print("\nSe analizarán tres tipos de datos:")
    print("  - Datos ordenados (peor caso para ABB)")
    print("  - Datos aleatorios (caso promedio)")
    print("  - Datos en orden inverso (peor caso para ABB)")
    print("="*70)
    
    # Inicializar controlador y vista
    controller = PerformanceController()
    view = PerformanceView()
    
    # Definir tamaños de prueba
    data_sizes = [100, 500, 1000, 2000, 3000]
    
    print(f"\nTamaños de prueba: {data_sizes}")
    print("\nIniciando pruebas de rendimiento...\n")
    
    # Lista para almacenar todos los resultados
    all_results = []
    
    # 1. Pruebas con datos aleatorios
    print("\n" + "="*70)
    print("1. PRUEBAS CON DATOS ALEATORIOS")
    print("="*70)
    results_random = controller.compare_performance(data_sizes, 'random')
    view.print_statistics(results_random)
    view.plot_all_comparisons(results_random, prefix='')
    all_results.append(results_random)
    
    # 2. Pruebas con datos ordenados
    print("\n" + "="*70)
    print("2. PRUEBAS CON DATOS ORDENADOS (Peor caso para ABB)")
    print("="*70)
    results_ordered = controller.compare_performance(data_sizes, 'ordered')
    view.print_statistics(results_ordered)
    view.plot_all_comparisons(results_ordered, prefix='')
    all_results.append(results_ordered)
    
    # 3. Pruebas con datos en orden inverso
    print("\n" + "="*70)
    print("3. PRUEBAS CON DATOS EN ORDEN INVERSO (Peor caso para ABB)")
    print("="*70)
    results_reverse = controller.compare_performance(data_sizes, 'reverse')
    view.print_statistics(results_reverse)
    view.plot_all_comparisons(results_reverse, prefix='')
    all_results.append(results_reverse)
    
    # Generar gráfica combinada
    print("\n" + "="*70)
    print("GENERANDO GRÁFICA COMPARATIVA COMPLETA")
    print("="*70)
    view.plot_combined_comparison(all_results, 'combined_comparison.png')
    
    # Resumen final
    print("\n" + "="*70)
    print("RESUMEN DE CONCLUSIONES")
    print("="*70)
    print("\n1. COMPLEJIDAD TEMPORAL:")
    print("   - ABB sin balanceo:")
    print("     * Mejor caso (aleatorio): O(log n)")
    print("     * Peor caso (ordenado): O(n)")
    print("   - Red-Black Tree:")
    print("     * Todos los casos: O(log n) garantizado")
    
    print("\n2. ALTURA DEL ÁRBOL:")
    print("   - ABB: Puede degenerar en una lista (altura = n)")
    print("   - Red-Black: Altura máxima garantizada <= 2*log₂(n+1)")
    
    print("\n3. BALANCEO:")
    print("   - ABB: Sin balanceo automático")
    print("   - Red-Black: Balanceo automático mediante rotaciones y recoloreo")
    
    print("\n4. APLICACIONES:")
    print("   - ABB: Útil cuando los datos son aleatorios y se necesita simplicidad")
    print("   - Red-Black: Ideal para sistemas que requieren rendimiento predecible")
    
    print("\n" + "="*70)
    print("PRUEBAS COMPLETADAS")
    print("="*70)
    print("\nGráficas generadas:")
    print("  - insertion_random.png, insertion_ordered.png, insertion_reverse.png")
    print("  - search_random.png, search_ordered.png, search_reverse.png")
    print("  - height_random.png, height_ordered.png, height_reverse.png")
    print("  - combined_comparison.png (comparativa completa)")
    print("\n")


if __name__ == "__main__":
    main()
