@echo off
chcp 65001 >nul
title Curso OpenCode - GitHub Manager
color 0A
cls

:menu
echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║          ENVIAR CAMBIOS A GITHUB - MENU                       ║
echo ╠═══════════════════════════════════════════════════════════════╣
echo ║                                                               ║
echo ║   [1] Ver ESTADO de git (que cambio?)                        ║
echo ║   [2] Agregar TODO al staging (git add .)                    ║
echo ║   [3] Hacer COMMIT (con mensaje)                             ║
echo ║   [4] Subir a GITHUB (git push)                              ║
echo ║   [5] TODO EN UNO: add + commit + push                       ║
echo ║   [6] Ver HISTORIAL de commits                               ║
echo ║   [0] SALIR                                                  ║
echo ║                                                               ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.
set /p opcion="  Selecciona una opcion: "

if "%opcion%"=="1" goto estado
if "%opcion%"=="2" goto agregar
if "%opcion%"=="3" goto commit
if "%opcion%"=="4" goto push
if "%opcion%"=="5" goto todo_en_uno
if "%opcion%"=="6" goto historial
if "%opcion%"=="0" goto salir

echo.
echo Opcion invalida. Intenta de nuevo.
pause >nul
goto menu

:estado
echo.
echo ═══════════════════════════════════════════════════════════════
echo   ESTADO ACTUAL DE GIT
echo ═══════════════════════════════════════════════════════════════
git status
echo.
pause
goto menu

:agregar
echo.
echo ═══════════════════════════════════════════════════════════════
echo   AGREGANDO TODOS LOS CAMBIOS AL STAGING...
echo ═══════════════════════════════════════════════════════════════
git add .
echo.
echo [OK] Cambios agregados al staging.
echo.
pause
goto menu

:commit
echo.
echo ═══════════════════════════════════════════════════════════════
echo   CREAR NUEVO COMMIT
echo ═══════════════════════════════════════════════════════════════
echo.
echo Tipos de commit:
echo   feat:     nueva funcionalidad
echo   fix:      correccion de bug
echo   docs:     documentacion
echo   style:    formato, sin cambios de codigo
echo   refactor: reestructuracion de codigo
echo   chore:    tareas de mantenimiento
echo.
set /p msg="Escribe el mensaje del commit: "
echo.
git commit -m "%msg%"
if errorlevel 1 (
    echo.
    echo [ERROR] No se pudo crear el commit.
    echo         Asegurate de haber agregado cambios primero (opcion 2).
) else (
    echo.
    echo [OK] Commit creado exitosamente.
)
echo.
pause
goto menu

:push
echo.
echo ═══════════════════════════════════════════════════════════════
echo   SUBIENDO A GITHUB...
echo ═══════════════════════════════════════════════════════════════
git push origin master
echo.
if errorlevel 1 (
    echo [ERROR] No se pudo subir.
    echo         Verifica tu conexion a internet o las credenciales.
) else (
    echo [OK] Cambios subidos a GitHub exitosamente!
    echo.
    echo Tu repo: https://github.com/gmolina75/curso-maestro-opencode
)
echo.
pause
goto menu

:todo_en_uno
echo.
echo ═══════════════════════════════════════════════════════════════
echo   ADD + COMMIT + PUSH - TODO EN UNO
echo ═══════════════════════════════════════════════════════════════
echo.
set /p msg="Escribe el mensaje del commit: "
echo.
echo [1/3] Agregando cambios...     
git add .
echo [OK]
echo.
echo [2/3] Creando commit...        
git commit -m "%msg%"
if errorlevel 1 (
    echo.
    echo [ERROR] No se pudo crear el commit. No hay cambios nuevos?
    pause
    goto menu
)
echo [OK]
echo.
echo [3/3] Subiendo a GitHub...     
git push origin master
echo [OK]
echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║              TODO LISTO!                                       ║
echo ╠═══════════════════════════════════════════════════════════════╣
echo ║  Ver online:                                                   ║
echo ║  https://github.com/gmolina75/curso-maestro-opencode          ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.
pause
goto menu

:historial
echo.
echo ═══════════════════════════════════════════════════════════════
echo   HISTORIAL DE COMMITS (ultimos 10)
echo ═══════════════════════════════════════════════════════════════
git log --oneline -10 --graph
echo.
pause
goto menu

:salir
cls
echo.
echo Hasta pronto! 👋
echo.
timeout /t 2 >nul
exit
