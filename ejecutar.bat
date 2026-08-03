@echo off
chcp 65001 >nul
title Curso Maestro OpenCode - Generador
color 0B
cls

:menu
echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║       CURSO MAESTRO DE OPENCODE - MENU PRINCIPAL            ║
echo ╠═══════════════════════════════════════════════════════════════╣
echo ║                                                               ║
echo ║   [1] Generar TODAS las presentaciones (desde papers/)       ║
echo ║   [2] Generar SILABO resumido                                ║
echo ║   [3] Generar CASOS DE USO (10 escenarios)                   ║
echo ║   [4] Aplicar tema visual MEJORADO (azul pastel)             ║
echo ║   [5] Ver ESTADISTICAS del curso                             ║
echo ║   [6] Verificar CONFIGURACION del proyecto                   ║
echo ║   [7] Abrir carpeta de PRESENTACIONES                        ║
echo ║   [0] SALIR                                                  ║
echo ║                                                               ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.

set /p opcion="  Selecciona una opcion: "

if "%opcion%"=="1" goto generar_todas
if "%opcion%"=="2" goto generar_silabo
if "%opcion%"=="3" goto generar_casos
if "%opcion%"=="4" goto mejorar
if "%opcion%"=="5" goto estadisticas
if "%opcion%"=="6" goto verificar
if "%opcion%"=="7" goto abrir_carpeta
if "%opcion%"=="0" goto salir

echo.
echo Opcion invalida. Intenta de nuevo.
pause >nul
goto menu

:generar_todas
cls
echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║     GENERANDO TODAS LAS PRESENTACIONES DESDE PAPERS/        ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.
python src\crear_todas_presentaciones.py
if errorlevel 1 (
    echo.
    echo [ERROR] Verifica que tengas python-pptx instalado:
    echo   pip install -r requirements.txt
)
echo.
pause
goto menu

:generar_silabo
cls
echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║              GENERANDO SILABO RESUMIDO                        ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.
python src\crear_silabo.py
if errorlevel 1 (
    echo.
    echo [ERROR] Verifica que tengas python-pptx instalado:
    echo   pip install -r requirements.txt
)
echo.
pause
goto menu

:generar_casos
cls
echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║           GENERANDO CASOS DE USO (10 escenarios)              ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.
python src\crear_presentaciones_casos_de_uso.py
if errorlevel 1 (
    echo.
    echo [ERROR] Verifica que tengas python-pptx instalado:
    echo   pip install -r requirements.txt
)
echo.
pause
goto menu

:mejorar
cls
echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║         APLICANDO TEMA VISUAL MEJORADO (azul pastel)          ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.
python src\mejorar_presentaciones.py
if errorlevel 1 (
    echo.
    echo [ERROR] Verifica que tengas python-pptx instalado:
    echo   pip install -r requirements.txt
)
echo.
pause
goto menu

:estadisticas
cls
echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║              ESTADISTICAS DEL CURSO                           ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.
python src\github_automation.py stats
echo.
pause
goto menu

:verificar
cls
echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║         VERIFICANDO CONFIGURACION DEL PROYECTO                ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.
python src\github_automation.py verify
echo.
pause
goto menu

:abrir_carpeta
cls
echo.
echo Abriendo carpeta de presentaciones...
start presentaciones
goto menu

:salir
cls
echo.
echo Hasta pronto! 👋
echo.
timeout /t 2 >nul
exit
