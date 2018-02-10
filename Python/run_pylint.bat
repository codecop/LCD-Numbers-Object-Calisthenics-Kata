@if "%OS%"=="Windows_NT" @setlocal
@rem run Object Calisthenics rules against lcd
@set PYTHONPATH=pylint\checkers;%PYTHONPATH%
call pylint --rcfile objectcalisthenics.pylintrc lcd
@if "%OS%"=="Windows_NT" @endlocal
