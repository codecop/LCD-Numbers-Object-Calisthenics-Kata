@rem run Object Calisthenics rules against sample.py as test
@setlocal
@set PYTHONPATH=.;%PYTHONPATH%
call pylint --rcfile ../objectcalisthenics.pylintrc .\samples\sample.py
@endlocal
