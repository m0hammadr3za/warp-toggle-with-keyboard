@echo off
REM Build the executable using pyinstaller
pyinstaller --onefile --noconsole script.py

REM Delet build directory and script.spec
rmdir /s /q build
del script.spec

REM Rename the .exe file
rename dist\script.exe "WARP toggle with keyboard".exe

REM Create build directory if it doesn't exist
if not exist build mkdir build

REM Move the WARP toggle with keyboard.exe file to the build directory
move dist\"WARP toggle with keyboard".exe build

REM Delete dist file
rmdir /s /q dist

echo Build creation complete!
pause