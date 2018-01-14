@if "%OS%"=="Windows_NT" @setlocal
@set PYTHONPATH=pylint;%PYTHONPATH%
call pylint --rcfile objectcalisthenics.pylintrc lcd
@if "%OS%"=="Windows_NT" @endlocal
