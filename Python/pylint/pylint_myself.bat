@rem run pylint against the rules' code to find any problems
@FOR /F "usebackq delims==" %%i IN (`dir /b *.py`) DO @call pylint %%i
