@echo off
REM Script de configuración automatizada para Windows
REM Automated setup script for Windows

echo ========================================
echo Configurando Comparativo ABB vs Red-Black
echo Setting up ABB vs Red-Black Comparison
echo ========================================
echo.

REM Verificar Python / Check Python
echo Verificando instalacion de Python...
echo Checking Python installation...

where python >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Python no esta instalado
    echo ERROR: Python is not installed
    echo Por favor instala Python 3.8 o superior desde https://www.python.org/
    echo Please install Python 3.8 or higher from https://www.python.org/
    pause
    exit /b 1
)

python --version
echo Python encontrado / Python found
echo.

REM Crear entorno virtual / Create virtual environment
echo Creando entorno virtual...
echo Creating virtual environment...

if exist venv (
    echo ADVERTENCIA: El directorio venv ya existe.
    echo WARNING: venv directory already exists.
    echo Deseas eliminarlo y crear uno nuevo? (S/N)
    echo Do you want to remove it and create a new one? (Y/N)
    set /p response=
    if /i "%response%"=="S" goto deletevenv
    if /i "%response%"=="Y" goto deletevenv
    echo Instalacion cancelada / Installation cancelled
    pause
    exit /b 1
    
    :deletevenv
    echo Eliminando directorio venv...
    rmdir /s /q venv
    echo Directorio venv eliminado
)

python -m venv venv
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: No se pudo crear el entorno virtual
    echo ERROR: Could not create virtual environment
    pause
    exit /b 1
)
echo Entorno virtual creado / Virtual environment created
echo.

REM Activar entorno virtual / Activate virtual environment
echo Activando entorno virtual...
echo Activating virtual environment...
call venv\Scripts\activate.bat
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: No se pudo activar el entorno virtual
    echo ERROR: Could not activate virtual environment
    pause
    exit /b 1
)
echo.

REM Actualizar pip / Update pip
echo Actualizando pip...
echo Updating pip...
python -m pip install --upgrade pip --quiet
echo pip actualizado / pip updated
echo.

REM Instalar dependencias / Install dependencies
echo Instalando dependencias...
echo Installing dependencies...
pip install -r requirements.txt
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: No se pudieron instalar las dependencias
    echo ERROR: Could not install dependencies
    pause
    exit /b 1
)
echo Dependencias instaladas / Dependencies installed
echo.

REM Verificar instalación / Verify installation
echo Verificando instalacion...
echo Verifying installation...
python -c "import matplotlib, numpy, PIL" 2>nul
if %ERRORLEVEL% EQU 0 (
    echo Todas las dependencias estan correctamente instaladas
    echo All dependencies are correctly installed
) else (
    echo ADVERTENCIA: Algunas dependencias pueden no haberse instalado correctamente
    echo WARNING: Some dependencies may not have been installed correctly
)

echo.
echo ========================================
echo Instalacion completada exitosamente!
echo Installation completed successfully!
echo ========================================
echo.
echo Para usar el proyecto / To use the project:
echo.
echo 1. Activar el entorno virtual / Activate the virtual environment:
echo    venv\Scripts\activate
echo.
echo 2. Ejecutar el programa / Run the program:
echo    python main.py        # Comparativo completo / Full comparison
echo    python demo.py        # Demostracion rapida / Quick demo
echo.
echo 3. Desactivar cuando termines / Deactivate when done:
echo    deactivate
echo.
echo Para mas informacion, consulta / For more information, see:
echo    - GUIA_INSTALACION.md
echo    - INFORME_DETALLADO.md
echo    - README.md
echo.
pause
