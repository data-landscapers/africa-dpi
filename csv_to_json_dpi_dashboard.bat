@echo off
setlocal EnableExtensions
title CSV to JSON
echo.
echo  Converts a CSV using csv-to-json.py and writes JSON in the same folder.
echo.
set /p "CSVPATH=Enter full path to CSV file: "
if not defined CSVPATH (
  echo No path entered.
  goto :end
)

set "CSVPATH=%CSVPATH:"=%"

if not exist "%CSVPATH%" (
  echo.
  echo File not found:
  echo   %CSVPATH%
  goto :end
)

REM Output: same drive\path\basename as CSV, extension .json
for %%I in ("%CSVPATH%") do set "JSONOUT=%%~dpnI.json"

set "SCRIPT=csv-to-json_dpi_dashboard.py"
if not exist "%SCRIPT%" (
  echo.
  echo Script not found:
  echo   %SCRIPT%
  goto :end
)

python "%SCRIPT%" "%CSVPATH%" "%JSONOUT%"

if errorlevel 1 (
  echo.
  echo Conversion failed. Check Python on PATH and CSV columns expected by the script.
  goto :end
)

echo.
:end
pause
