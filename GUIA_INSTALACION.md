# Guía de Instalación y Configuración

## 📋 Índice
1. [Requisitos del Sistema](#requisitos-del-sistema)
2. [Compatibilidad de Python](#compatibilidad-de-python)
3. [Instalación con Entorno Virtual (Recomendado)](#instalación-con-entorno-virtual-recomendado)
4. [Instalación Sin Entorno Virtual](#instalación-sin-entorno-virtual)
5. [Verificación de la Instalación](#verificación-de-la-instalación)
6. [Solución de Problemas](#solución-de-problemas)
7. [Dependencias Detalladas](#dependencias-detalladas)

---

## 1. Requisitos del Sistema

### Mínimos
- **Python**: 3.8 o superior
- **pip**: 20.0 o superior
- **Sistema Operativo**: Windows, macOS, Linux
- **Memoria RAM**: 256 MB (recomendado 512 MB para conjuntos grandes de datos)
- **Espacio en disco**: 100 MB

### Recomendados
- **Python**: 3.10 o superior
- **pip**: última versión
- **Memoria RAM**: 1 GB o más
- **Espacio en disco**: 500 MB (incluye entorno virtual)

---

## 2. Compatibilidad de Python

Este proyecto es compatible con las siguientes versiones de Python:

| Versión de Python | Estado | Notas |
|-------------------|--------|-------|
| **3.8** | ✅ Soportado | Versión mínima requerida |
| **3.9** | ✅ Soportado | Totalmente compatible |
| **3.10** | ✅ Soportado | Totalmente compatible |
| **3.11** | ✅ Soportado | Totalmente compatible |
| **3.12** | ✅ Soportado | Totalmente compatible (probado) |
| **3.13+** | ⚠️ Experimental | Debería funcionar, no probado oficialmente |
| **3.7 o anterior** | ❌ No soportado | No compatible |

### Verificar tu versión de Python

```bash
python --version
# o
python3 --version
```

**Salida esperada**: `Python 3.8.x` o superior

---

## 3. Instalación con Entorno Virtual (Recomendado)

### ¿Por qué usar un entorno virtual?

Un **entorno virtual (venv)** es una práctica recomendada que:

✅ **Aísla las dependencias** del proyecto del sistema
✅ **Evita conflictos** con otros proyectos Python
✅ **Garantiza versiones específicas** de paquetes
✅ **Facilita la reproducibilidad** en diferentes máquinas
✅ **Protege el sistema** de modificaciones no deseadas
✅ **Permite múltiples versiones** de la misma librería en diferentes proyectos

### 3.1 Instalación en Linux/macOS

#### Paso 1: Clonar el repositorio

```bash
git clone https://github.com/AndresMorenoS/Comparativo-ABB-vs-RedBlack.git
cd Comparativo-ABB-vs-RedBlack
```

#### Paso 2: Crear el entorno virtual

```bash
# Crear entorno virtual llamado 'venv'
python3 -m venv venv

# O especificar una versión particular de Python
python3.10 -m venv venv
```

**Explicación**:
- `python3 -m venv`: Ejecuta el módulo venv
- `venv`: Nombre del directorio del entorno virtual (puedes usar otro nombre)

#### Paso 3: Activar el entorno virtual

```bash
source venv/bin/activate
```

**Confirmación**: Tu prompt debería cambiar a mostrar `(venv)` al inicio:
```
(venv) usuario@maquina:~/Comparativo-ABB-vs-RedBlack$
```

#### Paso 4: Actualizar pip (recomendado)

```bash
pip install --upgrade pip
```

#### Paso 5: Instalar dependencias

```bash
pip install -r requirements.txt
```

#### Paso 6: Verificar instalación

```bash
python -c "import matplotlib, numpy; print('✅ Dependencias instaladas correctamente')"
```

#### Desactivar el entorno virtual (cuando termines)

```bash
deactivate
```

### 3.2 Instalación en Windows

#### Paso 1: Clonar el repositorio

```cmd
git clone https://github.com/AndresMorenoS/Comparativo-ABB-vs-RedBlack.git
cd Comparativo-ABB-vs-RedBlack
```

#### Paso 2: Crear el entorno virtual

```cmd
# Usando Python launcher (recomendado)
py -m venv venv

# O directamente con python
python -m venv venv
```

#### Paso 3: Activar el entorno virtual

```cmd
# En CMD
venv\Scripts\activate.bat

# En PowerShell
venv\Scripts\Activate.ps1
```

**Nota para PowerShell**: Si encuentras un error de política de ejecución, ejecuta:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Confirmación**: Tu prompt debería cambiar a:
```
(venv) C:\Users\Usuario\Comparativo-ABB-vs-RedBlack>
```

#### Paso 4: Actualizar pip

```cmd
python -m pip install --upgrade pip
```

#### Paso 5: Instalar dependencias

```cmd
pip install -r requirements.txt
```

#### Paso 6: Verificar instalación

```cmd
python -c "import matplotlib, numpy; print('✅ Dependencias instaladas correctamente')"
```

#### Desactivar el entorno virtual

```cmd
deactivate
```

---

## 4. Instalación Sin Entorno Virtual

⚠️ **Advertencia**: No recomendado para uso en producción o desarrollo regular.

### 4.1 Linux/macOS

```bash
# Clonar repositorio
git clone https://github.com/AndresMorenoS/Comparativo-ABB-vs-RedBlack.git
cd Comparativo-ABB-vs-RedBlack

# Instalar dependencias (--user para no requerir sudo)
pip3 install --user -r requirements.txt
```

### 4.2 Windows

```cmd
# Clonar repositorio
git clone https://github.com/AndresMorenoS/Comparativo-ABB-vs-RedBlack.git
cd Comparativo-ABB-vs-RedBlack

# Instalar dependencias
pip install -r requirements.txt
```

### Problemas Comunes Sin Entorno Virtual

1. **Conflictos de versiones**: Otros proyectos pueden requerir versiones diferentes de las mismas librerías
2. **Permisos**: Puede requerir privilegios de administrador/root
3. **Contaminación del sistema**: Instala paquetes globalmente
4. **Difícil de limpiar**: Complicado desinstalar todas las dependencias después

---

## 5. Verificación de la Instalación

### 5.1 Verificar que las dependencias se instalaron

```bash
# Listar paquetes instalados
pip list

# Verificar versiones específicas
pip show matplotlib numpy pillow
```

**Salida esperada**:
```
matplotlib    3.x.x
numpy         1.x.x
pillow        9.x.x
```

### 5.2 Ejecutar prueba rápida

```bash
# Ejecutar demo básico
python demo.py
```

**Salida esperada**: Debe mostrar operaciones de ABB y Red-Black Tree sin errores.

### 5.3 Ejecutar tests unitarios

```bash
# Tests del ABB
python tests/test_bst.py

# Tests del Red-Black Tree
python tests/test_rbt.py
```

**Salida esperada**: Todos los tests deben pasar.

### 5.4 Ejecutar comparativo completo

```bash
python main.py
```

**Salida esperada**: Generación de 10 gráficas PNG en el directorio del proyecto.

---

## 6. Solución de Problemas

### Problema 1: "python: command not found"

**Causa**: Python no está instalado o no está en PATH

**Solución**:
```bash
# Linux (Ubuntu/Debian)
sudo apt update
sudo apt install python3 python3-pip python3-venv

# macOS (con Homebrew)
brew install python3

# Windows: Descargar de python.org e instalar
```

### Problema 2: "No module named 'matplotlib'"

**Causa**: Dependencias no instaladas o entorno virtual no activado

**Solución**:
```bash
# Activar entorno virtual si usas uno
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate.bat  # Windows

# Reinstalar dependencias
pip install -r requirements.txt
```

### Problema 3: Error de importación en matplotlib backend

**Causa**: Falta backend gráfico en sistemas sin interfaz gráfica

**Solución**:
```bash
# Linux sin interfaz gráfica
sudo apt install python3-tk

# O modificar el backend de matplotlib
export MPLBACKEND=Agg
python main.py
```

### Problema 4: "pip: command not found"

**Causa**: pip no está instalado

**Solución**:
```bash
# Linux
sudo apt install python3-pip

# macOS
python3 -m ensurepip --upgrade

# Windows: Reinstalar Python con pip activado
```

### Problema 5: Errores de permisos en Linux/macOS

**Causa**: Intentar instalar paquetes globalmente sin permisos

**Solución 1** (recomendada): Usar entorno virtual
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Solución 2**: Usar flag --user
```bash
pip install --user -r requirements.txt
```

**Solución 3** (no recomendada): Usar sudo
```bash
sudo pip3 install -r requirements.txt
```

### Problema 6: ImportError en numpy

**Causa**: Versión incompatible de numpy para tu arquitectura

**Solución**:
```bash
# Desinstalar e instalar versión compatible
pip uninstall numpy
pip install numpy==1.21.0  # Versión más compatible
```

### Problema 7: Versión de Python incorrecta

**Causa**: Múltiples versiones de Python instaladas

**Solución**:
```bash
# Verificar versión
python3 --version

# Usar versión específica para crear venv
python3.10 -m venv venv

# O usar python launcher en Windows
py -3.10 -m venv venv
```

---

## 7. Dependencias Detalladas

### matplotlib (>=3.5.0)

**Descripción**: Librería para generación de gráficas y visualización de datos

**Uso en el proyecto**:
- Generación de gráficas comparativas de rendimiento
- Visualización de tiempos de inserción y búsqueda
- Gráficas de altura de árboles

**Compatibilidad**:
- Python 3.8-3.12: ✅ Totalmente compatible
- Requiere: numpy, pillow, python-dateutil

**Alternativas**: Si no puedes instalar matplotlib, puedes comentar las líneas de visualización y usar solo las salidas de texto.

### numpy (>=1.21.0)

**Descripción**: Librería fundamental para computación numérica

**Uso en el proyecto**:
- Cálculos de altura óptima logarítmica
- Operaciones matemáticas en análisis de rendimiento
- Soporte para matplotlib

**Compatibilidad**:
- Python 3.8-3.12: ✅ Totalmente compatible
- Versiones compiladas disponibles para todas las plataformas principales

**Nota**: numpy 1.21.0 es compatible con Python 3.8-3.10. Para Python 3.11+, se instalará automáticamente una versión más reciente.

### pillow (>=9.0.0)

**Descripción**: Librería de procesamiento de imágenes (PIL fork)

**Uso en el proyecto**:
- Guardado de gráficas en formato PNG
- Soporte de backend para matplotlib

**Compatibilidad**:
- Python 3.8-3.12: ✅ Totalmente compatible
- Soporta múltiples formatos de imagen

---

## 8. Mejores Prácticas

### ✅ Recomendaciones

1. **Siempre usa entornos virtuales**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # o venv\Scripts\activate en Windows
   ```

2. **Mantén pip actualizado**
   ```bash
   pip install --upgrade pip
   ```

3. **Congela tus dependencias**
   ```bash
   pip freeze > requirements_locked.txt
   ```

4. **Documenta tu versión de Python**
   ```bash
   python --version > python_version.txt
   ```

5. **Usa .gitignore para excluir venv**
   ```
   venv/
   __pycache__/
   *.pyc
   *.png
   ```

### ❌ Evitar

1. No instalar paquetes globalmente sin necesidad
2. No usar `sudo pip` a menos que sea absolutamente necesario
3. No commitear el directorio `venv/` al repositorio
4. No mezclar entornos virtuales y instalaciones globales

---

## 9. Comandos de Referencia Rápida

### Crear y activar entorno virtual

```bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Windows
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Ejecutar el proyecto

```bash
# Con entorno virtual activado
python main.py       # Comparativo completo
python demo.py       # Demostración básica
python gui.py        # Interfaz gráfica (si disponible)
```

### Ejecutar tests

```bash
python tests/test_bst.py
python tests/test_rbt.py
```

### Limpiar y reinstalar

```bash
# Desactivar y eliminar entorno virtual
deactivate
rm -rf venv  # Linux/macOS
rmdir /s venv  # Windows

# Recrear desde cero
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 10. Recursos Adicionales

### Documentación Oficial

- **Python venv**: https://docs.python.org/3/library/venv.html
- **pip**: https://pip.pypa.io/en/stable/
- **matplotlib**: https://matplotlib.org/stable/users/installing.html
- **numpy**: https://numpy.org/install/

### Soporte

Si encuentras problemas no cubiertos en esta guía:

1. Revisa los issues abiertos en GitHub
2. Crea un nuevo issue con:
   - Tu versión de Python
   - Tu sistema operativo
   - El error completo que estás recibiendo
   - Los pasos que seguiste

---

## 11. Preguntas Frecuentes (FAQ)

### ¿Puedo usar conda en lugar de venv?

Sí, conda es una alternativa válida:

```bash
conda create -n comparativo python=3.10
conda activate comparativo
pip install -r requirements.txt
```

### ¿Necesito instalar algo más además de las dependencias en requirements.txt?

No, las tres dependencias listadas (matplotlib, numpy, pillow) son suficientes. Estas librerías instalarán automáticamente sus propias subdependencias.

### ¿El proyecto funciona en Python 2.7?

No, Python 2.7 llegó al fin de su vida útil en 2020. Este proyecto requiere Python 3.8 o superior.

### ¿Puedo ejecutar el proyecto sin interfaz gráfica?

Sí, aunque las gráficas se generan como archivos PNG. En sistemas sin interfaz gráfica, asegúrate de configurar el backend de matplotlib:

```bash
export MPLBACKEND=Agg
python main.py
```

### ¿Cuánto espacio necesita el entorno virtual?

Aproximadamente 150-300 MB dependiendo de tu sistema operativo y versión de Python.

---

**Última actualización**: Noviembre 2024  
**Mantenedores**: Andrés Moreno, Valentina Burgos  
**Licencia**: Código abierto con fines educativos
