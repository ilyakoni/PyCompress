echo OFF
DEL "%~dp0\compressed\0" /q
DEL "%~dp0\compressed\0" /q
echo Compressing files...
py compressfolder.py
pause