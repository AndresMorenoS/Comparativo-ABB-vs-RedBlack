#!/bin/bash
# Script de configuración automatizada para Linux/macOS
# Automated setup script for Linux/macOS

set -e  # Salir si hay algún error / Exit on error

echo "========================================"
echo "Configurando Comparativo ABB vs Red-Black"
echo "Setting up ABB vs Red-Black Comparison"
echo "========================================"
echo ""

# Verificar Python / Check Python
echo "🔍 Verificando instalación de Python..."
echo "🔍 Checking Python installation..."

if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
    PYTHON_VERSION=$(python3 --version)
    echo "✅ $PYTHON_VERSION encontrado"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
    PYTHON_VERSION=$(python --version)
    echo "✅ $PYTHON_VERSION encontrado"
else
    echo "❌ Error: Python no está instalado"
    echo "❌ Error: Python is not installed"
    echo "Por favor instala Python 3.8 o superior desde https://www.python.org/"
    echo "Please install Python 3.8 or higher from https://www.python.org/"
    exit 1
fi

echo ""

# Verificar versión de Python / Check Python version
PYTHON_VERSION_NUM=$($PYTHON_CMD -c 'import sys; print(f"{sys.version_info.major}{sys.version_info.minor}")')
if [ "$PYTHON_VERSION_NUM" -lt 38 ]; then
    echo "❌ Error: Se requiere Python 3.8 o superior"
    echo "❌ Error: Python 3.8 or higher is required"
    echo "Versión detectada: $PYTHON_VERSION"
    exit 1
fi

# Crear entorno virtual / Create virtual environment
echo "📦 Creando entorno virtual..."
echo "📦 Creating virtual environment..."

if [ -d "venv" ]; then
    echo "⚠️  El directorio venv ya existe. ¿Deseas eliminarlo y crear uno nuevo? (s/n)"
    echo "⚠️  venv directory already exists. Do you want to remove it and create a new one? (y/n)"
    read -r response
    if [[ "$response" =~ ^([yYsS])$ ]]; then
        rm -rf venv
        echo "🗑️  Directorio venv eliminado"
    else
        echo "❌ Instalación cancelada"
        echo "❌ Installation cancelled"
        exit 1
    fi
fi

$PYTHON_CMD -m venv venv
echo "✅ Entorno virtual creado"
echo ""

# Activar entorno virtual / Activate virtual environment
echo "🔌 Activando entorno virtual..."
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Actualizar pip / Update pip
echo "⬆️  Actualizando pip..."
echo "⬆️  Updating pip..."
pip install --upgrade pip -q
echo "✅ pip actualizado"
echo ""

# Instalar dependencias / Install dependencies
echo "📥 Instalando dependencias..."
echo "📥 Installing dependencies..."
pip install -r requirements.txt
echo "✅ Dependencias instaladas"
echo ""

# Verificar instalación / Verify installation
echo "🧪 Verificando instalación..."
echo "🧪 Verifying installation..."

if $PYTHON_CMD -c "import matplotlib, numpy, PIL" 2>/dev/null; then
    echo "✅ Todas las dependencias están correctamente instaladas"
    echo "✅ All dependencies are correctly installed"
else
    echo "⚠️  Advertencia: Algunas dependencias pueden no haberse instalado correctamente"
    echo "⚠️  Warning: Some dependencies may not have been installed correctly"
fi

echo ""
echo "========================================"
echo "✅ Instalación completada exitosamente!"
echo "✅ Installation completed successfully!"
echo "========================================"
echo ""
echo "Para usar el proyecto / To use the project:"
echo ""
echo "1. Activar el entorno virtual / Activate the virtual environment:"
echo "   source venv/bin/activate"
echo ""
echo "2. Ejecutar el programa / Run the program:"
echo "   python main.py        # Comparativo completo / Full comparison"
echo "   python demo.py        # Demostración rápida / Quick demo"
echo ""
echo "3. Desactivar cuando termines / Deactivate when done:"
echo "   deactivate"
echo ""
echo "📖 Para más información, consulta / For more information, see:"
echo "   - GUIA_INSTALACION.md"
echo "   - INFORME_DETALLADO.md"
echo "   - README.md"
echo ""
