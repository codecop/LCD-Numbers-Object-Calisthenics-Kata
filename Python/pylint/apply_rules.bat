@rem run Object Calisthenics rules against sample.py as test
@setlocal
@set PYTHONPATH=.\checkers;%PYTHONPATH%
call pylint --rcfile ../objectcalisthenics.pylintrc .\samples\sample.py
@endlocal
