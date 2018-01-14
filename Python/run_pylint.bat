@setlocal
@set PYTHONPATH=pylint;%PYTHONPATH%
call pylint --rcfile objectcalisthenics.pylintrc lcd
@endlocal
