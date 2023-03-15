if EXIST %CD%/thisVenv/Scripts/activate.bat goto :Ready
python -m venv %CD%/thisVenv
call %CD%/thisVenv/Scripts/activate.bat
echo this next line should execute
pip3 install -r requirements.txt
goto :launch
:Ready
call %CD%/thisVenv/Scripts/activate.bat
echo %PYTHON%
:launch
%CD%/thisVenv/Scripts/python.exe -m pip install --upgrade pip
echo %reloadGradio%
if %reloadGradio%==y gradio main.py
if NOT %reloadGradio%==y python main.py
pause