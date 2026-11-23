@echo off
setlocal
set "SCRIPT_DIR=%~dp0"
where py >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    py -3 -B "%SCRIPT_DIR%scaffold.py" %*
    exit /b %ERRORLEVEL%
)
where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    python -B "%SCRIPT_DIR%scaffold.py" %*
    exit /b %ERRORLEVEL%
)
echo [SKILL_FAIL] Python 3 not found on Windows PATH. >&2
exit /b 1
