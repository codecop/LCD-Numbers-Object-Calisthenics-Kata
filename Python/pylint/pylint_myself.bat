@FOR /F "usebackq delims==" %%i IN (`dir /b *.py`) DO @call pylint %%i
