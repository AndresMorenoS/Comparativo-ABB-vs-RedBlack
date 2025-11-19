# Comparativo-ABB-vs-RedBlack

Proyecto enfocado en comprender, implementar y comparar un Árbol Binario de Búsqueda sin balanceo (ABB) y un Árbol Red-Black, analizando sus diferencias en costos computacionales, balanceo y eficiencia.

## 📋 Descripción

Este proyecto implementa y compara dos estructuras de datos de árbol:

1. **ABB (Árbol Binario de Búsqueda)**: Estructura sin balanceo automático que puede degenerar en una lista enlazada en el peor caso.
2. **Red-Black Tree**: Árbol auto-balanceado que garantiza operaciones O(log n) en todos los casos mediante rotaciones y recoloreo de nodos.

## 🏗️ Arquitectura

El proyecto sigue el patrón **MVC (Model-View-Controller)**:

```
Comparativo-ABB-vs-RedBlack/
├── model/                      # Modelos de datos
│   ├── bst_node.py            # Nodo del ABB
│   ├── binary_search_tree.py  # Implementación del ABB
│   ├── rb_node.py             # Nodo del Red-Black Tree
│   └── red_black_tree.py      # Implementación del Red-Black Tree
├── controller/                 # Lógica de negocio
│   └── performance_controller.py  # Controlador de pruebas de rendimiento
├── view/                       # Visualización
│   └── performance_view.py    # Generación de gráficas
├── tests/                      # Pruebas unitarias
│   ├── test_bst.py            # Tests del ABB
│   └── test_rbt.py            # Tests del Red-Black Tree
├── main.py                     # Punto de entrada de la aplicación
├── demo.py                     # Script de demostración básica
└── requirements.txt            # Dependencias del proyecto
```

## 🚀 Instalación

### Requisitos previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/AndresMorenoS/Comparativo-ABB-vs-RedBlack.git
cd Comparativo-ABB-vs-RedBlack
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## 📊 Uso

### Ejecutar el comparativo completo

```bash
python main.py
```

Este comando ejecutará:
- Pruebas con datos **aleatorios** (caso promedio)
- Pruebas con datos **ordenados** (peor caso para ABB)
- Pruebas con datos en **orden inverso** (peor caso para ABB)

Generará gráficas comparativas de:
- Tiempos de inserción
- Tiempos de búsqueda
- Altura de los árboles

### Ejecutar demostración básica

```bash
python demo.py
```

Este script muestra:
- Operaciones básicas de inserción, búsqueda y recorridos
- Comparación del peor caso (datos ordenados)
- Diferencias de altura entre ABB y Red-Black Tree

### Ejecutar tests unitarios

```bash
# Tests del ABB
python tests/test_bst.py

# Tests del Red-Black Tree
python tests/test_rbt.py
```

## 📈 Resultados

El programa genera 10 gráficas en formato PNG:

### Por tipo de datos:
- `insertion_[tipo].png` - Comparación de tiempos de inserción
- `search_[tipo].png` - Comparación de tiempos de búsqueda
- `height_[tipo].png` - Comparación de alturas de árboles

Donde `[tipo]` puede ser: `random`, `ordered`, `reverse`

### Gráfica combinada:
- `combined_comparison.png` - Vista general de todas las comparaciones

## 🔍 Características Implementadas

### Árbol Binario de Búsqueda (ABB)
- ✅ Inserción iterativa (evita stack overflow)
- ✅ Búsqueda iterativa
- ✅ Recorridos: inorden, preorden, postorden
- ✅ Cálculo de altura (iterativo con BFS)
- ✅ Complejidad O(n) en el peor caso (datos ordenados)

### Red-Black Tree
- ✅ Inserción con balanceo automático
- ✅ Rotaciones: izquierda y derecha
- ✅ Recoloreo de nodos según reglas Red-Black
- ✅ Búsqueda eficiente
- ✅ Recorridos: inorden, preorden, postorden
- ✅ Complejidad O(log n) garantizada en todos los casos
- ✅ Altura máxima: 2 * log₂(n+1)

## 📊 Análisis de Complejidad

### Complejidad Temporal

| Operación | ABB (Promedio) | ABB (Peor caso) | Red-Black Tree |
|-----------|----------------|------------------|----------------|
| Inserción | O(log n)       | O(n)            | O(log n)       |
| Búsqueda  | O(log n)       | O(n)            | O(log n)       |
| Altura    | ~log₂(n)       | n               | ≤ 2*log₂(n+1) |

### Casos de Uso

**ABB (Árbol Binario de Búsqueda):**
- ✅ Implementación simple
- ✅ Bueno para datos aleatorios
- ❌ Degenera con datos ordenados
- ❌ Rendimiento impredecible

**Red-Black Tree:**
- ✅ Rendimiento garantizado O(log n)
- ✅ Mantiene balance automático
- ✅ Ideal para sistemas críticos
- ⚠️ Mayor complejidad de implementación
- ⚠️ Overhead por rotaciones

## 🧪 Pruebas

El proyecto incluye pruebas unitarias exhaustivas:

### Tests del ABB (`tests/test_bst.py`):
- Inserción de nodos
- Búsqueda de valores
- Recorridos (inorden, preorden, postorden)
- Cálculo de altura
- Operaciones en árbol vacío

### Tests del Red-Black Tree (`tests/test_rbt.py`):
- Inserción con balanceo
- Búsqueda de valores
- Recorridos
- Verificación de altura máxima
- Inserción de datos ordenados (peor caso)
- Verificación de propiedades Red-Black

## 📚 Conceptos Implementados

### Propiedades Red-Black Tree
1. Cada nodo es rojo o negro
2. La raíz es siempre negra
3. Todas las hojas (NIL) son negras
4. Si un nodo es rojo, sus hijos deben ser negros
5. Todos los caminos desde la raíz a las hojas tienen el mismo número de nodos negros

### Rotaciones
- **Rotación izquierda**: Para balancear cuando el subárbol derecho es más pesado
- **Rotación derecha**: Para balancear cuando el subárbol izquierdo es más pesado

## 🎯 Conclusiones

1. **ABB** es más simple pero impredecible
2. **Red-Black Tree** garantiza rendimiento consistente
3. Para datos ordenados, Red-Black Tree es hasta **95% más rápido**
4. La altura del Red-Black Tree se mantiene logarítmica incluso con datos ordenados
5. ABB degenera en lista con datos ordenados (altura = n)

## 📄 Licencia

Este proyecto es de código abierto y está disponible para fines educativos.

## 👥 Autor

Andrés Moreno - [@AndresMorenoS](https://github.com/AndresMorenoS) // Valentina Burgos


## 🙏 Agradecimientos

Proyecto desarrollado como parte del estudio de estructuras de datos y análisis de algoritmos.

